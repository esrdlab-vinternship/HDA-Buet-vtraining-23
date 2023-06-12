import psycopg2

class PostgresCon(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="econdb",
                                           user = "postgres",
                                           password = "Justdoit007",
                                           host = "127.0.0.1",
                                           port = "5432")

    def getConnection(self):
        print("Connection to DB established!")
        return self.connection