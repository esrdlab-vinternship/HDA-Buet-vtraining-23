from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s2.division,s1.year, SUM(t.total_price) " \
              "FROM star_schema.fact_table t " \
              "JOIN star_schema.time_dim s1 on s1.time_key=t.time_key " \
                "JOIN star_schema.store_dim s2 on s2.store_key=t.store_key " \
                "WHERE s1.year=2015 and s2.division='BARISAL'"\
                "GROUP BY CUBE(s2.division,s1.year) " \
                "ORDER BY (s2.division,s1.year)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division','year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)