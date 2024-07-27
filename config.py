import os

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
if GOOGLE_MAPS_API_KEY is None:
    raise ValueError("No GOOGLE_MAPS_API_KEY set for environment")