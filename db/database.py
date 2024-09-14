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
    saved_places = [something, something, something],
    (maybe) recently_viewed_pages = [something, something, something]
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
    monthly_rent: something,
    utilities: [something, something, something],
    amenities: [something, something, something],
    bus_stop_distance: something, (in minutes driving)
    campus_distance: something, (in minutes driving)
    grocery_store_distance: something, (in minutes driving)
    link_to_img: filepath to that image in filesystem
    parking_pass_needed: bool
}
"""