import mysql.connector

def stream_user_ages():
    """
    A generator that fetches user ages from the user_data table one by one.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="",  
            password="",  
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")

        # Yield each user's age one by one
        for row in cursor:
            yield row['age']

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.
    """
    total_age = 0
    count = 0

    # Use the generator to stream user ages
    for age in stream_user_ages():
        total_age += age
        count += 1

    # Calculate the average if there are any users
    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found.")


if __name__ == "__main__":
    # Run the calculation
    calculate_average_age()
