import os

API_KEY = os.environ.get('API_KEY', 'AIzaSyCdKPXkBgtiIVoYuRAl9GUkkVWry8a_4gA')
if API_KEY is None:
    raise ValueError("No API_KEY set for environment")