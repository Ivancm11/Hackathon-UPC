from flask import Flask
from flask import send_from_directory, redirect, request, jsonify
import os
from process import *
import threading
import mysql.connector

app = Flask(__name__, static_folder='static', static_url_path='')
path_to_upload = "/home/victor/Hackathon-UPC/upload" # change in docker
cnx = mysql.connector.connect(host='remotemysql.com',
                            user='3sRxPqRiLy',
                            database='3sRxPqRiLy',
                            password='dhpwyt9ufA',
                            port=3306)
cursor = cnx.cursor()

@app.route("/")
def main():
    return redirect("index.html")

@app.route("/upload", methods=['POST'])
def upload_file():
        if 'file' not in request.files:
            print("Not a file")
            return jsonify({'status':'error'})
        file = request.files['file']
        if file.filename=='':
            print("Not a file")
            return jsonify({'status':'error'})
        if file:
            print("Saving " + os.path.join(path_to_upload, file.filename))
            file.save(os.path.join(path_to_upload, file.filename))
            
            thread = threading.Thread(target=process, args=([os.path.join(path_to_upload, file.filename)]))
            thread.start()

        return  jsonify({'status':'success'})

@app.route("/search", methods=['GET'])
def search():
    
    result_json = {"data" : []}
    
    name = request.args.get('name')
    
    if len(name) == 0:
        return jsonify(result_json)

    print(name)
   
    # return json with data
    query = "SELECT * FROM foods WHERE name LIKE '%{}%'".format(name)
    cursor.execute(query)
    
    for (name, type_, energy, grasas, sugar, h2o, co2) in cursor:
        print((name, type_, energy, grasas, sugar, h2o, co2))

        result_json["data"].append({
            "name":name,
            "type":type_,
            "energy":energy,
            "grasas": grasas,
            "sugar":sugar,
            "H2O":h2o,
            "CO2":co2,
        })

    return jsonify(result_json)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    cursor.close()
    cnx.close()