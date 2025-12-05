from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hellow world"

@app.about("/about")
def about():
    return "Api crud feita com flask"

if __name__ == "__main__":
    app.run(debug=True)