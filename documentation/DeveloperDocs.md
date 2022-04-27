## How to add more values to the Building and Floor tables
To add buildings, locate buildingNames.csv in the mysite/static/ folder and input the id, building name, and the building's latitude and longitude to at least 5 decimal places.

To add floors, locate floorTable.csv in the mysite/static/ folder and input the id number, name, the file name of the floor plan image in the static folder, and the id of the building the floor resides in.

This won't actually add the values, you'll need to re-run loadData.py in the scripts folder.

In the mysite directory run this command.

    % python manage.py runscript loadData

## How to use the editor to add more rooms
Run the site using the same command from the Read Me:

    % python manage.py runserver

In your browser, go to http://127.0.0.1:8000/editor

Click on the dropdown and select the building. Click the second dropdown to select the floor. It will then display the floorplan for that room.

Navigate using the scrollbars and locate the room you'd like to mark. Click on the place you'd like to put the marker. It should automatically fill in an input field labeled "coordinates." You may adjust this value if you'd like. Once the marker is in a position you like, input the room number in the input field labeled "roomNumber." Finally, hit the submit button. If everything went well a popup notification will tell you that the value was added.

You can add as many rooms as you like, so long as that room number isn't already in the database. You can navigate to other buildings and floors as you please.

This adds the values to the roomCoordinates.csv file as well as inputs the value into your database programmatically, so you do not need to rerun loadData.py. If you need to recreate your database, roomCoordinates.csv will have all the values you created. 