from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''
        SELECT s.division, i.item_name, sum(f.total_price)
        FROM star_schema.fact_table f
        JOIN star_schema.item_dim i ON i.item_key = f.item_key
        JOIN star_schema.store_dim s ON s.store_key = f.store_key
        GROUP BY CUBE(i.item_name, s.division)
        ORDER BY i.item_name, s.division
        '''

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'item_name', 'total_price'])
        pd_data['total_price'] = pd_data['total_price'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')
    
    if __name__ == '__main__':
        query9 = Query9()
        data = query9.execute()
        print(data)