from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

import listing 

app = Flask(__name__, static_folder='flask-html-app\static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/hokie_way_db"
mongo = PyMongo(app)

mongo.db.location_data.drop()

listing.add_listing_data(mongo)

@app.route('/')
def home():
    listings = list(mongo.db.location_data.find())
    return render_template('index.html', listings=listings)  # Render the index.html file

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')  

@app.route('/<listing_name>', methods=['GET'])
def listingdisplay(listing_name):
    listing = mongo.db.location_data.find_one({"name": listing_name})
    if listing:
        return render_template('listingdisplay.html', listing=listing)
    else:
        return render_template('404.html'), 404


"""
Code to create a new user in our database. Java input looks like:
{
    "firstName": xxxx,
    "lastName": xxxx,
    "email": xxxx,
}
"""
@app.route('/create_new_user', methods=['POST'])
def create_new_user():
    data = request.json
    result = mongo.db.user_data.insert_one({
        "firstName": data.get('firstName'),
        "lastName": data.get('lastName'),
        "email": data.get('email'),
        "saved_places": []
    })
    
    return jsonify({"message": "User data added", "id": str(result.inserted_id)}), 201


"""
Adds a saved place to a user's saved places. Java dict input should be
in form of:
{
    "email": the user's email,
    "new_place": the name of the new place to add
}
"""
@app.route('/add_user_saved_place', methods=['POST'])
def add_user_saved_place():
    data = request.json
    query = {"email": data.get("email")}
    newvalue = {"$push": {"saved_places": data.get("new_place")}}
    result = mongo.db.user_data.update_one(query, newvalue)
    
    if result.matched_count == 0: #if no users were found with that email
        return jsonify({"message": "User not found in database"}), 404
    
    if result.modified_count > 0: #something was modified
        return jsonify({"message": "Place saved"}), 200
    else: #nothing was modified
        return jsonify({"message": "No change made to saved places."}), 500


"""
Returns the list of saved places for a users email
"""
@app.route('/get_user_saved_places', methods=['GET'])
def get_user_saved_places():
    data = request.json
    query = {"email": data.get("email")}
    
    user_data = mongo.db.user_data.find(query)
    
    if user_data:
        saved_places = user_data.get("saved_places", [])
        return jsonify(saved_places), 200
    else:
        return jsonify({"message": "No saved places found"}), 404

app.static_folder = 'static'
      
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
