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


@app.route('/login')
def login():
    return "Here are your badges."




if __name__ == "__main__":
    app.run(debug=True)
    