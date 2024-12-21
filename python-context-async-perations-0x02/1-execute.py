import mysql.connector

class ExecuteQuery:
    def __init__(self, db_name ,query, param):
        self.db_name = db_name
        self.query = query
        self.param = param
    def __enter__(self):
        self.conn = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='root',
                                            database=self.db_name)
        self.currsor = self.conn.cursor()
        return self
    def execute(self):
        self.currsor.execute(self.query, self.param)
        rows = self.currsor.fetchall()
        return rows
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.currsor.close()
        self.currsor.close()

query = 'SELECT * FROM users WHERE age > %s'
params = (25,)
with ExecuteQuery('ALX_prodev', query, params) as curr:
    rows = curr.execute()
    print(rows)

        