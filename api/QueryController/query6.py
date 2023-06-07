from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT t.store_key, t.item_name, t.quantity " \
                "FROM ( " \
                    "SELECT p.store_key, q.item_name, SUM(p.quantity) as quantity, " \
                    "ROW_NUMBER() OVER (PARTITION BY p.store_key ORDER BY SUM(p.quantity) DESC) AS row_num " \
                    "FROM ecomdb_star_schema.fact_table p JOIN ecomdb_star_schema.item_dim q on p.item_key=q.item_key " \
                    "GROUP BY p.store_key, q.item_name " \
                ") AS t " \
                "WHERE t.row_num <= 3"
        cur.execute(query)
        result = cur.fetchall()[0:12]
        pd_data = pd.DataFrame(list(result), columns=['store', 'item', 'units'])
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)
