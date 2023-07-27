import sqlite3
from datetime import datetime

class QueryRunner(object):

    def __init__(self, config):
        self.config = config
        self.database_file_name = "%s\\%s.db" % (
            self.config.get("database_directory"),
            self.config.get("database_name")
        )

    def run_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        conn.execute(sql_str)
        conn.commit()

    def fetch_sql(self, sql_str):
        conn = sqlite3.connect(self.database_file_name)
        query = conn.execute(sql_str)
        results = query.fetchall()
        return results

    def create_all_tables(self):
        self.create_coffees_table()

    def create_coffees_table(self):
        sql_str = "CREATE TABLE coffees(date DATE, description VARCHAR, oz FLOAT)"
        try:
            self.run_sql(sql_str)
        except sqlite3.OperationalError:
            pass

    def insert_coffee(self, description, oz, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        sql_str = "INSERT INTO coffees ('date', 'description', 'oz') VALUES ('%s', '%s', '%s')" % (date, description, oz)
        self.run_sql(sql_str)

    def get_coffees(self):
        sql_str = "SELECT * FROM coffees"
        return self.fetch_sql(sql_str)
