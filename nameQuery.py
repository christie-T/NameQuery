from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017")  # can leave this line
db = client["names"]  # can replace w/ database name, if neccesary
collection = db["names"]  # can replace w/ collection name, if neccesary

@app.route("/names", methods=["GET"])
def get_names(): # query names and return sorted to http://localhost:5000/names
    
    cursor = collection.find({}, {"_id": 0, "FirstName": 1})
    sorted_names = sorted([doc["FirstName"] for doc in cursor]) # using the built-in py sort

    return jsonify({"names": sorted_names}) # returns sorted names in json format

if __name__ == "__main__":
    app.run(debug=True)
