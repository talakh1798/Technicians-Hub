// Initialize the map on the 'mapid' div
var mymap = L.map('mapid').setView([31.9465, 35.3027], 10); // Centered on Palestine with a zoom level of 10

// Add OpenStreetMap tiles to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 19
}).addTo(mymap);

// Function to locate the user
function locateUser() {
    if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const latlng = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            // Set the map view to the user's location
            mymap.setView(latlng, 13);

            // Add a marker to show the user's location
            L.marker(latlng).addTo(mymap)
                .bindPopup("You are here!").openPopup();
        }, function() {
            alert("Unable to retrieve your location");
        });
    } else {
        alert("Geolocation is not supported by your browser");
    }
}

// Call the function to locate the user
locateUser();
