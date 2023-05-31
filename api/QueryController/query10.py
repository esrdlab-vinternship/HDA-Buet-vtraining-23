from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute1(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key, t.month, AVG(f.total_price) " \
                  "FROM ecomdb_star_schema.fact_table f " \
                  "JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
                  "JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key " \
                    "GROUP BY CUBE(s.store_key,t.month) " \
                    "ORDER BY s.store_key, t.month"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_ID','month' ,'average_sales'])
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute1()
    print(data)
