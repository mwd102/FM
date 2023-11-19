const maxAllowed = 8;
const checkboxes = document.querySelectorAll('input[type="checkbox"]');
var sortDirections = [];
const selectedRolesContainer = document.getElementById('selected-roles');


checkboxes.forEach(checkbox => {
  checkbox.addEventListener('change', function() {
    let checkedCount = document.querySelectorAll('input[type="checkbox"]:checked').length;
    if (checkedCount > maxAllowed) {
      this.checked = false;
    }
    updateSummary();
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
          };
          selectedRolesContainer.appendChild(pill);
      });
      document.getElementById("roleCount").textContent = selectedCheckboxes.length
  } else {
        document.getElementById("roleCount").textContent = "0"
        selectedRolesContainer.innerHTML = '<span class="pill">No roles selected</span>';
  }
}


function fetchDataAndDisplayTable() {
  fetch('/get_data')
      .then(response => response.json())
      .then(data => {
          if (data.length > 0) {
              const table = buildTable(data);
              document.getElementById('data-table-container').innerHTML = table;
              fetch('/clear_data')
          } else {
              document.getElementById('data-table-container').innerHTML = '';
          }
      })
      .catch(error => console.error('Error:', error));
}

function buildTable(data) {
  let table = '<table role="grid" id="data-table" class="table table-striped table-bordered">';

  if (data.length > 0) {
      table += '<thead><tr>';
      Object.keys(data[0]).forEach((key, index) => {
          table += `<th scope="col" onclick="sortTable(${index})" style="cursor:pointer;"><b>${key}</b></th>`;
      });
      table += '</tr></thead>';
  }

  table += '<tbody>';
  data.forEach(row => {
      table += '<tr>';
      Object.values(row).forEach(value => {
          table += `<td>${value}</td>`;
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

updateSummary();
fetchDataAndDisplayTable();