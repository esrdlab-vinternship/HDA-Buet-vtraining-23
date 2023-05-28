from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT SUM(t.total_price) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.time_dim s on s.time_key=t.time_key " \
              "WHERE s.year = 2015 "\
              "GROUP BY (s.year)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query4 = Query4()
    data = query4.execute()
    #print(data)
