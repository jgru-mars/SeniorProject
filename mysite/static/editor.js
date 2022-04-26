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

function WriteToFile() {
    var floor = document.getElementById("floor");
    var floorname = floor.options[floor.selectedIndex].text
    var room = document.getElementById("room");
    if(postext.value!=="" && room.value!=="")
    {
        let data = floorname + "," + room.value + "," + postext.value

        getJSON(window.location.href +'runfunction/?datastring=' + data,
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