# https://realpython.com/python-sql-libraries/
import mysql.connector
from mysql.connector import Error
import os

from dotenv import load_dotenv

load_dotenv()

# credentials needed for the sql connection
hostname = os.getenv("MY_HOSTNAME")
myusername = os.getenv('MY_USERNAME')
mypassword = os.getenv('MY_PASSWORD')
db = os.getenv('MY_DB')


def createDBvalues():  # creates the database if it doesn't exist yet.
    mydb = mysql.connector.connect(host=hostname, username=myusername, password=mypassword, database=db)
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")  # check all tables
    # floorexists = False
    # buildingexists = False
    # roomexists = False
    # for x in cursor:
    #     if str(x) == "('polls_floor',)":  # if a floor equals this, it exists
    #         floorexists = True
    #     elif str(x) == "('polls_building',)":
    #         buildingexists = True
    #     elif str(x) == "('polls_room',)":
    #         roomexists = True
    # if buildingexists:
    #     try:
    #         cursor.execute("INSERT into polls_building (ID, name) values (1, 'OConnell Hall')")
    #         cursor.execute("INSERT into polls_building (ID, name) values (2, 'St. Charles Hall')")
    #         cursor.execute("INSERT into polls_building (ID, name) values (3, 'Simperman Hall')")
    #         cursor.execute("INSERT into polls_building (ID, name) values (4, 'Library')")
    #         mydb.commit()
    #         print('inserted building values!')
    #     except Error as e:  # if there's an error catch it and print it
    #         print("ERROR: " + str(e))
    # if floorexists:  # if the floor table was just created, add the values
    #     try:
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (1, 'OConnell 1st',"
    #                        "'OC1.png', 1)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (2, 'Charles 1st',"
    #                        "'CharlesS1.png', 2)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (3, 'Charles Ground',"
    #                        "'CharlesGroundFloor.png', 2)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (4, 'Simperman 1st',"
    #                        "'SimpFortin1.png', 3)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (5, 'Simperman 2nd',"
    #                        "'SimpFortin2.png', 3)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (6, 'Simperman 3rd',"
    #                        "'SimpFortin3.png', 3)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (7, 'Simperman 4th',"
    #                        "'SimpFortin4.png', 3)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (8, 'Library 1st',"
    #                        "'Library 1st floor.png', 4)")
    #         cursor.execute("INSERT into polls_floor (ID, name, floorImg, building_id) values (9, 'Library 2nd',"
    #                        "'Library 2nd floor.png', 4)")
    #         mydb.commit()
    #         print('inserted floor values!')
    #     except Error as e:  # if there's an error catch it and print it
    #         print("ERROR: " + str(e))
    # if roomexists:
    #     try:
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(1, 12, 3, 600, 450)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(2, 14, 3, 600, 600)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(3, 17, 3, 780, 620)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(4, 27, 3, 764, 1337)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(5, 34, 3, 550, 1300)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(6, 44, 3, 1020, 1500)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(7, 45, 3, 1000, 1350)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(8, 133, 2, 970, 1400)")
    #         cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values "
    #                        "(9, 140, 2, 500, 1350)")
    #         mydb.commit()
    #         print('inserted room values!')
    #     except Error as e:  # if there's an error catch it and print it
    #         print("ERROR: " + str(e))

# def readDataFromFile():
#     topDir = os.path.dirname(os.path.dirname(os.getcwd()))
#     file1 = open(topDir + '/documentation/roomCoordinates.csv', 'r')
#     mydb = mysql.connector.connect(host=hostname, username=myusername, password=mypassword, database=db)
#     cursor = mydb.cursor()
#     myid = 1
#     try:
#         Lines = file1.readlines()
#         for line in Lines:
#             values = line.split(",")
#             floorid = ""
#             execute = False
#             if values[0] == "charles":
#                 if values[1] == "ground":
#                     floorid = "3"
#                     execute = True
#                 elif values[1] == "1":
#                     floorid = "2"
#                     execute = True
#             elif values[0] == "simp":
#                 if values[1] == "1":
#                     floorid = "4"
#                     execute = True
#                 elif values[1] == "2":
#                     floorid = "5"
#                     execute = True
#                 elif values[1] == "3":
#                     floorid = "6"
#                     execute = True
#                 elif values[1] == "4":
#                     floorid = "7"
#                     execute = True
#             elif values[0] == "ocon":
#                 floorid = "1"
#                 execute = True
#             elif values[0] == "lib":
#                 if values[1] == "1":
#                     floorid = "8"
#                     execute = True
#                 elif values[1] == "2":
#                     floorid = "9"
#                     execute = True
#             if execute:
#                 cursor.execute("INSERT into polls_room (id, roomNumber, floor_id, xOffset, yOffset) values ("
#                                + str(myid) + "," + values[2] + "," + floorid + ", " + values[3] + ", " + values[4] + ")")
#                 myid+=1
#         mydb.commit()
#         print('inserted room values from file!')
#     except Error as e:  # if there's an error catch it and print it
#         print("ERROR: " + str(e))

createDBvalues()
#readDataFromFile()
