
from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute1(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query ="SELECT s.store_key, i.item_name, SUM(f.quantity) as quantity_sales_for_each_item " \
                  "FROM ecomdb_star_schema.fact_table f " \
                  "JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
                  "JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                    "GROUP BY CUBE(s.store_key,i.item_name) " \
                    "ORDER BY s.store_key,  SUM(f.quantity) desc"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_ID','item', 'quantity'])
        pd_data = pd_data.dropna()
        pd_data=pd_data.groupby('store_ID').head(3)
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute1()
    print(data)
