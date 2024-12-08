import sqlite3
import functools

# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log the SQL query before executing the function
        if 'query' in kwargs:
            print(f"Executing SQL query: {kwargs['query']}")
        elif len(args) > 0:
            print(f"Executing SQL query: {args[0]}")
        
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
