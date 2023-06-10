from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        # for each store I will just keep the products in decending oder of the purchase,
        # then with help of python library i will pick top three

        # firstly, sort with store key, if tie then sort with sum of t.quantity

        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.store_key, it.item_name ,SUM(t.quantity) " \
                      "FROM ecomdb_star_schema.fact_table t " \
                      "JOIN ecomdb_star_schema.store_dim s on s.store_key=t.store_key " \
                      "JOIN ecomdb_star_schema.item_dim it on it.item_key=t.item_key " \
                      "GROUP BY CUBE(s.store_key, it.item_name) " \
                      "ORDER BY s.store_key, SUM(t.quantity) desc"
        cur.execute(select_stmt)


        result = cur.fetchall()



        pd_data = pd.DataFrame(list(result), columns=['store_id', 'item_name', 'quantity'])
        pd_data['quantity'] = pd_data['quantity'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('store_id').head(3)
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)
