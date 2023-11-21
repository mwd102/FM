const maxAllowed = 8;
const checkboxes = document.querySelectorAll('input[type="checkbox"]');
var sortDirections = [];
let selectionOrder = 0;
const selectedRolesContainer = document.getElementById('selected-roles');

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("modeToggle").addEventListener("click", modeToggle);
});


function updateLocalStorage() {
    const savedCheckboxes = Array.from(checkboxes).map(checkbox => ({
        value: checkbox.value,
        code: checkbox.dataset.code,
        checked: checkbox.checked,
        order: checkbox.checked ? checkbox.dataset.order : null

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
                if (savedCheckbox.checked) {
                    checkbox.dataset.order = savedCheckbox.order;
                }
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
        else if (this.checked) {
            const maxOrder = Math.max(0, ...Array.from(checkboxes).filter(cb => cb.checked && cb !== this).map(cb => parseInt(cb.dataset.order || 0, 10)));
            this.dataset.order = maxOrder + 1;
        }
        updateSummary();
        updateLocalStorage();
    });
});

function updateSummary() {
    const selectedRolesContainer = document.getElementById('selected-roles');
    selectedRolesContainer.innerHTML = '';
    const selectedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked);
    selectedCheckboxes.sort((a, b) => (a.dataset.order || 0) - (b.dataset.order || 0));

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


    const savedCheckboxes = JSON.parse(localStorage.getItem('selectedCheckboxes')) || [];
    const savedOrderMap = new Map(savedCheckboxes.map(item => [item.code, parseInt(item.order, 10)]));
          

    
    let dynamicColumns = Array.from(new Set(data.reduce((acc, row) => acc.concat(Object.keys(row)), [])))
    .filter(key => !staticColumns.includes(key))
    .sort((a, b) => {
        const orderA = savedOrderMap.get(a) || 1000;
        const orderB = savedOrderMap.get(b) || 1000;
        return orderA - orderB;
    });
    

    const columnOrder = staticColumns.concat(dynamicColumns);
      
  
    if (data.length > 0) {
        
        showExportButton();
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

  

function exportTableToHTML() {
    const table = document.getElementById('data-table').cloneNode(true);
    
    if (table.tHead.rows.length > 1) {
        table.tHead.deleteRow(1); //deleting search row...
    }

    const style = `
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                border: 1px solid #ddd;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
        </style>
    `;


    const tableHTML = style + table.outerHTML;
    const filename = 'table_export.html';
    const blob = new Blob([tableHTML], { type: 'text/html' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function showExportButton() {
    const exportButton = document.getElementById('export-button');
    exportButton.style.display = 'block';

    if (!exportButton.getAttribute('data-click-assigned')) {
        exportButton.addEventListener('click', function(event) {
            event.preventDefault(); 
            exportTableToHTML(); 
        });
        exportButton.setAttribute('data-click-assigned', 'true');
    }
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

$(document).ready(function () {
    $("#searchInput").on("input", function () {
        updateFilter($(this).val().toLowerCase());
    });

    $("#clearSearch").on("click", function (e) {
        e.preventDefault()
        $("#searchInput").val("");
        updateFilter("");
    });

    function updateFilter(searchValue) {
        $(".filter-item").each(function () {
            var text = $(this).text().toLowerCase();
            if (text.indexOf(searchValue) === -1) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });
    }
});

updateSummary();
fetchDataAndDisplayTable();