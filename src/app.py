from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.debug=Config.DEBUG
    app.run(host='0.0.0.0', port=5000)