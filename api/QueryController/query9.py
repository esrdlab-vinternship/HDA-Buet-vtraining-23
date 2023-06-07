from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT id.item_name,sd.division, SUM(f.total_price) " \
              "FROM star_schema.fact_table f " \
              "JOIN star_schema.item_dim id on id.item_key=f.item_key " \
                "JOIN star_schema.store_dim sd on sd.store_key=f.store_key " \
                "GROUP BY CUBE(id.item_name,sd.division) "\
                "ORDER BY id.item_name"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item','division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        pd_data = pd_data[0:20]
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute()
    print(data)