import sqlite3
import functools
from datetime import datetime

# Decorator to log SQL queries along with the timestamp
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Log the SQL query with timestamp before executing the function
        if 'query' in kwargs:
            print(f"[{timestamp}] Executing SQL query: {kwargs['query']}")
        elif len(args) > 0:
            print(f"[{timestamp}] Executing SQL query: {args[0]}")
        
        # Call the original function
        return func(*args, **kwargs)
    
    return wrapper

@log_queries
def fetch_all_users(query):
    """
    Fetch all users from the database using the provided SQL query.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Example usage:
query = "SELECT * FROM users"
users = fetch_all_users(query=query)
