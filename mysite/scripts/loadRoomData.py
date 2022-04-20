import csv

from polls.models import Room, Floor
from mysql.connector import Error


# The command to run is python3 manage.py runscript loadRoomData

# https://thewebdev.info/2022/03/27/how-to-import-csv-data-into-python-django-models/
# building,floor,roomNum,XOffset,YOffset, in the csv file this is the format
def run():
    with open(
            r'../documentation/roomCoordinates.txt') as f:
        reader = csv.reader(f)
        myid = 1
        try:
            for row in reader:
                floorid = 0
                execute = False
                if row[0] == "charles":
                    if row[1] == "ground":
                        floorid = 3
                        execute = True
                    elif row[1] == "1":
                        floorid = 2
                        execute = True
                elif row[0] == "simp":
                    if row[1] == "1":
                        floorid = 4
                        execute = True
                    elif row[1] == "2":
                        floorid = 5
                        execute = True
                    elif row[1] == "3":
                        floorid = 6
                        execute = True
                    elif row[1] == "4":
                        floorid = 7
                        execute = True
                elif row[0] == "fortin":
                    if row[1] == "1":
                        floorid = 10
                        execute = True
                    elif row[1] == "2":
                        floorid = 11
                        execute = True
                elif row[0] == "ocon":
                    floorid = 1
                    execute = True
                elif row[0] == "lib":
                    if row[1] == "1":
                        floorid = 8
                        execute = True
                    elif row[1] == "2":
                        floorid = 9
                        execute = True
                if execute:
                    print(floorid)
                    f = Floor.objects.get(id=floorid)
                    _, insert = Room.objects.get_or_create(
                        id=myid,
                        floor=f,
                        roomNumber=row[2],
                        XOffset=row[3],
                        YOffset=row[4]
                    )
                    myid += 1
        except Error as e:  # if there's an error catch it and print it
            print("ERROR: " + str(e))
