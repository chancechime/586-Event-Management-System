import pymssql

class Database:
    pass
    def __init__(self):
        try:
            self.connection = pymssql.connect(server='ems.cp084oyu2d47.us-west-1.rds.amazonaws.com', user='admin', password='L33?Af6K}Pxx9e!s%CabSo_w*|$q', database='ems')
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except Exception as e:
            print("Failed to connect to the database: {e}")
    def get_cursor(self):
        return self.cursor
    def get_connection(self):
        return self.connection
    def close_connection(self):
        self.connection.close()
    def commit(self):
        self.connection.commit()
    def rollback(self):
        self.connection.rollback()
    def execute(self, query):
        self.cursor.execute(query)
        self.commit()
    def fetchone(self):
        return self.cursor.fetchone()
    def fetchall(self):
        return self.cursor.fetchall()
    def fetchmany(self, size):
        return self.cursor.fetchmany(size)
    def __del__(self):
        self.close_connection()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()