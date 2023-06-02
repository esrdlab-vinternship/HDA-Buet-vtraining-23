from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.division, t.year,SUM(f.total_price) AS total_sales " \
    "FROM star_schema.fact_table f " \
    "JOIN star_schema.store_dim s ON f.store_key = s.store_key " \
    "JOIN star_schema.time_dim t ON f.time_key = t.time_key " \
    "WHERE s.division = 'BARISAL' AND t.year = 2015 " \
    "GROUP BY CUBE(s.division, t.year) " \
    "ORDER BY s.division, t.year "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')
    

if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
    