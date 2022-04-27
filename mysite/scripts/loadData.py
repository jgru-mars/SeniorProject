import csv

from polls.models import Room, Floor, Building
from mysql.connector import Error


# The command to run is python3 manage.py runscript loadData while in the mysite directory

# https://thewebdev.info/2022/03/27/how-to-import-csv-data-into-python-django-models/
def run():
    with open(
            r'static/roomCoordinates.csv') as f, open(r'static/buildingNames.csv') as b, open(r'static/floorTable.csv') as g:
        roomReader = csv.reader(f)
        buildingReader = csv.reader(b)
        floorReader = csv.reader(g)
        myid = 1
        try:
            # The following loads in the data from buildingNames.csv into the SQL database using models
            # id, name
            for row in buildingReader:
                _, insert = Building.objects.get_or_create(
                    id = row[0],
                    name=row[1]
                )
            # The following loads in the data from floorTable.csv into the SQL database using models
            # id, name, floorimg, building_id
            for row in floorReader:
                _, insert = Floor.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                    floorimg=row[2],
                    building_id=row[3]
                )
            # The following loads in the data from roomCoordinates.csv into the SQL database using models
            # floor_id,roomNumber,XOffset,YOffset
            for row in roomReader:
                _, insert = Room.objects.get_or_create(
                    id=myid,
                    floor_id=row[0],
                    roomNumber=row[1],
                    XOffset=row[2],
                    YOffset=row[3]
                )
                # increases the ID each time it goes through the loop
                myid += 1
        except Error as e:  # if there's an error catch it and print it
            print("ERROR: " + str(e))

