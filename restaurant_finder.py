# This code will generate a list of restaurants, their price points, their locations as well as their contact information within a radius of Schneider Electric Osaka.
# Doing this will accelerate the process of doing the market segmentation and sending out preliminary surveys to the prospective restaurants for the primary market research.

import googlemaps
import time
import json

#API KEY that was gotten from enabling google account
apikey = #Generate an API key by creating a billing account for the places API using the following link: https://developers.google.com/places/web-service/intro

gmaps = googlemaps.Client(key = apikey) #Connects to the google maps places API using the defined API key

#Need to get the user defined location, and radius criteria for the restaurant search
print("Please enter the longitude and lattitude of the central point of this search in the following format: 'longitude,lattitude':")
location = input()
print("Please enter the search radius in meters:")
radius = input()

       
#define the search for restaurants in Osaka (within 0.5km of Schneider Electric's office)
places_output = gmaps.places_nearby(location, radius, open_now = "False",type = 'restaurant')
#location = "34.6914,135.4991"

#Since output contains a lot of irrelevant information, filter the output down to what matters for the market segmentation

data = {} #make the empty shell for json file
data['restaurant'] = [] #makes the empty sections for the restaurant data

for place in places_output['results']:
    my_place_id = place['place_id']

    #Market segmented by: type of resto, price point, location and size (not easy to get from this method)
    my_fields = ['name', 'formatted_phone_number', 'formatted_address', 'type', 'price_level']
    
    #Generate new details for the place
    place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

    #print this information to ensure that it is accurate
    print(place_details)

    #append the necessary information to the JSON file
    data['restaurant'].append({
        'name': my_fields[0],
        'phone':my_fields[1],
        'address':my_fields[2],
        'type':my_fields[3],
        'price point':my_fields[4]
    })

#Create the JSON file with all of the information
with open('restaurant_data.json','w') as outfile:
    json.dump(data,outfile)

