from flask import Flask

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


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)




if __name__ == "__main__":
    app.run(debug=True)
    