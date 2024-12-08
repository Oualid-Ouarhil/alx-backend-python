import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows in batches from the user_data table.
    """
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="", 
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)  # Fetch rows as dictionaries
        cursor.execute("SELECT * FROM user_data")

        while True:
            rows = cursor.fetchmany(batch_size)
            if not rows:
                break
            yield rows

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def batch_processing(batch_size):
    """
    Process each batch to filter users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        processed_batch = [user for user in batch if user['age'] > 25]
        for user in processed_batch:
            print(user)
