from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT it.item_name,st.division, SUM(t.total_price) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.store_dim st on st.store_key=t.store_key " \
              "JOIN ecombd_star_schema.item_dim it on it.item_key=t.item_key " \
              "GROUP BY CUBE(it.item_name,st.division) "\
              "ORDER BY it.item_name"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name','division','total_sales'])
        pd_data = pd_data.dropna()

        pd_data['total_sales'] = pd_data['total_sales'].astype('float64')

        grouped = pd_data.groupby('item_name')

        final_result=[]

        for item_name, indices in grouped.groups.items():
            temp_dict = {}
            temp_dict['item'] = item_name
            group = pd_data.loc[indices]
            df_with_div_and_totalsales = group[['division','total_sales']]
            temp_dict['Sales'] = df_with_div_and_totalsales.to_dict(orient='records')

            final_result.append(temp_dict)

        #print(final_result)

        return final_result


if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute()
    #print(data)
