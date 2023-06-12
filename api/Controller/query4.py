from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query4(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT tt.year, sum(ft.total_price) " \
                "FROM star_schema.fact_table ft, star_schema.time_dim tt " \
                "WHERE ft.time_key = tt.time_key AND tt.year = 2015 " \
                "GROUP BY CUBE(tt.year) ORDER BY tt.year "
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['Year', 'Total price'])
        df = df.dropna()
        cursor.close()
        return df.to_dict(orient='records')