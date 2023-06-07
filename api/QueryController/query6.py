from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key, it.item_name, SUM(fact.quantity) " \
                "FROM ecomdb_star_schema.fact_table fact " \
                "JOIN ecomdb_star_schema.item_dim it on fact.item_key=it.item_key " \
                "JOIN ecomdb_star_schema.store_dim s on s.store_key=fact.store_key " \
                "GROUP BY CUBE(s.store_key, it.item_name)"  \
                "ORDER BY s.store_key ASC, SUM(fact.quantity) DESC "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'item_name', 'quantity'])
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('store_key').head(3)
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)
