from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT u.division, s.year, SUM(t.total_price) " \
              "FROM ecomdb_star_schema.fact_table t " \
              "JOIN ecomdb_star_schema.time_dim s on s.time_key=t.time_key " \
            "JOIN ecomdb_star_schema.store_dim u on u.store_key=t.store_key " \
                "WHERE s.year=2015 AND u.division='BARISAL' " \
                "GROUP BY s.year, u.division "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
