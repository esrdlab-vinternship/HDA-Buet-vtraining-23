from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute1(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query ="SELECT i.item_name,s.division, SUM(f.total_price) " \
                  "FROM ecomdb_star_schema.fact_table f " \
                  "JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
                  "JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                    "GROUP BY CUBE(s.division,i.item_name) " \
                    "ORDER BY i.item_name,s.division"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item','division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute1()
    print(data)
