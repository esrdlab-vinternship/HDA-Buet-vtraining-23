from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT SUM(t.total_price) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.store_dim st on st.store_key=t.store_key " \
              "JOIN ecombd_star_schema.time_dim td on td.time_key=t.time_key " \
              "WHERE st.division = 'BARISAL' and td.year = 2015  "\
              "GROUP BY (st.division,td.year) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['total_sales'])
        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    #print(data)
