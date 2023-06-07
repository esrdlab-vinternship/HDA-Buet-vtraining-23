from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key, t.month, AVG(fact.total_price) " \
                "FROM ecomdb_star_schema.fact_table fact " \
                "JOIN ecomdb_star_schema.store_dim s on s.store_key=fact.store_key " \
                "JOIN ecomdb_star_schema.time_dim t on t.time_key=fact.time_key " \
                "GROUP BY CUBE(s.store_key, t.month) " \
                "ORDER BY s.store_key, t.month "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'month', 'avg_sales'])
        pd_data['avg_sales'] = pd_data['avg_sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)
