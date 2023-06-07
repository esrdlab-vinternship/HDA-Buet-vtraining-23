from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name, t.quarter, SUM(fact.quantity) " \
                "FROM ecomdb_star_schema.fact_table fact " \
                "JOIN ecomdb_star_schema.item_dim i on i.item_key=fact.item_key " \
                "JOIN ecomdb_star_schema.time_dim t on t.time_key=fact.time_key " \
                "GROUP BY CUBE(i.item_name, t.quarter) " \
                "ORDER BY i.item_name, SUM(fact.quantity) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'quarter', 'quantity'])
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('item_name').head(1)
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)
