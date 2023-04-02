# Import required modules
from flask import Flask, render_template
import sqlite3

# Create a Flask application instance
app = Flask(__name__)

# Define function to get drone data from the database


def get_drones():
    # Create a connection to the database
    connection = sqlite3.connect('drones.db')
    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Execute a SELECT command to retrieve all rows from the "Drone" table
    cursor.execute("SELECT * FROM Drone")
    # Fetch all rows and store them in a variable
    drones = cursor.fetchall()

    # Close the connection and return the retrieved drone data
    connection.close()
    return drones

# Define a route for the application's homepage


@app.route('/')
def index():
    # Call the get_drones() function to retrieve drone data from the database
    drones = get_drones()
    # Render the HTML template named "index.html" and pass the retrieved drone data as a variable
    return render_template('index.html', drones=drones)


# If this script is run directly, start the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
