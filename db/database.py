from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["hokie_way_db"]

user_data_collection = db["user_data"]
"""
update recently_viewed_pages to remove last entry and add another
once it reaches a certain length
User data should look like this:
{
    firstName: something,
    lastName: something,
    email: something,
    username: something,
    password: something,
    saved_places = [something, something, something],
    recently_viewed_pages = [something, something, something]
}
"""

location_data_collection = db["location_data"]
"""
Listing data can look like this:
{
    address: {
        address_line_1,
        address_line_2,
        zip_code
    },
    website_link: something,
    office_hours: {
        sat: something
        sun: something
        and so on you get the idea
    },
    bed_and_bath: something (should be in form {bed}/{bath}),
    monthly_rent_price: something,
    utilities: [something, something, something],
    amenities: [something, something, something],
    bus_stop_distance: something,
    campus_distance: something,
    grocery_store_distance,
    link_to_img: need to find image link,
    parking_pass_needed: bool
}
"""

mydict = { "name": "John", "address": "Highway 37" }

x = user_data_collection.insert_one(mydict)

print(client.list_database_names())