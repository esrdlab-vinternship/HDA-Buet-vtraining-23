from numpy.ma import count

from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name as item, t.quarter, SUM(f.total_price) as sales "\
                "FROM star_schema.fact_table f "\
                "JOIN star_schema.time_dim t ON t.time_key = f.time_key "\
                "JOIN star_schema.item_dim i ON i.item_key = f.item_key "\
                "GROUP BY CUBE(i.item_name, t.quarter) "\
                "ORDER BY i.item_name, sales " 
        cur.execute(query)
        result_temp = cur.fetchall()

        result = []
        for i in range (0, 1300, 5):
            result.append(result_temp[i])
            
        result.pop()

        pd_data = pd.DataFrame(list(result), columns=['item', 'quarter', 'sales'])
        pd_data = pd_data.dropna()
        # return pd_data['item'].tolist()
        return pd_data.to_dict(orient='records')



if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)
