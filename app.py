from flask import Flask
from flask import send_from_directory, redirect, request
import os

app = Flask(__name__, static_folder='static', static_url_path='')
path_to_upload = "/home/victor/Hackathon-UPC/upload" # change in docker

@app.route("/")
def main():
    return redirect("index.html")

@app.route("/hola", methods=["GET"])
def holita():
    return "holita"


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("Not a file")
            return "NO"
        file = request.files['file']
        if file.filename=='':
            return "NO"
        print(file)
        if file:
            print("Saving " + os.path.join(path_to_upload, file.filename))
            file.save(os.path.join(path_to_upload, file.filename))
        return "SI"

if __name__ == "__main__":
    app.run(host='0.0.0.0')