from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Michigan Activity App!"


@app.route('/activities')
def activities():
    return "Here is a list of activities."


@app.route('/badges')
def badges():
    return "Here are your badges."


@app.route('/schedulingActivities')
def schedulingActivities():
    return "Here are your badges."


# Route for handling the login page 
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        users = load_users()
        if username in users:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only letters and numbers!'
        else:
            users[username] = {'password': password, 'email': email}
            save_users(users)
            msg = 'You have successfully registered!'
    return render_template('register.html', msg=msg)




if __name__ == "__main__":
    app.run(debug=True)
    