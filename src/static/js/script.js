/**
# 1KLIK Project - User Interface
# CS356 Group Project - Group One
# Abby Boyle, Adam Clacher, Aidan Purdie, James Brown, and Jamie Connelly

# script.js
# Store useful JavaScript functions
**/

function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

//window.onload = function() {
//    console.log("Page fully loaded");
//
//    fetch('/InputReader')
//        .then(response => {
//            console.log("Fetch response received");
//            return response.json();
//        })
//        .then(data => {
//            console.log("JSON data parsed:", data); // Print the data to the console to verify its structure
//            populateForm(data);
//            displayData(data);
//        })
//        .catch(error => console.error('Error fetching JSON:', error)); // Log any errors that occur during the fetch
//};
//
//function populateForm(data) {
//    console.log('Populating form with data:', data);  // Debug log to check the data being used to populate the form
//    if (data.Encoder && data.Encoder[0] && data.Encoder[0].encoder_types) {
//        populateSelect('encoderSelect', data.Encoder[0].encoder_types);
//    } else {
//        console.error("Encoder data not found");
//    }
//
//    if (data.Encoder && data.Encoder[1] && data.Encoder[1].codecs) {
//        populateSelect('codecSelect', data.Encoder[1].codecs);
//    } else {
//        console.error("Codec data not found");
//    }
//
//    if (data.Encoder && data.Encoder[6] && data.Encoder[6].scalability) {
//        populateSelect('scalabilitySelect', data.Encoder[6].scalability);
//    } else {
//        console.error("Scalability data not found");
//    }
//}
//
//function populateSelect(selectId, items) {
//    const select = document.getElementById(selectId);
//    select.innerHTML = '';  // Clear any existing options
//    items.forEach(item => {
//        console.log('Adding item to', selectId, ':', item);  // Debug log for each item being added
//        const option = document.createElement('option');
//        option.value = item.id;
//        option.textContent = item.name;
//        select.appendChild(option);
//    });
//}
//
//function displayData(data) {
//    const jsonData = document.getElementById('jsonData');  // Get the pre element by its ID
//    jsonData.textContent = JSON.stringify(data, null, 2);  // Display the JSON data as a pretty-printed string
//}

function sendFile(event) {

    fetch('/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            alert('File has been sent successfully');
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        if (error.message === 'Failed to fetch') {
            alert('File has been sent successfully'); // Handle specific fetch error
        } else {
            alert('Error: ' + error.message);
        }
    });
}

function toggleDivById(divId) {
        // Get the div element by its ID
        var div = document.getElementById(divId);

        // Toggle between showing and hiding the div
        if (div.style.display === "none" || div.style.display === "") {
            div.style.display = "block";
        } else {
            div.style.display = "none";
        }
    }