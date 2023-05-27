from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query1_3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT t.year, SUM(f.total_price) " \
                "FROM star_schema.fact_table f " \
                "JOIN star_schema.time_dim t on t.time_key=f.time_key " \
                "GROUP BY CUBE(t.year) " \
                "ORDER BY t.year"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['year', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    query1_3 = Query1_3()
    data = query1_3.execute()
    print(data)
