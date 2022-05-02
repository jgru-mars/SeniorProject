async function submitMethod(currentDrop, nextDrop) {
var y = document.getElementById(currentDrop);
var x = document.getElementById(nextDrop);
  x.parentElement.parentElement.style.display = "block";
  while (x.firstChild) {
   x.removeChild(x.firstChild)
  }

  if(currentDrop === "building")
  {
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

var indicator = document.getElementById('indicator');

function displayImagePage(floor)
{
    let room = document.getElementById("roomdiv");
    room.style.display = "block";
    var x = document.getElementById(floor);
    var img = document.getElementById('myimage');
    img.addEventListener("click", getClickPosition, false);
    var option1 = x.options[x.selectedIndex]
    if(option1 !== undefined)
    {
        img.style.display = "block";
        indicator.style.display = "block";
        getJSON(window.location.href +'image/?floorvalue=' + option1.text,
        function(err, data) {
        if (err !== null) {
        alert('Something went wrong: ' + err);
        } else {
          img.src = staticloc + data.value;
          }
        });
    }
    else
    {
        alert('Something went wrong. That value might not be in our database yet.');
    }
}
var postext = document.getElementById('newpos');

function getClickPosition(e)
{
    var parent = document.getElementById('parentDiv');
    var rect = parent.getBoundingClientRect();
    var xPosition = e.clientX - rect.left - 25;
    var yPosition = e.clientY - rect.top - 25;

    postext.value = xPosition + "," + yPosition;
    indicator.style.left = xPosition + 'px';
    indicator.style.top = yPosition + 'px';
}

function changeCoordVal()
{
    const myvals = postext.value.split(",")
    if(myvals[0] && myvals[1])
    {
        indicator.style.left = myvals[0] + 'px';
        indicator.style.top = myvals[1] + 'px';
    }

}

var insertBuilding = true;
var insertFloor = false;
var insertRoom = false;


function WriteToFile(filename) {
    var latlonginput = document.getElementById('latlonginput');
    var floorname = document.getElementById('floorname');
    var floorinput = document.getElementById('floorinput');
    var floorbuilding = document.getElementById('floorbuilding');
    var floor = document.getElementById("floor");
    var room = document.getElementById("room");
    var building = document.getElementById("buildname");
    var mydata = null;
    if(latlonginput.value!=="" && building.value!=="" && insertBuilding)
    {
        mydata = building.value + "," + latlonginput.value;
    }
    else if (floorname.value!=="" && floorinput.options[floorinput.selectedIndex].text!=="" && insertFloor)
    {
        mydata = floorname.value + ',' + floorinput.options[floorinput.selectedIndex].text + ',' + floorbuilding.options[floorbuilding.selectedIndex].text
    }
    else if (postext.value!=="" && room.value!=="" && insertRoom)
    {
        var floorname = floor.options[floor.selectedIndex].text
        mydata = floorname + "," + room.value + "," + postext.value;
    }

    if(mydata!==null){
        getJSON(window.location.href +'runfunction/?datastring=' + mydata + "&file=" + filename,
            function(err, data) {
            if (err !== null) {
            alert('Something went wrong: ' + err);
            } else {
              alert(data.result)
              }
            });
    }
    else
    {
        alert("Please fill in all values")
    }
}

const view = new ol.View({
          center: ol.proj.fromLonLat([-112.03867441629914, 46.60075279618787]),
          zoom: 17
        })

// Initialize and add the map
var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
    view: view

});


map.on('click', function(e) {
    var lonlat = ol.proj.transform(e.coordinate, 'EPSG:3857', 'EPSG:4326')
    latlonginput.value = lonlat;
});


function getFloorPlans() {
  var floorinput = document.getElementById('floorinput');
  floorinput.parentElement.parentElement.style.display = "block";

  while (floorinput.firstChild) {
   floorinput.removeChild(floorinput.firstChild) //clear out list
  }

    getJSON('http://127.0.0.1:8000/editor/getFiles/',
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
  o = document.createElement("option");
  o.setAttribute("disabled", "disabled")
  o.setAttribute("selected", "selected")
  o.text = " -- SELECT -- "
  floorinput.appendChild(o);
    for (let i = 0; i < data.filename.length; i++) {
        o = document.createElement("option");
        o.value = data.filename[i];
        o.text = data.filename[i];
        o.class = "dropdwn-content"
        floorinput.appendChild(o);
    }
  }
});
}

function switchMode()
{
    var editmode = document.getElementById('editmode');
    var buildiv = document.getElementById('AddBuilding');
    var floordiv = document.getElementById('AddFloor');
    var roomdiv = document.getElementById('AddRoom');
    if(editmode.options[editmode.selectedIndex].value==="building")
    {
        insertBuilding = true;
        insertFloor = false;
        insertRoom = false;
        buildiv.style.display = "block";
        floordiv.style.display = "none";
        roomdiv.style.display = "none";
    }
    else if(editmode.options[editmode.selectedIndex].value==="floor")
    {
        insertBuilding = false;
        insertFloor = true;
        insertRoom = false;
        buildiv.style.display = "none";
        floordiv.style.display = "block";
        roomdiv.style.display = "none";
    }
    else if(editmode.options[editmode.selectedIndex].value==="room")
    {
        insertBuilding = false;
        insertFloor = false;
        insertRoom = true;
        buildiv.style.display = "none";
        floordiv.style.display = "none";
        roomdiv.style.display = "block";
    }
}