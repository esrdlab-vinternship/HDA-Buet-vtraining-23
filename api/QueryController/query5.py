from numpy.ma import count

from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.district, t.year, SUM(f.total_price) " \
                "FROM star_schema.fact_table f " \
                "INNER JOIN star_schema.time_dim t on t.time_key=f.time_key " \
                "INNER JOIN star_schema.store_dim s on s.store_key=f.store_key " \
                "WHERE t.year=2015 and s.district='BARISAL' " \
                "GROUP BY CUBE(t.year, s.district) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['district', 'year', 'sales'])
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
