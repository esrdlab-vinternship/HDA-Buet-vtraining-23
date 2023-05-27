from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query5(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT sum(ft.total_price) " \
                "FROM star_schema.fact_table ft, star_schema.store_dim st, star_schema.time_dim tt " \
                "WHERE ft.store_key = st.store_key AND ft.time_key = tt.time_key AND st.division = 'BARISAL' AND tt.year = 2015 " \
                "GROUP BY st.division,tt.year ORDER BY st.division " 
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['Total price'])
        df = df.dropna()
        cursor.close()
        return df.to_dict(orient='records')