from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name, s.division, SUM(fact.total_price) " \
                "FROM ecomdb_star_schema.fact_table fact " \
                "JOIN ecomdb_star_schema.item_dim i on i.item_key=fact.item_key " \
                "JOIN ecomdb_star_schema.store_dim s on s.store_key=fact.store_key " \
                "GROUP BY CUBE(i.item_name, s.division) " \
                "ORDER BY i.item_name, s.division "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'division', 'quantity'])
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute()
    print(data)
