import mysql
import mysql.connector


class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            user='root', password='root',
                                            database=self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


with DatabaseConnection('ALX_prodev') as cursor:
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
