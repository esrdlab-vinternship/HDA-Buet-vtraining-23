from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query2_1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT f2.customer_key, SUM(f2.total_price) " \
                "FROM star_schema.fact_table f1 " \
                "JOIN star_schema.fact_table f2 on f2.customer_key=f1.customer_key " \
                "GROUP BY CUBE(f2.customer_key) " \
                "ORDER BY f2.customer_key "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['customer', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query2_1 = Query2_1()
    data = query2_1.execute()
    print(data)
