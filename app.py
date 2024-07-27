from flask import Flask, render_template, request, jsonify
import requests
import os
from config import GOOGLE_MAPS_API_KEY

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/calculate', methods=['POST'])
def calculate():
    start = request.form['start']
    end = request.form['end']
    mode = request.form['mode']

    # Google Maps Distance Matrix API endpoint
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={start}&destinations={end}&mode={mode}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        distance = data['rows'][0]['elements'][0]['distance']['value'] / 1000  # in km
        duration = data['rows'][0]['elements'][0]['duration']['text']

        # Calculate carbon footprint
        emission_factors = {
            'driving': 0.21,  # kg CO2 per km
            'transit': 0.1,
            'bicycling': 0,
            'walking': 0
        }
        emissions = distance * emission_factors.get(mode, 0)

        return jsonify({'distance': distance, 'duration': duration, 'emissions': emissions})
    else:
        return jsonify({'error': 'Error fetching data from Google Maps API'}), 500
