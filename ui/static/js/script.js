// script to make an AJAX request to the price predictor REST API
const predictButton = document.querySelector('.predict_button');
predictButton.addEventListener('click', makeRequest);

function makeRequest() {
  jsonData = buildJson();
  updatePrice(jsonData);
}

function buildJson() {
  // building the JSON data for the POST request to the REST API
  const date = document.getElementById('year').value;
  const area = document.getElementById('area').value.replace(/_/g, ' ');
  const housesSold = document.getElementById('houses_sold').value || null;
  const noOfCrimes = document.getElementById('no_of_crimes').value || null;
  const data = {"date": date,
                "area": area,
                "houses_sold": housesSold,
                "no_of_crimes": noOfCrimes,
                };
  console.log(data)
  return data;
}

function updatePrice(jsonData) {
  // AJAX request to the REST API
  const xmlhttp = new XMLHttpRequest();
  xmlhttp.open("POST", "http://127.0.0.1:5000/predict_price", true);
  // xmlhttp.setRequestHeader('Access-Control-Allow-Origin', '*');
  xmlhttp.onreadystatechange = function(){
    if (this.readyState == 4 && this.status == 200) {
      const responsePrediction = JSON.parse(this.responseText);
      const predictionDiv = document.querySelector('.prediction');
      predictionDiv.textContent = responsePrediction.predicted_price;
    }
  }
  xmlhttp.send( JSON.stringify( jsonData ) );
}