
from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute1(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.division, t.year, SUM(f.total_price) " \
                  "FROM ecomdb_star_schema.fact_table f " \
                  "JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
                  "JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key " \
                    "WHERE s.division='BARISAL' and t.year='2015' "\
                    "GROUP BY CUBE(s.division,t.year) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['year','division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        #pd_data['year'] = pd_data['year'].astype('int')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5= Query5()
    data = query5.execute1()
    print(data)
