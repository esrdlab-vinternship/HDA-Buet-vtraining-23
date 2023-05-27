from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query1_2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.district, SUM(f.total_price) " \
                "FROM star_schema.fact_table f " \
                "JOIN star_schema.store_dim s on s.store_key=f.store_key " \
                "GROUP BY CUBE(s.district) " \
                "ORDER BY s.district  " 
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['district', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    query1_2 = Query1_2()
    data = query1_2.execute()
    print(data)
