from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/search/<query>")
def search_results(query):
    return f"You Searched For: {query}"

@app.route("/<int:id>")
def integer(id):
    return f"hello {id}"

@app.route("/<float:myfloat>")
def floatmy(myfloat):
    return f"This is the float"

@app.route("/<string:Mystring>")
def mystring(Mystring):
    return f" This is a {type(Mystring).__name__}"

if __name__== "__main__":
    app.run(debug=True) 