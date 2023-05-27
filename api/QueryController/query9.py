from numpy.ma import count

from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name, s.division, SUM(f.total_price) as total_sales "\
                "FROM star_schema.fact_table f "\
                "JOIN star_schema.item_dim i ON i.item_key = f.item_key "\
                "JOIN star_schema.store_dim s ON s.store_key = f.store_key "\
                "GROUP BY CUBE(i.item_name, s.division) "\
                "ORDER BY i.item_name, s.division " 
        cur.execute(query)
        result = cur.fetchall()

        for r in result: 
            if r[0] == None or r[1] == None or r[0] == '':
                result.remove(r)

        for i in range(0, 4, 1):
            result.pop()

        pd_data = pd.DataFrame(list(result), columns=['item', 'division', 'sales'])
        pd_data = pd_data.dropna()
        # return pd_data['item', 'division'].tolist()
        return pd_data.to_dict(orient='records')



if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute()
    print(data)
