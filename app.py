from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the app in debug mode if the script is called directly
if __name__ == '__main__':
    app.run(debug=True)

