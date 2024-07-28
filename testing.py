import googlemaps
from config import API_KEY

gmaps = googlemaps.Client(key=API_KEY)

start = "815 Whitlock Avenue"
end = "712 Casarin Crescent"
mode = "walking"
result = gmaps.distance_matrix(start, end, mode)

print(result)

distance_text = result['rows'][0]['elements'][0]['distance']['text']
time_taken = result['rows'][0]['elements'][0]['duration']['text']

print(f'The distance from {start} to {end} by {mode.lower()} is {distance_text}, and the time it takes to get there is {time_taken}.')

distance_km = float(distance_text.split()[0])
emission_factors = {
    'DRIVING': 0.21,  # kg CO2 per km
    'TRANSIT': 0.1,
    'BICYCLING': 0,
    'WALKING': 0
}
emissions = distance_km * emission_factors.get(mode.upper(), 0)
print(f'Emissions: {emissions:.2f} kg CO2')