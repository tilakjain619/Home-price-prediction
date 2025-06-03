const baseUrl = 'https://home-price-prediction-fmq7.onrender.com'; // Define base URL separately

function onPageLoad() {
    const apiUrl = baseUrl + '/api/get_location_names';
    const uiLocations = document.getElementById('uiLocations');

    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        if (data && data.locations) {
            data.locations.forEach(location => {
                let opt = new Option(location, location);
                uiLocations.appendChild(opt);
            });
        }
    })
    .catch(error => console.log("Error fetching locations:", error));
}

function onClickedEstimatePrice() {
    const sqft = document.getElementById('uiSqft').value;
    const bhk = document.querySelector('input[name="uiBHK"]:checked')?.value;
    const bath = document.querySelector('input[name="uiBathrooms"]:checked')?.value;
    const location = document.getElementById('uiLocations').value;
    const uiEstimatedPrice = document.getElementById('uiEstimatedPrice');

    console.log("Selected Values:", sqft, bhk, bath, location);

    const apiUrl = baseUrl + '/api/predict_home_price';

    fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            total_sqft: sqft,
            location: location,
            bhk: bhk,
            bath: bath
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response Data:", data);
        if (data.estimated_price) {
            uiEstimatedPrice.innerHTML = data.estimated_price.toString() + ' Lakhs';
        } else {
            console.log("Invalid response format");
        }
    })
    .catch(error => console.log("Error predicting price", error));
}

window.onload = onPageLoad;
