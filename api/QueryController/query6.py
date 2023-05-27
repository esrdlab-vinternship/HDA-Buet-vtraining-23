from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key as store_key, i.item_name as item_name, sum(ft.quantity) as quantity_sales_per_item " \
"FROM ecomdb_star_schema.fact_table ft " \
"JOIN ecomdb_star_schema.store_dim s ON s.store_key = ft.store_key "\
"JOIN ecomdb_star_schema.item_dim i ON i.item_key = ft.item_key "\
"GROUP BY CUBE (s.store_key, i.item_name)" \
"ORDER BY s.store_key, quantity_sales_per_item "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'item_name', 'quantity'])
        pd_data['quantity'] = pd_data['quantity'].astype('float64')
        pd_data = pd_data.dropna()
        top3 = pd_data.groupby('store_key').head(3)
        # print(pd_data)
        return top3.to_dict(orient='records')


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)
