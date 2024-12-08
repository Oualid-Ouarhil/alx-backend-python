import time
import sqlite3
import functools

# Decorator to automatically open and close the database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open the database connection
        conn = sqlite3.connect('users.db')  
        try:
            # Call the decorated function with the connection
            return func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed after the function executes
            conn.close()
    
    return wrapper

# Decorator to retry the function in case of failure
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    # Try executing the function
                    return func(*args, **kwargs)
                except Exception as e:
                    # If an error occurs, print it and wait before retrying
                    attempt += 1
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            # If all attempts fail, raise the exception
            print(f"Failed after {retries} attempts.")
            raise e  # Raise the last exception encountered
        return wrapper
    return decorator

# Example usage of both decorators

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetch all users from the database with retry on failure.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Fetch users with automatic retry on failure
try:
    users = fetch_users_with_retry()
    print(users)
except Exception as e:
    print(f"Failed to fetch users: {e}")
