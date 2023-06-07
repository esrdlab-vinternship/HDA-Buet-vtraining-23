from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.division, t.year, SUM(fact.total_price) " \
                "FROM ecomdb_star_schema.fact_table fact " \
                "JOIN ecomdb_star_schema.time_dim t on fact.time_key=t.time_key " \
                "JOIN ecomdb_star_schema.store_dim s on s.store_key=fact.store_key " \
                "WHERE t.year = 2015 AND s.division = 'BARISAL' " \
                "GROUP BY CUBE(t.year, s.division)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data.iloc[0:1]
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
