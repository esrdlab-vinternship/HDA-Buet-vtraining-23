from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query6(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = " SELECT rank_filter.* FROM (SELECT st.store_key, it.item_name, sum(ft.quantity), RANK() OVER (PARTITION BY st.store_key ORDER BY sum(ft.quantity) DESC) " \
                "FROM star_schema.fact_table ft, star_schema.item_dim it, star_schema.store_dim st " \
                "WHERE ft.store_key = st.store_key AND ft.item_key = it.item_key " \
                "GROUP BY st.store_key, it.item_name ORDER BY st.store_key ASC, sum(ft.quantity) DESC) rank_filter WHERE RANK <= 3 "
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['store key', 'item name', 'quantity', 'rank'])
        df = df.drop(['rank'],axis=1)
        cursor.close()
        return df.to_dict(orient='records')