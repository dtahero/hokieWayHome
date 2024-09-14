
class Listing:
    allListings = []
    
    def __init__(self, name: str, address: list, website_link: str, office_hours: list, 
                 bath: int, bed: int, price: float, utilities: list, ammenities: str,
                 bus_stop_distance: int, campus_distance: int, grocery_store_distance: int,
                 link_to_img: str, parking_pass_needed: bool):
        self.name = name
        self.address = address
        self.website_link = website_link
        self.office_hours = office_hours
        self.bath = bath
        self.bed = bed
        self.price = price
        self.utilities = utilities
        self.ammenities = ammenities
        self.bus_stop_distance = bus_stop_distance,
        self.campus_distance = campus_distance,
        self.grocery_store_distance = grocery_store_distance,
        self.link_to_img = link_to_img,
        self.parking_pass_needed = parking_pass_needed
        
        #array for all listingss
        Listing.allListings.append(self)
    
def add_listing(mongo, name: str, address: list, website_link, office_hours: dict, 
                bed: float, bath: float, monthly_rent: int, utilities: list, amenities: list, 
                bus_stop_distance: int, campus_distance: int, grocery_store_distance: int, 
                link_to_image: str, parking_pass_needed: bool):
    data = {
        "name": name,
        "address": {
            address[0],
            address[1],
            address[2]
        },
        "website_link": website_link,
        "office_hours": {
            "Saturday": office_hours["sat"],
            "Sunday": office_hours["sun"],
            "Monday": office_hours["mon"],
            "Tuesday": office_hours["tue"],
            "Wednesday": office_hours["wed"],
            "Thursday": office_hours["thu"],
            "Friday": office_hours["fri"]
        },
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