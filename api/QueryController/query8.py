from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT it.item_name,tm.quarter, SUM(t.total_price) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.time_dim tm on tm.time_key=t.time_key " \
              "JOIN ecombd_star_schema.item_dim it on it.item_key=t.item_key " \
              "GROUP BY CUBE(it.item_name,tm.quarter) "\
              "ORDER BY it.item_name,SUM(t.total_price) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data= pd.DataFrame(result, columns=['item_name','quarter','total_price'])
        pd_data = pd_data.dropna()
        pd_data['total_price'] = pd_data['total_price'].astype('float64')

        worst_season = pd_data.groupby('item_name').head(1)
        #print(worst_season)

        return worst_season.to_dict(orient='records')


if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    #print(data)
