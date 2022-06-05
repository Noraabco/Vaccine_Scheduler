import pymssql
import os


class ConnectionManager:

    def __init__(self):
        self.server_name = "414hw3server.database.windows.net"
        self.db_name = "CSE414_HW3"
        self.user = "yilinl8@414hw3server.database.windows.net"
        self.password = "qwe123E@1"
        self.conn = None




    def create_connection(self):
        try:
            self.conn = pymssql.connect(server=self.server_name, user=self.user, password=self.password, database=self.db_name)
        except pymssql.Error as db_err:
            print("Database Programming Error in SQL connection processing! ")
            print(db_err)
            quit()
        return self.conn

    def close_connection(self):
        try:
            self.conn.close()
        except pymssql.Error as db_err:
            print("Database Programming Error in SQL connection processing! ")
            print(db_err)
            quit()
