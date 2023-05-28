from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT st.store_key,tm.month, avg(t.total_price) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.store_dim st on st.store_key=t.store_key " \
              "JOIN ecombd_star_schema.time_dim tm on tm.time_key=t.time_key " \
              "GROUP BY CUBE(st.store_key,tm.month) "\
              "ORDER BY st.store_key,tm.month "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key','month','total_sales'])
        pd_data = pd_data.dropna()

        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')

        grouped = pd_data.groupby('store_key')

        final_result=[]

        for store_key, indices in grouped.groups.items():
            temp_dict = {}
            temp_dict['store_key'] = store_key
            group = pd_data.loc[indices]
            df_with_month_and_totalsales = group[['month','total_sales']]
            temp_dict['Sales'] = df_with_month_and_totalsales.to_dict(orient='records')

            final_result.append(temp_dict)

        #print(final_result)

        return final_result


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    #print(data)
