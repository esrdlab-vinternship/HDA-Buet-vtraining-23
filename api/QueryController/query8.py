from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT t.item_name, t.quarter " \
                "FROM ( " \
                "SELECT i.item_name, t.quarter, ROW_NUMBER() OVER (PARTITION BY i.item_name ORDER BY SUM(f.quantity) ASC) as row_num " \
                "FROM ecomdb_star_schema.fact_table f JOIN ecomdb_star_schema.item_dim i on f.item_key=i.item_key " \
                "JOIN ecomdb_star_schema.time_dim t on f.time_key=t.time_key " \
                "GROUP BY i.item_name, t.quarter " \
                ") AS t " \
                "WHERE row_num=1 "
        cur.execute(query)
        result = cur.fetchall()[0:12]
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'quarter'])
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)
