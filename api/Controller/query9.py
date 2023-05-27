from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query9(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT it.item_name, st.division, sum(ft.total_price) " \
                "FROM star_schema.fact_table ft, star_schema.item_dim it, star_schema.store_dim st " \
                "WHERE ft.store_key = st.store_key AND ft.item_key = it.item_key " \
                "GROUP BY it.item_name, st.division ORDER BY it.item_name ASC, st.division ASC"
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['item name', 'division', 'total price'])
        cursor.close()
        return df.to_dict(orient='records')