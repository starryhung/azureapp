from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Starry, on Azure App Service for Linux"