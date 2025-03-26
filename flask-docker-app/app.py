from flask import Flask  # Import Flask framework

app = Flask(__name__)  # Create a Flask app instance

@app.route('/')  # Define a route for the home page
def home():
    return "Hello, Docker! This is a Flask App."  # Display this message when accessed

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000
