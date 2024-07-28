from flask import Flask, render_template, request, jsonify
import requests
import os
import googlemaps
from config import API_KEY

app = Flask(__name__)
gmaps = googlemaps.Client(key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    start = data.get('start')
    end = data.get('end')
    mode = data.get('mode')

    try:
        result = gmaps.distance_matrix(start, end, mode)
        distance_text = result['rows'][0]['elements'][0]['distance']['text']
        time_taken = result['rows'][0]['elements'][0]['duration']['text']

        distance_km = float(distance_text.split()[0])
        emission_factors = {
            'driving': 0.21,  # kg CO2 per km
            'transit': 0.1,
            'bicycling': 0,
            'walking': 0
        }
        emissions = distance_km * emission_factors.get(mode, 0)

        return jsonify({
            'distance': distance_text,
            'duration': time_taken,
            'emissions': emissions
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)