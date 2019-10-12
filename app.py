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
    
    name_and_surnames = request.args.get('name')
    # get name
    print(name_and_surnames)
    name_and_surnames = name_and_surnames.split(" ")

    name = name_and_surnames[0]
    if len(name_and_surnames) == 4:
        name += " " + name_and_surnames[1]
        surname1 = name_and_surnames[2]
        surname2 = name_and_surnames[3]
    else:
        surname1 = name_and_surnames[1]
        surname2 = name_and_surnames[2]
    
    '''if len(names_and_surnames) >= 1:
        name = names_and_surnames[0]

    if len(names_and_surnames) == 4:
        name = " " + name_and_surnames[1]
        surname1 = names_and_surnames[2]
        surname2 = names_and_surnames[3]
    elif len(name_and_surnames) == 3:
        surname1 = names_and_surnames[1]
        surname2 = names_and_surnames[2]
    elif len(name_and_surnames) == 2:
        surname1 = names_and_surnames[1]'''

    # return json with data
    query = "SELECT * FROM informations WHERE name=%s AND surname1=%s AND surname2=%s"

    cursor.execute(query, (name, surname1, surname2))

    #query =  "SELECT * FROM informations"
    #cursor.execute(query)

    for (name, surname1, surname2, dni, pdfid, extrainfo) in cursor:
        print((name, surname1, surname2, dni, pdfid))

        result_json["data"].append({
            "name":name,
            "surname1":surname1,
            "surname2":surname2,
            "dni": dni
        })

    return jsonify(result_json)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    cursor.close()
    cnx.close()