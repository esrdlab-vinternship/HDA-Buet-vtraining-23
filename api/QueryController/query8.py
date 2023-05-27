from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name as item, t.quarter, SUM(ft.total_price) as total_sales_price "\
        "FROM ecomdb_star_schema.fact_table ft "\
        "JOIN ecomdb_star_schema.time_dim t ON t.time_key = ft.time_key "\
        "JOIN ecomdb_star_schema.item_dim i ON i.item_key = ft.item_key "\
        "GROUP BY CUBE(i.item_name, t.quarter) "\
        "ORDER BY i.item_name, total_sales_price "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item', 'quarter', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        worst = pd_data.groupby('item').head(1)
        # print(pd_data)
        return worst.to_dict(orient='records')


if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)
