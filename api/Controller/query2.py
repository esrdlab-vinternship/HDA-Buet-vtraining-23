from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query2(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT  ct.name, sum(ft.total_price) " \
                "FROM star_schema.fact_table ft, star_schema.customer_dim ct " \
                "WHERE ft.customer_key = ct.customer_key " \
                "GROUP BY CUBE(ct.name) ORDER BY ct.name "
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['Customer Name', 'Total price'])
        df = df.dropna()
        cursor.close()
        return df.to_dict(orient='records')