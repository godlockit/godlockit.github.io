import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        if not self.connection:
            self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.execute_query(query)

    def insert_data(self, table_name, data):
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        placeholders = ', '.join('?' * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, values)

    def select_data(self, table_name, columns=None, condition=None):
        if not columns:
            columns = '*'
        query = f"SELECT {columns} FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        return self.execute_query(query)

