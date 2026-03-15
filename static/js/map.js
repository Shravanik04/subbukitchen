// map.js – Delivery location picker using Leaflet + OpenStreetMap

let map, marker;

function initMap(defaultLat = 13.0827, defaultLng = 80.2707) {
  if (map) return; // already initialized

  map = L.map('map').setView([defaultLat, defaultLng], 13);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 19
  }).addTo(map);

  // Custom saffron marker icon
  const icon = L.divIcon({
    html: `<div style="
      background: #FF6B00;
      width: 28px; height: 28px;
      border-radius: 50% 50% 50% 0;
      transform: rotate(-45deg);
      border: 3px solid white;
      box-shadow: 0 2px 8px rgba(0,0,0,0.35);
    "></div>`,
    iconSize: [28, 28],
    iconAnchor: [14, 28],
    className: ''
  });

  // Click to place / move marker
  map.on('click', (e) => {
    placeMarker(e.latlng.lat, e.latlng.lng, icon);
  });

  // Try to get user location
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      pos => {
        const { latitude, longitude } = pos.coords;
        map.setView([latitude, longitude], 15);
        placeMarker(latitude, longitude, icon);
      },
      () => {} // silently fail
    );
  }
}

function placeMarker(lat, lng, icon) {
  if (marker) {
    marker.setLatLng([lat, lng]);
  } else {
    marker = L.marker([lat, lng], { icon, draggable: true }).addTo(map);
    marker.on('dragend', () => {
      const pos = marker.getLatLng();
      updateCoords(pos.lat, pos.lng);
    });
  }
  updateCoords(lat, lng);
}

function updateCoords(lat, lng) {
  document.getElementById('latitude').value = lat.toFixed(6);
  document.getElementById('longitude').value = lng.toFixed(6);

  const coordsDisplay = document.getElementById('coords-display');
  if (coordsDisplay) {
    coordsDisplay.textContent = `📍 ${lat.toFixed(5)}, ${lng.toFixed(5)}`;
  }

  // Reverse geocode for address hint
  fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`)
    .then(r => r.json())
    .then(data => {
      if (data.display_name) {
        const addrField = document.getElementById('address');
        if (addrField && !addrField.value) {
          addrField.value = data.display_name;
        }
      }
    })
    .catch(() => {});
}

// Expose for order.html
window.initDeliveryMap = initMap;
