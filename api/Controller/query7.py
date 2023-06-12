from DBConnection.dbconfig import PostgresCon
import pandas as pd

class Query7(object):
    def __init__(self, days):
        self.days = days
        self.connection = PostgresCon().getConnection()

    def execute(self):
        connection = PostgresCon().getConnection()
        cursor = connection.cursor()
        query = "SELECT DISTINCT(it.item_name) " \
                "FROM star_schema.fact_table ft, star_schema.item_dim it, star_schema.time_dim tt, star_schema.trans_dim tr " \
                "WHERE ft.item_key = it.item_key AND ft.time_key = tt.time_key AND tr.payment_key = ft.payment_key AND " \
                " %s >= (CURRENT_DATE::DATE - TO_DATE(tt.date, 'DD-MM-YYYY HH24:MI')::DATE) AND (tr.trans_type = 'Mobile' OR tr.trans_type = 'cash') " \
                "ORDER BY it.item_name " 
        cursor.execute(query, [self.days])
        result = cursor.fetchall()
        df = pd.DataFrame(list(result), columns=['Item Name'])
        cursor.close()
        return df.to_dict(orient='records')