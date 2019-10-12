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

def computeCo2(calories, carbohydrates, protein, fat, saturatedFats, salt, co2):
    return 0.0

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
    query = "SELECT * FROM foods2 WHERE name LIKE '%{}%'".format(name)
    cursor.execute(query)
    
    for (name, calories, carbohydrates, protein, fat, saturatedFats, salt, co2) in cursor:

        result_json["data"].append({
            "name":name,
            "calories":calories,
            "carbohydrates":carbohydrates,
            "protein": protein,
            "fat":fat,
            "saturatedFats":saturatedFats,
            "salt":salt,
            "co2":co2,
        })

    return jsonify(result_json)


@app.route("/computeCo2", methods=['GET'])
def compute_co2():
    result_json = {}
    
    calories = request.args.get('name')
    carbohydrates = request.args.get('carbohydrates')
    protein = request.args.get('protein')
    fat = request.args.get('fat')
    saturatedFats = request.args.get('saturatedFats')
    salt = request.args.get('salt')
    co2 = request.args.get('co2')

    result_json = {'result':computeCo2(calories, carbohydrates, protein, fat, saturatedFats, salt, co2)}

    return jsonify(result_json)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    cursor.close()
    cnx.close()