from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT t.year, SUM(f.total_price) " \
                "FROM star_schema.fact_table f " \
                "JOIN star_schema.time_dim t on t.time_key=f.time_key " \
                "WHERE t.year = 2015 " \
                "GROUP BY CUBE(t.year) " \
                "ORDER BY t.year "
        
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')
    
if __name__ == '__main__':
    query4 = Query4()
    data = query4.execute()
    print(data)
    