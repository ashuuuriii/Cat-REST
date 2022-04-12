// the interface for this project is being implemented without a backend.
const yearDropdown = document.querySelector('#year');
const years = Array.from(new Array(26), (x, i) => i + 1995);
const areaDropdown = document.querySelector('#area');
const areas = ['city_of_london', 'barking_and_dagenham', 'barnet', 'bexley',
               'brent', 'bromley', 'camden', 'croydon', 'ealing', 'enfield',
               'tower_hamlets', 'greenwich', 'hackney', 'south east', 
               'hammersmith and fulham', 'haringey', 'harrow', 'havering',
               'hillingdon', 'hounslow', 'islington', 'kensington_and_chelsea',
               'kingston_upon_thames', 'lambeth', 'lewisham', 'merton', 'newham',
               'redbridge', 'richmond_upon_thames', 'southwark', 'sutton', 
               'waltham_forest', 'wandsworth', 'westminster', 'inner_london',
               'outer_london', 'north_east', 'north_west', 'yorks_and_the_humber',
               'east_midlands', 'west_midlands', 'east_of_england', 'london',
               'south_west', 'england']
populateDropdown(yearDropdown, years);
populateDropdown(areaDropdown, areas)

function populateDropdown(field, data) {
  let newOption;

  for (let opt in data) {
    newOption = document.createElement('option');
    newOption.setAttribute('value', data[opt]);
    newOption.textContent = (typeof data[opt] == 'string') ? cleanString(data[opt]) : data[opt];
    field.appendChild(newOption);
  }
}

function cleanString(str) {
  let retStr = str.replace(/^\w/, c => c.toUpperCase());
  retStr = retStr.replaceAll('_', ' ');
  return retStr;
}