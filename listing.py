class Listing:
    allListings = []
    
    def __init__(self, address: str, location: str, price: float, bath: int, bed: int, water: bool, electricity: bool, ammenities: str):
        self.address = address
        self.location = location
        self.price = price
        self.bath = bath
        self.bed = bed
        self.water = water
        self.electricity = electricity
        self.ammenities = ammenities
        
        #array for all listingss
        Listing.allListings.append(self)
    

