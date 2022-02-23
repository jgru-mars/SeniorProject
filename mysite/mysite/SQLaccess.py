# https://realpython.com/python-sql-libraries/
import mysql.connector
from mysql.connector import Error
import os
#from dotenv import load_dotenv

#load_dotenv()

# credentials needed for the sql connection
hostname = "localhost"
myusername = "root"
#mypassword = os.getenv('MY_PASSWORD')
mypassword = "austinMySQL01!"
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
            cursor.execute('CREATE TABLE seniorprojectdb.floor (floorid int NOT NULL AUTO_INCREMENT, '
                           'floorName VARCHAR(45) DEFAULT NULL, plan VARCHAR(50), PRIMARY KEY (floorid)) ')
            print('database created!')
        except Error as e:  # if there's an error catch it and print it
            print("ERROR: " + str(e))

        mydb = mysql.connector.connect(host=hostname, username=myusername, password=mypassword, database = db)
        cursor = mydb.cursor()
        try:
            cursor.execute("INSERT into floor (floorID, floorName, plan) values (1, 'OConnell 1st','OC1.png')")
            cursor.execute("INSERT into floor (floorID, floorName, plan) values (2, 'Charles 1st','CharlesS1.png')")
            cursor.execute("INSERT into floor (floorID, floorName, plan) values (3, 'Simperman 1st','SimpFortin1.png')")
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
        cursor.execute("SELECT plan from floor where floorName = '" + value + "'")
        connection.commit()  # confirm changes
        result = cursor.fetchall()  # gets the result of the query
        print("The Query was executed successfully with the result " + str(result[0][0]))
    except Error as e:
        print("ERROR: " + str(e))
    return str(result[0][0])


createDB()
