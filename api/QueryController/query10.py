from numpy.ma import count

from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.store_key, t.month, AVG(f.total_price) as average_price "\
                "FROM star_schema.fact_table f "\
                "JOIN star_schema.store_dim s ON s.store_key = f.store_key "\
                "JOIN star_schema.time_dim t ON t.time_key = f.time_key " \
                "GROUP BY CUBE(s.store_key, t.month) "\
                "ORDER BY s.store_key, t.month " 
        cur.execute(query)
        result = cur.fetchall()
        for r in result:
            if r[1] == None:
                result.remove(r)
            
        for i in range (0, 12, 1):
            result.pop()
            
        pd_data = pd.DataFrame(list(result), columns=['store', 'month', 'average sales'])
        pd_data = pd_data.dropna()
        # return pd_data['store', 'month'].tolist()
        return pd_data.to_dict(orient='records')



if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)
