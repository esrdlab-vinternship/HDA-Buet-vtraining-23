from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")
    
    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name, tim.quarter, SUM(f.total_price) as total_price " \
                "FROM star_schema.fact_table as f " \
                "JOIN star_schema.item_dim as i ON i.item_key = f.item_key " \
                "JOIN star_schema.time_dim as tim ON tim.time_key = f.time_key " \
                "GROUP BY CUBE(i.item_name, tim.quarter) " \
                "ORDER BY i.item_name, SUM(f.total_price) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name', 'quarter', 'total_price'])
        pd_data['total_price'] = pd_data['total_price'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')
    
    if __name__ == '__main__':
        query8 = Query8()
        data = query8.execute()
        print(data)