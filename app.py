#getting the access token from Amadeus:
import requests

def get_amadeus_access_token(api_key, api_secret):
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': api_secret
    }
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        return token
    else:
        return {"error": "Failed to get access token"}

# Example Usage
api_key = 'b5zfxuxACANHN3uYArjCGAXyUUDxoxAq'
api_secret = 'Db8DR680hygmn1FC'
token = get_amadeus_access_token(api_key, api_secret)
print(f"Access Token: {token}")

#fetching flight prices from Amadeus:

def get_flight_prices(token, origin, destination, departure_date):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'originLocationCode': origin,
        'destinationLocationCode': destination,
        'departureDate': departure_date,
        'adults': '1'
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch flight prices"}

# Example Usage
flights = get_flight_prices(token, 'JFK', 'LHR', '2024-09-20')
print(flights)

#hotel recommendations

def get_hotel_recommendations(token, city, check_in, check_out):
    url = "https://test.api.amadeus.com/v2/shopping/hotel-offers"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'cityCode': city,
        'checkInDate': check_in,
        'checkOutDate': check_out,
        'roomQuantity': '1',
        'adults': '1'
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch hotel recommendations"}

# Example Usage
hotels = get_hotel_recommendations(token, 'NYC', '2024-09-20', '2024-09-25')
print(hotels)

#Combine Flight and Hotel Data

def combine_results(flights, hotels):
    combined_data = {
        'flights': flights,
        'hotels': hotels
    }
    return combined_data

# Example usage of combining both responses
combined = combine_results(flights, hotels)
print(combined)

#Formatting Flight Data:

def format_flight_data(flights):
    formatted_flights = []
    
    for offer in flights.get('data', []):
        flight_info = {
            'origin': offer['itineraries'][0]['segments'][0]['departure']['iataCode'],
            'destination': offer['itineraries'][0]['segments'][-1]['arrival']['iataCode'],
            'departure_time': offer['itineraries'][0]['segments'][0]['departure']['at'],
            'arrival_time': offer['itineraries'][0]['segments'][-1]['arrival']['at'],
            'price': offer['price']['total'],
            'airline': offer['itineraries'][0]['segments'][0]['carrierCode']
        }
        formatted_flights.append(flight_info)
    
    return formatted_flights

# Example Usage
formatted_flights = format_flight_data(flights)
print(formatted_flights)

#Formatting Hotel Data

def format_hotel_data(hotels):
    formatted_hotels = []
    
    for hotel in hotels.get('data', []):
        hotel_info = {
            'name': hotel['hotel']['name'],
            'rating': hotel['hotel']['rating'],
            'price': hotel['offers'][0]['price']['total'],
            'check_in': hotel['offers'][0]['checkInDate'],
            'check_out': hotel['offers'][0]['checkOutDate'],
            'address': hotel['hotel']['address']['lines'][0],
        }
        formatted_hotels.append(hotel_info)
    
    return formatted_hotels

# Example Usage
formatted_hotels = format_hotel_data(hotels)
print(formatted_hotels)

# Combining and Presenting Data:

def present_combined_results(formatted_flights, formatted_hotels):
    # Display flights first
    print("Available Flights:")
    for flight in formatted_flights:
        print(f"From {flight['origin']} to {flight['destination']} - Price: {flight['price']} USD")
        print(f"Airline: {flight['airline']}, Departure: {flight['departure_time']}, Arrival: {flight['arrival_time']}")
        print("---")
    
    # Display hotels next
    print("\nRecommended Hotels:")
    for hotel in formatted_hotels:
        print(f"Hotel: {hotel['name']}, Rating: {hotel['rating']}, Price: {hotel['price']} USD")
        print(f"Address: {hotel['address']}")
        print(f"Check-in: {hotel['check_in']}, Check-out: {hotel['check_out']}")
        print("---")

# Example usage of presenting the combined data
present_combined_results(formatted_flights, formatted_hotels)
