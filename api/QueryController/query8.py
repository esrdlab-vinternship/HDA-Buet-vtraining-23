from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT id.item_name,td.quarter, SUM(f.quantity) " \
              "FROM star_schema.fact_table f " \
              "JOIN star_schema.item_dim id on id.item_key=f.item_key " \
                "JOIN star_schema.time_dim td on td.time_key=f.time_key " \
                "GROUP BY CUBE(id.item_name,td.quarter) " \
                "ORDER BY id.item_name,SUM(f.quantity) ASC"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item','quarter', 'quantity'])
        # pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        worst = pd_data.groupby('item').head(1)
        pd_data = worst[0:20]
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)