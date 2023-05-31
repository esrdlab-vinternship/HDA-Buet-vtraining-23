from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute1(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name,t.quarter, SUM(f.total_price) " \
                  "FROM ecomdb_star_schema.fact_table f " \
                  "JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key " \
                  "JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                    "GROUP BY CUBE(t.quarter,i.item_name) " \
                    "ORDER BY SUM(f.total_price)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name','quarter', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data=pd_data.groupby('item_name').head(1)
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute1()
    print(data)
