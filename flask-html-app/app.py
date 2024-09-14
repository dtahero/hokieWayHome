from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
import listing


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/hokie_way_db"
mongo = PyMongo(app)

#this is here for now
office_hours = {
    "sat": "8",
    "sun": "8",
    "mon": "8",
    "tue": "8",
    "wed": "8",
    "thu": "8",
    "fri": "8"
}

listing.add_listing(mongo, "Foxridge", "1111 place dr", "wwww.place.com", office_hours, 
            2, 3, 700.0, ["gas, electricity"], ["pool"], 12, 15, 2, 
            "not a real filepath", True)

print(mongo.db.list_collection_names())

@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html file

@app.route('/signin')
def signin():
    return render_template('signin.html')  # Render the signin.html file

@app.route('/signup')
def signup():
    return render_template('signup.html')  

@app.route('/forgotpass')
def forgotpass():
    return render_template('forgotpass.html')  

@app.route('/loginmenu')
def loginmenu():
    return render_template('loginmenu.html')  

@app.route('/listingdisplay')
def listingdisplay():
    return render_template('listingdisplay.html')  



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
