## How to add more values to the Building and Floor tables
To add buildings, locate buildingNames.csv in the mysite/static/ folder and input the id, building name, and the building's latitude and longitude to at least 5 decimal places.

To add floors, locate floorTable.csv in the mysite/static/ folder and input the id number, name, the file name of the floor plan image in the static folder, and the id of the building the floor resides in.

This won't actually add the values, you'll need to re-run loadData.py in the scripts folder.

In the mysite directory run this command.

    % python manage.py runscript loadData

## How to use the editor
Run the site using the same command from the Read Me:

    % python manage.py runserver

In your browser, go to http://127.0.0.1:8000/editor

To switch between edit modes for building, floor, and room, click on the dropdown labeled "Edit Mode."

This adds the values to the csv files as well as inputs the value into your database programmatically, so you do not need to rerun loadData.py. If you need to recreate your database, your value csv files will have all the values you created. 

### Add more buildings
Enter the name of the building into the text input labeled "Building Name." Next, locate the building on the OpenLayers interactive map. Click on the center of the building, and the Lat and Long input field should update. Click submit to add that value to the database. If all went well, there should be a pop up message notifying that the value has been submitted.

### Add more floors
Click on the building you'd like to add floors to in the dropdown labeled Building Name. Next, in the dropdown labeled "Floor Plan," select the image you would like to use for a floor plan. The image should exist in the static folder beforehand, and it must be a PNG or JPEG. Finally, enter the name of the floor in "Floor Name" and click submit. If all went well, there should be a pop up message notifying that the value has been submitted.

### Add more rooms

Click on the dropdown and select the building. Click the second dropdown to select the floor. It will then display the floorplan for that room.

Navigate using the scrollbars and locate the room you'd like to mark. Click on the place you'd like to put the marker. It should automatically fill in an input field labeled "coordinates." You may adjust this value if you'd like. Once the marker is in a position you like, input the room number in the input field labeled "roomNumber." Finally, hit the submit button. If everything went well a popup notification will tell you that the value was added.

You can add as many rooms as you like, so long as that room number isn't already in the database. You can navigate to other buildings and floors as you please.