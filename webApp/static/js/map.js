let map;
let marker;
let autocomplete;
const position = { lat: -34.397, lng: 150.644 }; 
const input = document.getElementById("place_input");

function initMap() {
  map = new google.maps.Map(document.getElementById("map_google"), {
    center: position,
    zoom: 15,
  });
  marker = new google.maps.Marker({
    position: position,
    map: map,
  })

  InitAutocomplete();
}

function InitAutocomplete(){
    autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.addListener('place_changed', function(){
        const place = autocomplete.getPlace();
        console.log(place)
        map.setCenter(place.geometry.location)
        marker.setPosition(place.geometry.location)
    });
}

window.initMap = initMap;