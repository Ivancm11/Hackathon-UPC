from flask import Flask
from flask import send_from_directory, redirect

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route("/")
def main():
    return redirect("index.html")

@app.route("/hola", methods=["GET"])
def holita():
    return "holita"

if __name__ == "__main__":
    app.run(host='0.0.0.0')