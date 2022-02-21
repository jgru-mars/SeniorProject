# https://realpython.com/python-sql-libraries/
import mysql.connector
from mysql.connector import Error

# credentials needed for the sql connection
hostname = "localhost"
myusername = "root"
mypassword = "password01"  # make sure to set this to your root password
db = "seniorprojectdb"


def createDB():  # creates the database if it doesn't exist yet.
    newdb = mysql.connector.connect(host=hostname, username=myusername, password=mypassword)
    cursor = newdb.cursor()
    cursor.execute("SHOW DATABASES")  # check all databases
    dbexists = False
    for x in cursor:
        if str(x) == "('seniorprojectdb',)":  # if a db equals this, it exists
            dbexists = True
    if not dbexists:  # if the database doesnt exist, create it!
        try:
            cursor.execute('CREATE DATABASE seniorprojectdb;')
            cursor.execute('CREATE TABLE seniorprojectdb.floor (floorid int NOT NULL AUTO_INCREMENT, '
                           'floorName VARCHAR(45) DEFAULT NULL, plan VARCHAR(50), PRIMARY KEY (userid)) '
                           )
            cursor.execute("INSERT into floor (floorID, floorName, plan) values (1, 'OConnel 1st','OC1.png)")
            cursor.execute("INSERT into floor (floorID, floorName, plan) values (2, 'OConnel 2nd','CharlesS1.png')")
            cursor.execute("INSERT into floor (floorID, floorName, plan) values (3, 'Simperman 3rd','SimpFortin1.png)")

        except Error as e:  # if theres an error catch it and print it
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
