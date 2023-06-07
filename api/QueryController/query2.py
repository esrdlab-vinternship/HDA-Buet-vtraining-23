from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT t.trans_type, SUM(f.total_price) " \
                "FROM ecomdb_star_schema.fact_table f " \
                "JOIN ecomdb_star_schema.trans_dim t on t.payment_key=f.payment_key " \
                "GROUP BY CUBE(t.trans_type) " \
                "ORDER BY t.trans_type "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['trans_type', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    data = query2.execute()
    print(data)
