from flask import Flask, redirect, render_template, request, url_for, session
import uuid

app = Flask(__name__)

# Set of users allowed to access the super-secret URL
allowed_users = {"nate", "ted", "upperclass"}

# This store the list of valid sessions to determine if a valid user is logged in
active_sessions = dict()


@app.route("/", methods=["GET"])
def start():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def login():
    # Ensure the username was provided, otherwise redirect them back
    username = request.form['username']
    if not username:
        return redirect(url_for('start'))

    # If the user is allowed, set a random session cookie if one doesn't exist
    if username.lower() in allowed_users:
        session_uuid = uuid.uuid4()
        active_sessions[session_uuid] = username
        session['uuid'] = session_uuid
        return "<p>Login Successful</p>"

    return "<p>Permission Denied</p>"


@app.route("/secret")
def secret():
    global active_sessions

    # Fetch the cookie, so we can determine if they are allowed
    # as well as it allows us to lookup their username.
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

# adding a comment to test git push