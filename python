from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return "Hello, World!"

# Define another route that returns JSON data
@app.route('/api')
def api():
    data = {"message": "Welcome to the Flask API"}
    return jsonify(data)

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)