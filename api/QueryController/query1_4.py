from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query1_4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT t.month, SUM(f.total_price) " \
                "FROM star_schema.fact_table f " \
                "JOIN star_schema.time_dim t on t.time_key=f.time_key " \
                "GROUP BY CUBE(t.month) " \
                "ORDER BY t.month " 
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['month', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    query1_4 = Query1_4()
    data = query1_4.execute()
    print(data)
