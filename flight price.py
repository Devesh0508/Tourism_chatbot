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
