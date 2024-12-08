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

# Decorator to manage database transactions (commit or rollback)
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            # Start the transaction (implicitly happens when you execute queries)
            result = func(conn, *args, **kwargs)
            # Commit the transaction if no error occurred
            conn.commit()
            return result
        except Exception as e:
            # Rollback the transaction if an error occurred
            conn.rollback()
            print(f"Error: {e}. Transaction rolled back.")
            raise  # Reraise the exception after rollback
    
    return wrapper

# Example usage of both decorators

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """
    Update the user's email in the database.
    """
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    return f"User {user_id} email updated to {new_email}"

# Update user's email with automatic transaction handling
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
