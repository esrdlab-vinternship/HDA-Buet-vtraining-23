from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.store_key , tim.month, AVG(t.total_price) " \
                      "FROM ecomdb_star_schema.fact_table t " \
                      "JOIN ecomdb_star_schema.time_dim tim on tim.time_key=t.time_key " \
                      "JOIN ecomdb_star_schema.store_dim s on s.store_key=t.store_key " \
                      "GROUP BY CUBE(s.store_key, tim.month) " \
                      "ORDER BY s.store_key, tim.month "
        cur.execute(select_stmt)


        result = cur.fetchall()

        pd_data = pd.DataFrame(list(result), columns=['store_key', 'month', 'total_avg_price'])
        pd_data['total_avg_price'] = pd_data['total_avg_price'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)
