from flask import Flask, redirect, render_template, request, url_for, session
import uuid
import SQLaccess

app = Flask(__name__)

# create database if it doesn't exist yet
SQLaccess.createDB()

# connection to sql database
myconnection = SQLaccess.connectToDB()

# This stores the list of valid sessions to determine if a valid user is logged in
active_sessions = dict()


@app.route("/", methods=["GET"])
def start():  # display the index page
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def login():
    # Ensure the username and password was provided, otherwise redirect them back
    username = request.form['username']
    password = request.form['password']
    if not username or not password:  # they didn't fill in all the fields
        return redirect(url_for('start'))

    # If the SQL query goes through and the login credentials are correct, set a random session cookie if one doesn't
    # exist
    if SQLaccess.validateLogin(myconnection, username, password):
        session_uuid = uuid.uuid4()
        active_sessions[session_uuid] = username
        session['uuid'] = session_uuid
        return "<p>Login Successful</p><br/><br/><a href='secret'>Click here to see your secret!</a>"

    return "<p>Incorrect Login. Permission denied.</p><br/><br/><a href='/'>Back</a>"


@app.route("/register", methods=["GET", "POST"])
def register():  # display the register page
    return render_template('register.html')


@app.route("/createaccount", methods=["POST"])
def createaccount():
    # Ensure all entries were provided and the two password entries are the same, otherwise redirect them back
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    if not email or not username or not password or not password2: # they didn't fill in all the fields
        return "<p>Please fill all fields.</p><br/><br/><a href='register'>Back</a>"
    if password != password2:  # they didn't type the same password
        return "<p>The passwords you entered are not the same.</p><br/><br/><a href='register'>Back</a>"

    # register the user to insert their info into the database
    if SQLaccess.registerUser(myconnection, email, username, password):
        return "<p>Successfully created account!</p><br/><br/><a href='/'>Back to Login.</a>"

    return "<p>Something went wrong.</p><br/><br/><a href='register'>Back</a>"


@app.route("/secret")
def secret():
    global active_sessions

    # Fetch the cookie, so we can determine if they are allowed
    # as well as it allows us to look up their username.
    session_uuid = session.get('uuid')
    if session_uuid is None:
        return "<p>Permission Denied</p>"

    # Ensure we have their name.  If not, make something up
    username = active_sessions[session_uuid]
    if username is None:
        username = 'anonymous'

    return f"<p>Hello {username}</p>"


@app.route("/logout", methods=["GET"])
def logout():
    global active_sessions

    # Clear out the session cookie and remove them from the dict
    session_uuid = session.pop('uuid', None)
    if session_uuid:
        active_sessions.pop('uuid', None)
    return "<p>Goodbye Cruel World!</p>"


if __name__ == '__main__':
    # Configure the secret for sessions
    app.secret_key = "SUPER secret"

    app.run(debug=True)
