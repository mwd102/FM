const maxAllowed = 8;
const checkboxes = document.querySelectorAll('input[type="checkbox"]');
var sortDirections = [];
const selectedRolesContainer = document.getElementById('selected-roles');

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("modeToggle").addEventListener("click", modeToggle);
});

function updateLocalStorage() {
    const savedCheckboxes = Array.from(checkboxes).map(checkbox => ({
        value: checkbox.value,
        checked: checkbox.checked
    }));
    localStorage.setItem('selectedCheckboxes', JSON.stringify(savedCheckboxes));
}

function restoreCheckboxesState() {
    const savedCheckboxes = JSON.parse(localStorage.getItem('selectedCheckboxes'));
    if (savedCheckboxes) {
        savedCheckboxes.forEach(savedCheckbox => {
            const checkbox = Array.from(checkboxes).find(c => c.value === savedCheckbox.value);
            if (checkbox) {
                checkbox.checked = savedCheckbox.checked;
            }
        });
        updateSummary();
    }
}

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        let checkedCount = document.querySelectorAll('#roleField input[type="checkbox"]:checked').length;
        if (checkedCount > maxAllowed) {
            this.checked = false;
        }
        updateSummary();
        updateLocalStorage();
    });
});

function updateSummary() {
    const selectedRolesContainer = document.getElementById('selected-roles');
    selectedRolesContainer.innerHTML = '';
    const selectedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked);

    if (selectedCheckboxes.length > 0) {
        selectedCheckboxes.forEach(checkbox => {
            const pill = document.createElement('span');
            pill.textContent = checkbox.nextSibling.textContent.trim();
            pill.classList.add('pill');
            pill.onclick = function() {
                checkbox.checked = false;
                updateSummary();
                updateLocalStorage();
            };
            selectedRolesContainer.appendChild(pill);
        });
        document.getElementById("roleCount").textContent = selectedCheckboxes.length;
    } else {
        selectedRolesContainer.innerHTML = '<span class="pill">No roles selected</span>';
        document.getElementById("roleCount").textContent = "0";
    }
}

document.addEventListener('DOMContentLoaded', restoreCheckboxesState);

function fetchDataAndDisplayTable() {
  fetch('/get_data')
      .then(response => response.json())
      .then(data => {
          if (data.length > 0) {
              const table = buildTable(data);
              document.getElementById('data-table-container').innerHTML = table;
              fetch('/clear_data');
          } else {
              document.getElementById('data-table-container').innerHTML = '';
          }
      })
      .catch(error => console.error('Error:', error));
}

function buildTable(data) {
    let table = '<table role="grid" id="data-table" class="table table-striped table-bordered">';
  
    const staticColumns = [
        'Inf', 'Name', 'Age', 'Club', 'Transfer Value', 'Wage', 'Nat', 'Position',
         'Personality', 'Media Handling', 'Left Foot', 'Right Foot', 'Spd', 'Jum',
          'Str', 'Work', 'Height'];

    const dynamicColumns = Array.from(new Set(data.reduce((acc, row) => acc.concat(Object.keys(row)), []).filter(key => !staticColumns.includes(key))));

    const columnOrder = staticColumns.concat(dynamicColumns);
  
    if (data.length > 0) {
        // Header row for column titles
        table += '<thead><tr>';
        columnOrder.forEach((key, index) => {
            table += `<th scope="col" onclick="sortTable(${index})" style="cursor:pointer;"><i class="fa-solid fa-sort fa-2xs"></i><br><b>${key}</b></th>`;
          });
        table += '</tr>';

        table += '<tr>';
        columnOrder.forEach((key, index) => {
            table += `
                <th scope="col">
                    <input type="text" class="form-control" onkeyup="filterTable(${index}, this.value)" placeholder="">
                </th>`;
        });
        table += '</tr></thead>';
    }
  
    table += '<tbody>';
    data.forEach(row => {
      table += '<tr>';
      columnOrder.forEach(key => {
        table += `<td>${row[key] || ''}</td>`;
      });
      table += '</tr>';
    });
    table += '</tbody></table>';
    return table;
  }

function filterTable(columnIndex, searchTerm) {
    var table, tr, td, i, txtValue;
    table = document.getElementById("data-table");
    tr = table.getElementsByTagName("tr");
    searchTerm = searchTerm.toUpperCase();

    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[columnIndex];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(searchTerm) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}
  
  

function sortTable(columnIndex) {
    var table, rows, switching, i, shouldSwitch, direction, switchcount = 0;
    table = document.getElementById("data-table");
    switching = true;
    direction = sortDirections[columnIndex] || 'descending';
  
    let elements = document.getElementsByClassName("fa-2xs");
  
      for (let i = 0; i < elements.length; i++) {
          let element = elements[i];
          element.classList.remove("fa-sort-up", "fa-sort-down");
          element.classList.add("fa-sort");
      }
  
    while (switching) {
        switching = false;
        rows = table.getElementsByTagName("TR");
  
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[columnIndex];
            y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
        
            if (x && y) {
                let xContent = isNaN(parseFloat(x.innerHTML)) ? x.innerHTML.toLowerCase() : parseFloat(x.innerHTML);
                let yContent = isNaN(parseFloat(y.innerHTML)) ? y.innerHTML.toLowerCase() : parseFloat(y.innerHTML);
        
                let iconElement = document.getElementsByClassName("fa-2xs")[columnIndex];
        
                if ((direction === 'ascending' && xContent < yContent) ||
                    (direction === 'descending' && xContent > yContent)) {
                    shouldSwitch = true;
        
                    if (direction === 'ascending') {
                        iconElement.classList.remove("fa-sort-up", "fa-sort");
                        iconElement.classList.add("fa-sort-down");
                    } else {
                        if (iconElement.classList.contains("fa-sort")) {
                            iconElement.classList.remove("fa-sort");
                        } else {
                            iconElement.classList.remove("fa-sort-down");
                        }
                        iconElement.classList.add("fa-sort-up");
                    }
                    break;
                }
            }
        }
        
        
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount === 0 && direction === 'ascending') {
                direction = 'descending';
                switching = true;
            }
        }
    }
    sortDirections[columnIndex] = (direction === 'ascending') ? 'descending' : 'ascending';
  }

//Toggle Light/Dark Mode
function modeToggle() {
    let element = document.body;
    let modeButton = document.getElementById("modeToggle");
    let modeIcon = modeButton.querySelector("i"); // Select the icon inside the button

    if (element.dataset.bsTheme == "light") {
        element.dataset.bsTheme = "dark";
        modeIcon.classList.remove("fa-moon"); // Remove the moon icon
        modeIcon.classList.add("fa-sun"); // Add the sun icon
    } else {
        element.dataset.bsTheme = "light";
        modeIcon.classList.remove("fa-sun"); // Remove the sun icon
        modeIcon.classList.add("fa-moon"); // Add the moon icon
    }
}

updateSummary();
fetchDataAndDisplayTable();