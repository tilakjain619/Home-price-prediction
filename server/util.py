import json, pickle, numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    xx = np.zeros(len(__data_columns))

    xx[0] = sqft
    xx[1] = bath
    xx[2] = bhk
    if loc_index >= 0:
        xx[loc_index] = 1

    return round(__model.predict([xx])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading artifacts...")
    global __data_columns
    global __locations
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)
    
    print("Done with Loading Artifacts!")

if __name__ == '__main__':
    load_saved_artifacts()
    get_location_names()
    print(get_estimated_price('Ejipura', 1000, 2, 2))