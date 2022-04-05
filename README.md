# SeniorProject
2022 Carroll CS Senior Project

A web app that helps students figure out where they need to go on campus.

### Requirements

    % pip install -r requirements.txt

### Setting up database:
Create your database locally in mySQL.
In order to be able to connect to a local database, you must have MySQL installed and an .env file in the project with the following set up:

    MY_HOSTNAME = "yourhost"
    MY_USERNAME = "yourusername"
    MY_PASSWORD = "yourpassword"
    MY_DB = "yourdatabasename"

Then from the mysite directory run these commands.

    % python manage.py makemigrations polls
    % python manage.py migrate polls
    % python manage.py migrate

This creates your tables but not your values in the tables. Next locate SQLAccess.py in mysite/mysite/ and run it. This will create the data values for the tables.

### How to run:

In your command line, navigate to the directory in which the manage.py file resides.
Run this command:

    %python manage.py runserver

In your browser, go to http://127.0.0.1:8000/