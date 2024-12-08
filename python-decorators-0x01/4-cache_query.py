import time
import sqlite3
import functools

# Cache dictionary to store results of SQL queries
query_cache = {}

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

# Cache query decorator to store query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query, *args, **kwargs):
        # Check if the query result is cached
        if query in query_cache:
            print("Using cached result for query:", query)
            return query_cache[query]
        
        # Call the function to execute the query and cache the result
        result = func(conn, query, *args, **kwargs)
        
        # Store the result in the cache
        query_cache[query] = result
        print("Caching result for query:", query)
        return result
    
    return wrapper

# Fetch users from the database with caching
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
