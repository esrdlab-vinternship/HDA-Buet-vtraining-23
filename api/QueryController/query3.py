from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT SUM(t.total_price) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.store_dim s on s.store_key=t.store_key " \
              "WHERE s.division = 'BARISAL' "\
              "GROUP BY (s.division)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query3 = Query3()
    data = query3.execute()
    #print(data)
