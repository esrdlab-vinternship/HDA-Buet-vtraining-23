from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.trans_type, SUM(t.total_price) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.trans_dim s on s.payment_key=t.payment_key " \
              "GROUP BY CUBE(s.trans_type) " \
              "ORDER BY s.trans_type"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['trans_type', 'total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        print(pd_data.to_dict(orient='records'))

        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    data = query2.execute()
    #print(data)
