import locationtagger

def find_location(text: str):
    """
    
    """
    
    # extracting entities.
    place_entity = locationtagger.find_locations(text = text)
    
    # getting all countries
    countries = place_entity.countries
    
    # getting all states
    states = place_entity.regions
    
    # getting all cities
    cities = place_entity.cities


    return countries, states, cities
