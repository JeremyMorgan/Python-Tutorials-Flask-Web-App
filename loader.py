# Import required modules
import sqlite3
import csv


# Define function to create the database and table
def create_database():
    # Create a connection to the database
    connection = sqlite3.connect('drones.db')
    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Execute a CREATE TABLE command to create a "Drone" table with the required columns
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Drone" (
        "Id"    INTEGER,
        "Name"  TEXT,
        "FlightTime"    INTEGER,
        "SensorSize"    TEXT,
        "WeightMetric"  NUMERIC,
        "WeightImperial"        NUMERIC,
        "TopSpeedMetric"        NUMERIC,
        "TopSpeedImperial"      NUMERIC,
        "Cost"  NUMERIC,
        PRIMARY KEY("Id" AUTOINCREMENT)
    );
    """)

    # Commit the changes to the database and close the connection
    connection.commit()
    connection.close()


# Define function to insert drone data into the table
def insert_drone_data(drone_data):
    # Create a connection to the database
    connection = sqlite3.connect('drones.db')
    # Create a cursor object to execute SQL commands
    cursor = connection.cursor()

    # Execute an INSERT INTO command to insert the drone data into the "Drone" table
    cursor.execute("""
    INSERT INTO Drone (Name, FlightTime, SensorSize, WeightMetric, WeightImperial, TopSpeedMetric, TopSpeedImperial, Cost)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, drone_data)

    # Commit the changes to the database and close the connection
    connection.commit()
    connection.close()


# Define function to load data from CSV file into the table
def load_csv_data(file_name):
    # Open the CSV file for reading
    with open(file_name, 'r') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)
        # Skip the header row
        next(csv_reader)

        # Loop through each row in the CSV file
        for row in csv_reader:
            # Convert the row to a tuple
            drone_data = tuple(row)
            # Insert the drone data into the table using the insert_drone_data() function
            insert_drone_data(drone_data)


# If this script is run directly, call the create_database() and load_csv_data() functions
if __name__ == "__main__":
    create_database()
    load_csv_data('drones.csv')
