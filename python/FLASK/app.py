from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to this flask course </h1>"

@app.route("/index")
def index():
    return "Welcome to the index page"
if __name__ =="__main__":
    app.run(debug=True)