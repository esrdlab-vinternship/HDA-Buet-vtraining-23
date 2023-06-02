from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key as store_key , i.item_name as item_name, SUM(f.quantity) as quantity_sales "\
                "FROM star_schema.fact_table as f "\
                "JOIN star_schema.store_dim as s ON s.store_key = f.store_key " \
                "JOIN star_schema.item_dim as i ON i.item_key = f.item_key " \
                "GROUP BY CUBE(s.store_key, i.item_name) " \
                "ORDER BY s.store_key, sum(f.quantity) DESC "

        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'item_name', 'quantity_sales'])
        pd_data['quantity_sales'] = pd_data['quantity_sales'].astype('float64')
        
        pd_data = pd_data.dropna()
        # top 3 products for each store
        pd_data = pd_data.groupby('store_key').head(3)
        pd_data = pd_data[:30]
        return pd_data.to_dict(orient='records')
    if __name__ == '__main__':
        query6 = Query6()
        data = query6.execute()
        print(data)