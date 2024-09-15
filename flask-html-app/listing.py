#This is a helper function for saving space in the main file for loading listing data


def add_listing(mongo, name: str, address: list, website: str, 
                bed: float, bath: float, monthly_rent: int, utilities: list, amenities: list, 
                bus_stop_distance: int, campus_distance: int, grocery_store_distance: int, 
                link_to_image: str, parking_pass_needed: str):
    
    data = {
        "name": name,
        "address": [
            address[0],
            address[1],
        ],
        "website": website,
        "bed": bed,
        "bath": bath,
        "monthly_rent": monthly_rent,
        "utilities": utilities,
        "amenities": amenities,
        "bus_stop_distance": bus_stop_distance,
        "campus_distance": campus_distance,
        "grocery_store_distance": grocery_store_distance,
        "link_to_img": link_to_image,
        "parking_pass_needed": parking_pass_needed
    }

    mongo.db.location_data.insert_one(data)


def add_listing_data(mongo):
    add_listing(mongo, "Foxridge", ["750 Hethwood Blvd, NW, #100G", "Blacksburg, VA 24060"], "https://www.foxridgeliving.com/", 
                2, 3, 600.0, ["Water, Electricity, Internet"], ["Pool", "Gym", "Common Area"], 12, 15, 2, 
                "not a real filepath", "No")

    add_listing(mongo, "Hunters Ridge", ["1310 Henry Lane", "Blacksburg, VA 24060"], "https://huntersridgeblacksburg.com/", 
                2, 3, 700.0, ["Water, Electricity"], ["Gym", "Outdoor Common Area"], 12, 15, 2, 
                "not a real filepath", "Yes")

    add_listing(mongo, "The Hub", ["1201 Snyder Lane", "Blacksburg, VA 24060"], "https://huboncampus.com/blacksburg/", 
                2, 3, 900.0, ["Electricity"], ["Pool", "Gym", ], 12, 15, 2, 
                "not a real filepath", "Yes")
    
    add_listing(mongo, "The Hub", ["1201 Snyder Lane", "Blacksburg, VA 24060"], "https://huboncampus.com/blacksburg/", 
                2, 3, 900.0, ["Electricity"], ["Pool", "Gym", ], 12, 15, 2, 
                "not a real filepath", "Yes")