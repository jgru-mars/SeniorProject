async function submitMethod(currentDrop, nextDrop) {
var y = document.getElementById(currentDrop);
var x = document.getElementById(nextDrop);
  x.parentElement.parentElement.style.display = "block";
  while (x.firstChild) {
   x.removeChild(x.firstChild)
  }

  if(currentDrop === "building")
  {
    displayBuildingLocation(y.options[y.selectedIndex].text);
    let room = document.getElementById("roomdiv");
    room.style.display = "none";
  }

  getJSON('http://127.0.0.1:8000/' + nextDrop + '/?'+ currentDrop + 'value=' + y.options[y.selectedIndex].text,
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
  o = document.createElement("option");
  o.setAttribute("disabled", "disabled")
  o.setAttribute("selected", "selected")
  o.text = " -- SELECT -- ";
  x.appendChild(o);
    for (let i = 0; i < data.values.length; i++) {
        o = document.createElement("option");
        o.value = data.values[i];
        o.text = data.values[i];
        o.class = "dropdwn-content"
        x.appendChild(o);
    }
  }
});
}

var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};

function displayImagePage(floor,room)
{
    var x = document.getElementById(floor);
    var y = document.getElementById(room);
    var option1 = x.options[x.selectedIndex]
    var option2 = y.options[y.selectedIndex]
    if(option1 !== undefined && option2 !== undefined)
    {
        url = 'http://127.0.0.1:8000/image/?floorvalue=' + option1.text + '&roomvalue=' + option2.text;
        window.location.href = url;
    }
    else
    {
        alert('Something went wrong. That value might not be in our database yet.');
    }

}

function displayBuildingLocation(building)
{
    var x = 0;
    var y = 0;
    var indicator = document.getElementById("indicator");
    if (building==="Library")
    {
        x = 100;
        y = 250;
        zoomLoc(46.60205948571197, -112.03806097729837);
    }
    else if (building==="OConnell Hall")
    {
        x = 420;
        y = 680;
        zoomLoc(46.600815, -112.040290);
    }
    else if (building==="Simperman Hall")
    {
        x = 680;
        y = 150;
        zoomLoc(46.599812, -112.037358);
    }
    else if (building==="St. Charles Hall")
    {
        x = 400;
        y = 380;
        zoomLoc(46.600947, -112.038586);
    }
    indicator.style.display = "block";
    indicator.style.left = x + 'px';
    indicator.style.top = y + 'px';
}

// Initialize and add the map
function initMap() {
  // The location of campus
  const campus= { lat: 46.60075279618787, lng: -112.03867441629914 };
  // The map, centered at campus
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 17,
    center: campus,
  });
  // The marker, positioned at campus
  const marker = new google.maps.Marker({
    position: campus,
    map: map,
  });
}

function zoomLoc(latitude, longitude)
{
  const campus= { lat: latitude, lng: longitude};
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 18,
    center: campus,
  });
  const marker = new google.maps.Marker({
    position: campus,
    map: map,
  });
}
