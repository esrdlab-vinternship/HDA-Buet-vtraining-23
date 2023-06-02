from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''
            SELECT s.store_key, tim.month, avg(f.total_price)
            FROM star_schema.fact_table f
            JOIN star_schema.store_dim s ON s.store_key = f.store_key
            JOIN star_schema.time_dim tim ON tim.time_key = f.time_key
            GROUP BY CUBE(s.store_key, tim.month)
            ORDER BY s.store_key, tim.month
            '''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'month', 'avg'])
        pd_data['avg'] = pd_data['avg'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')
    
    if __name__ == '__main__':
        query10 = Query10()
        data = query10.execute()
        print(data)