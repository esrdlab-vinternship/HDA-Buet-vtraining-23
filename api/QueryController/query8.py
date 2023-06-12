from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        # for each store I will just keep the products in decending oder of the purchase,
        # then with help of python library i will pick top three

        # firstly, sort with store key, if tie then sort with sum of t.quantity

        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT tim.quarter, it.item_name ,SUM(t.total_price) " \
                      "FROM ecomdb_star_schema.fact_table t " \
                      "JOIN ecomdb_star_schema.item_dim it on it.item_key=t.item_key " \
                      "JOIN ecomdb_star_schema.time_dim tim on tim.time_key=t.time_key " \
                      "GROUP BY CUBE(it.item_name, tim.quarter) " \
                      "ORDER BY it.item_name, SUM(t.total_price) "
        cur.execute(select_stmt)
        result = cur.fetchall()

        pd_data = pd.DataFrame(list(result), columns=['quarter', 'item_name', 'quantity'])
        pd_data['quantity'] = pd_data['quantity'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('item_name').head(1)
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)
