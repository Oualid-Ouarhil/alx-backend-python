import mysql.connector

def paginate_users(page_size, offset):
    """
    Fetch users from the user_data table using pagination with a specific offset and limit.
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
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()
        connection.close()
        return rows

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []


def lazy_paginate(page_size):
    """
    Generator function to lazily load pages of users, each containing 'page_size' rows.
    """
    offset = 0
    while True:
        # Get the current page of users
        users = paginate_users(page_size, offset)
        
        # If no more data, break out of the loop
        if not users:
            break
        
        # Yield the current page of users
        yield users
        
        # Increment the offset by the page size for the next batch
        offset += page_size


if __name__ == "__main__":
    # Example usage of lazy pagination
    for page in lazy_paginate(100):  # Change page_size as needed
        for user in page:
            print(user)
