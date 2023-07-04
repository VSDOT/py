from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "index.html"
if__name__ == "__main__":
    app.run(port="8080", host='0.0.0.0')
