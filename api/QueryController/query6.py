from numpy.ma import count

from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key as store_key, i.item_name as item_name, sum(f.quantity) as quantity " \
                "FROM star_schema.fact_table f " \
                "JOIN star_schema.store_dim s ON s.store_key = f.store_key "\
                "JOIN star_schema.item_dim i ON i.item_key = f.item_key "\
                "GROUP BY CUBE (s.store_key, i.item_name)" \
                "ORDER BY s.store_key, quantity "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store', 'item', 'quantity'])
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')
        # return pd_data['store', 'item'].tolist()


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)
