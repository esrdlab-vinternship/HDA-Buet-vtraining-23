from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        # Now we want to sort by year wise
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT tt.year, s.division, SUM(t.total_price)" \
                      "FROM ecomdb_star_schema.fact_table t " \
                      "JOIN ecomdb_star_schema.time_dim tt on tt.time_key=t.time_key " \
                      "JOIN ecomdb_star_schema.store_dim s ON s.store_key=t.store_key " \
                      "WHERE tt.year = 2015 and s.division = 'BARISAL'" \
                      "GROUP BY CUBE(tt.year, s.division) "
        cur.execute(select_stmt)
        #records = cur.fetchall()

        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['year', 'division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        # print(pd_data)
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
