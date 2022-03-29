async function submitMethod(currentDrop, nextDrop) {
var y = document.getElementById(currentDrop);
var x = document.getElementById(nextDrop);
  x.parentElement.parentElement.style.display = "block";
  while (x.firstChild) {
   x.removeChild(x.firstChild)
  }

  getJSON('http://127.0.0.1:8000/' + nextDrop + '/?'+ currentDrop + 'value=' + y.options[y.selectedIndex].text,
function(err, data) {
  if (err !== null) {
    alert('Something went wrong: ' + err);
  } else {
    for (let i = 0; i < data.values.length; i++) {
        o = document.createElement("option");
        o.value = data.values[i];
        o.text = data.values[i];
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
    url = 'http://127.0.0.1:8000/image/?floorvalue=' + x.options[y.selectedIndex].text + '&roomvalue=' + y.options[y.selectedIndex].text;
    window.location.href = url;
}