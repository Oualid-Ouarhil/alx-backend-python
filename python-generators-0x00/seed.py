import mysql.connector
import csv
import uuid

# Connects to the MySQL database server
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_mysql_username",  # Replace with your MySQL username
            password="your_mysql_password"  # Replace with your MySQL password
        )
        print("Connection to MySQL server successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Creates the database ALX_prodev if it does not exist
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev created or already exists")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Connects to the ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="ALX_prodev"
        )
        print("Connection to ALX_prodev database successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Creates the table user_data if it does not exist
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3) NOT NULL,
                INDEX (user_id)
            )
        """)
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

# Inserts data into the user_data table from a CSV file
def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check if data already exists
                cursor.execute("SELECT * FROM user_data WHERE email = %s", (row['email'],))
                if cursor.fetchone() is None:
                    cursor.execute("""
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s)
                    """, (str(uuid.uuid4()), row['name'], row['email'], row['age']))
        connection.commit()
        print("Data inserted into user_data table successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found")
    finally:
        cursor.close()
