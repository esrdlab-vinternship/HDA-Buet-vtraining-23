from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute1(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.division, SUM(t.total_price) " \
                "from ecomdb_star_schema.fact_table t " \
                "join ecomdb_star_schema.store_dim s on s.store_key=t.store_key " \
                "group by cube(s.division)" \
                "order by s.division"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query1 = Query1()
    data = query1.execute1()
    print(data)
