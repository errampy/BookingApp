from .models_master_general import *
from .convert_model_obj_to_dict import query_set_obj_to_dict,get_obj_to_dict
# Country CRUD functions
def create_country(code, name):
    try:
        country = Country.objects.create(code=code, name=name)
        return country
    except Exception as e:
        print(f"Error occurred while creating country: {e}")
        return None

def get_country(code):
    try:
        country = Country.objects.get(pk=code)
        return get_obj_to_dict(country)
    except Country.DoesNotExist:
        print(f"Country with code {code} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving country: {e}")
        return None

def update_country(code, name):
    country = get_country(code)
    if country:
        try:
            country.name = name
            country.save()
            return country
        except Exception as e:
            print(f"Error occurred while updating country: {e}")
            return None
    else:
        print(f"Country with code {code} does not exist.")
        return None

def delete_country(code):
    country = get_country(code)
    if country:
        try:
            country.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting country: {e}")
            return False
    else:
        print(f"Country with code {code} does not exist.")
        return False

# CountyOrState CRUD functions
def create_county_or_state(county, code, name):
    try:
        county_or_state = CountyOrState.objects.create(county=county, code=code, name=name)
        return county_or_state
    except Exception as e:
        print(f"Error occurred while creating county/state: {e}")
        return None

def get_county_or_state(code):
    try:
        county_or_state = CountyOrState.objects.get(pk=code)
        return county_or_state
    except CountyOrState.DoesNotExist:
        print(f"County/state with code {code} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving county/state: {e}")
        return None

def update_county_or_state(code, name):
    county_or_state = get_county_or_state(code)
    if county_or_state:
        try:
            county_or_state.name = name
            county_or_state.save()
            return county_or_state
        except Exception as e:
            print(f"Error occurred while updating county/state: {e}")
            return None
    else:
        print(f"County/state with code {code} does not exist.")
        return None

def delete_county_or_state(code):
    county_or_state = get_county_or_state(code)
    if county_or_state:
        try:
            county_or_state.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting county/state: {e}")
            return False
    else:
        print(f"County/state with code {code} does not exist.")
        return False

# City CRUD functions
def create_city(country, county_or_state, code, name):
    try:
        city = City.objects.create(country=country, county_or_state=county_or_state, code=code, name=name)
        return city
    except Exception as e:
        print(f"Error occurred while creating city: {e}")
        return None

def get_city(code):
    try:
        city = City.objects.get(pk=code)
        return city
    except City.DoesNotExist:
        print(f"City with code {code} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving city: {e}")
        return None

def update_city(code, name):
    city = get_city(code)
    if city:
        try:
            city.name = name
            city.save()
            return city
        except Exception as e:
            print(f"Error occurred while updating city: {e}")
            return None
    else:
        print(f"City with code {code} does not exist.")
        return None

def delete_city(code):
    city = get_city(code)
    if city:
        try:
            city.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting city: {e}")
            return False
    else:
        print(f"City with code {code} does not exist.")
        return False
