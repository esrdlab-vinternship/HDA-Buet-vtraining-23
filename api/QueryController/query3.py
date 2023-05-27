from DBconnection.dbconf import PostgresConnection
import pandas as pd

class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT s.district, SUM(f.total_price) " \
                "FROM star_schema.fact_table f " \
                "JOIN star_schema.store_dim s on s.store_key=f.store_key " \
                "WHERE s.district='BARISAL' " \
                "GROUP BY CUBE(s.district)  " 
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['district', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        return pd_data.to_dict(orient='records')
        # return pd_data['district'].tolist() # this does not work


if __name__ == '__main__':
    query3 = Query3()
    data = query3.execute()
    print(data)
