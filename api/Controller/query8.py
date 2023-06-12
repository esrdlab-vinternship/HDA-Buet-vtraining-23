from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query8(object):
    def __init__(self):
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT it.item_name, tt.quarter " \
                "FROM star_schema.fact_table ft, star_schema.item_dim it, star_schema.time_dim tt " \
                "WHERE ft.time_key = tt.time_key AND ft.item_key = it.item_key " \
                "GROUP BY it.item_name, tt.quarter ORDER BY it.item_name ASC, sum(ft.quantity) ASC"
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=['item name', 'quarter'])
        cursor.close()
        return df.to_dict(orient='records')