from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query10(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT CONCAT(st.district, '-', st.upazilla), tt.month, avg(ft.total_price) " \
                "FROM star_schema.fact_table ft, star_schema.time_dim tt, star_schema.store_dim st " \
                "WHERE ft.store_key = st.store_key AND ft.time_key = tt.time_key " \
                "GROUP BY st.store_key, tt.month ORDER BY st.district ASC, st.upazilla ASC, tt.month ASC"
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['store', 'month', 'avg'])
        cursor.close()
        return df.to_dict(orient='records')