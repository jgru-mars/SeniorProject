# https://realpython.com/python-sql-libraries/
import mysql.connector
from mysql.connector import Error
import os

# from dotenv import load_dotenv

# load_dotenv()

# credentials needed for the sql connection
hostname = "localhost"
myusername = "root"
# mypassword = os.getenv('MY_PASSWORD')
mypassword = "password01"
db = "seniorprojectdb"


def createDB():  # creates the database if it doesn't exist yet.
    newdb = mysql.connector.connect(host=hostname, username=myusername, password=mypassword)
    cursor = newdb.cursor()
    cursor.execute("SHOW DATABASES")  # check all databases
    dbexists = False
    for x in cursor:
        if str(x) == "('seniorprojectdb',)":  # if a db equals this, it exists
            dbexists = True
    if not dbexists:  # if the database doesn't exist, create it!
        try:
            cursor.execute('CREATE DATABASE seniorprojectdb;')
            cursor.execute('CREATE TABLE seniorprojectdb.polls_floor (id int NOT NULL AUTO_INCREMENT, name VARCHAR(45) '
                           'DEFAULT NULL, floorImg VARCHAR(50), building int, PRIMARY KEY (id)) ')
            cursor.execute('CREATE TABLE seniorprojectdb.polls_building (id int NOT NULL AUTO_INCREMENT, '
                           'name VARCHAR(45) DEFAULT NULL, PRIMARY KEY (id)) ')
            cursor.execute('CREATE TABLE seniorprojectdb.polls_rooms (id int NOT NULL AUTO_INCREMENT, '
                           'roomNumber int, floor int, xOffset int, yOffset int, PRIMARY KEY (id))')
            print('database created!')
        except Error as e:  # if there's an error catch it and print it
            print("ERROR: " + str(e))

        mydb = mysql.connector.connect(host=hostname, username=myusername, password=mypassword, database=db)
        cursor = mydb.cursor()
        try:
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (1, 'OConnell 1st',"
                           "'OC1.png', 1)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (2, 'Charles 1st',"
                           "'CharlesS1.png', 2)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (3, 'Charles Ground',"
                           "'CharlesGroundFloor.png', 2)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (4, 'Simperman 1st',"
                           "'SimpFortin1.png', 3)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (5, 'Simperman 2nd',"
                           "'SimpFortin2.png', 3)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (6, 'Simperman 3rd',"
                           "'SimpFortin3.png', 3)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (7, 'Simperman 4th',"
                           "'SimpFortin4.png', 3)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (8, 'Library 1st',"
                           "'Library 1st floor.png', 4)")
            cursor.execute("INSERT into polls_floor (ID, name, floorImg, building) values (9, 'Library 2nd',"
                           "'Library 2nd floor.png', 4)")
            cursor.execute("INSERT into polls_building (ID, name) values (1, 'OConnell Hall')")
            cursor.execute("INSERT into polls_building (ID, name) values (2, 'St. Charles Hall')")
            cursor.execute("INSERT into polls_building (ID, name) values (3, 'Simperman Hall')")
            cursor.execute("INSERT into polls_building (ID, name) values (4, 'Library')")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 12, 3, 600, 450)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 14, 3, 600, 600)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 17, 3, 780, 620)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 27, 3, 764, 1337)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 34, 3, 550, 1300)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 44, 3, 1020, 1500)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 45, 3, 1000, 1350)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 133, 2, 1000, 1300)")
            cursor.execute("INSERT into polls_rooms (id, roomNumber, floor, xOffset, yOffset) values "
                           "(1, 140, 2, 500, 1400)")
            mydb.commit()
            print('inserted values!')
        except Error as e:  # if there's an error catch it and print it
            print("ERROR: " + str(e))


def connectToDB():  # returns a connection to the database using the credentials at the top of the program
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            username=myusername,
            password=mypassword,
            database=db
        )
        print("We have connected to " + db + " successfully!")
    except Error as e:
        print("ERROR: " + str(e))
    return connection


def getFloorImg(connection, value):
    result = ""
    cursor = connection.cursor(buffered=True)  # create a buffered cursor based off the connection
    try:
        cursor.execute("SELECT floorImg from floor where floorName = '" + value + "'")
        connection.commit()  # confirm changes
        result = cursor.fetchall()  # gets the result of the query
        print("The Query was executed successfully with the result " + str(result[0][0]))
    except Error as e:
        print("ERROR: " + str(e))
    return str(result[0][0])


def getBuildings(connection):
    result = ""
    cursor = connection.cursor(buffered=True)  # create a buffered cursor based off the connection
    try:
        cursor.execute("SELECT buildingName from building")
        connection.commit()  # confirm changes
        result = cursor.fetchall()  # gets the result of the query
        print("The Query was executed successfully with the result " + str(result))
    except Error as e:
        print("ERROR: " + str(e))
    return result


def getFloors(connection, building):
    cursor = connection.cursor(buffered=True)  # create a buffered cursor based off the connection
    try:
        cursor.execute(
            "SELECT floorName from floor where building ="
            "(SELECT id from building where buildingName = '" + building + "')")
        connection.commit()  # confirm changes
        result = cursor.fetchall()  # gets the result of the query
        print("The Query was executed successfully with the result " + str(result))
    except Error as e:
        print("ERROR: " + str(e))
    myresult = [''] * len(result)
    for i in range(len(result)):
        myresult[i] = result[i][0]
    return myresult


createDB()


class csvLine():

    def __init__(self, row):
        self.building = row[0]
        self.floor = row[1]
        self.roomNum = row[2]
        self.xOffset = row[3]
        self.yOffset = row[4]
