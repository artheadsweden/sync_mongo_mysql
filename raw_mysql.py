import mysql.connector


class RawSql:
    def __init__(self, user, password, host, port, database):
        self.mysql_connection = mysql.connector.connect(
            user=user, 
            password=password, 
            host=host, 
            port=port, 
            database=database
        )
        self.cursor = self.mysql_connection.cursor()

    def store_dict(self, table: str, data: dict):
        fields = ', '.join([k for k in data])
        values = ', '.join([str(v) if not isinstance(v, str) else f"'{v}'" for v in data.values()])
        sql = f"INSERT INTO {table} ({fields}) VALUES ({values})"
        self.cursor.execute(sql)
        self.mysql_connection.commit()

    def get_all(self, table):
        self.cursor.execute(f"SELECT * FROM {table}")
        return [dict(zip(self.cursor.column_names, row)) for row in self.cursor]