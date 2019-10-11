from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "hola"

@app.route("/hola", methods=["GET"])
def holita():
    return "holita"

if __name__ == "__main__":
    app.run(host='0.0.0.0')