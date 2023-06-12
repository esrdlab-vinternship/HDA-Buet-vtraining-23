from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query3(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT  st.division, sum(ft.total_price) " \
                "FROM star_schema.fact_table ft, star_schema.store_dim st " \
                "WHERE ft.store_key = st.store_key AND st.division = 'BARISAL' " \
                "GROUP BY CUBE(st.division) ORDER BY st.division " 
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['Division', 'Total price'])
        df = df.dropna()
        cursor.close()
        return df.to_dict(orient='records')