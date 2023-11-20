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
      table += '<thead><tr>';
      
      columnOrder.forEach((key, index) => {
        table += `<th scope="col" onclick="sortTable(${index})" style="cursor:pointer;"><b>${key}</b></th>`;
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
  
  

function sortTable(columnIndex) {
  var table, rows, switching, i, shouldSwitch, direction, switchcount = 0;
  table = document.getElementById("data-table");
  switching = true;
  direction = sortDirections[columnIndex] || 'descending'; 

  while (switching) {
      switching = false;
      rows = table.getElementsByTagName("TR");

      for (i = 1; i < (rows.length - 1); i++) {
          shouldSwitch = false;
          x = rows[i].getElementsByTagName("TD")[columnIndex];
          y = rows[i + 1].getElementsByTagName("TD")[columnIndex];

          var xContent = isNaN(parseFloat(x.innerHTML)) ? x.innerHTML.toLowerCase() : parseFloat(x.innerHTML);
          var yContent = isNaN(parseFloat(y.innerHTML)) ? y.innerHTML.toLowerCase() : parseFloat(y.innerHTML);

          if (direction === 'ascending') {
              if (xContent > yContent) {
                  shouldSwitch = true;
                  break;
              }
          } else if (direction === 'descending') {
              if (xContent < yContent) {
                  shouldSwitch = true;
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