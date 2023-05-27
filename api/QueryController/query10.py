from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key, t.month, AVG(f.total_price) as Average_price "\
"FROM ecomdb_star_schema.fact_table f "\
"JOIN ecomdb_star_schema.store_dim s ON s.store_key = f.store_key "\
"JOIN ecomdb_star_schema.time_dim t ON t.time_key = f.time_key " \
"GROUP BY CUBE(s.store_key, t.month) "\
"ORDER BY s.store_key, t.month "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key', 'month', 'average_sales'])
        pd_data['average_sales'] = pd_data['average_sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)
