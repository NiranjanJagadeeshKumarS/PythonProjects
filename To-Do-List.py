import flask




app = Flask(__name__)

@app.route("/")

def home():
    return "Home"

app.run(debug=True)





