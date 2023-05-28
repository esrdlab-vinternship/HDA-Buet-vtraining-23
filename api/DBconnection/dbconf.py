import psycopg2


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecombd",
                                           user="postgres",
                                           password="1234",
                                           host="127.0.0.1",
                                           port="5432")

    def getConnection(self):
        print("successfully connected to database")
        return self.connection
