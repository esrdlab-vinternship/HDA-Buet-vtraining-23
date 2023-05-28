from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT st.store_key,it.item_name, SUM(t.quantity) " \
              "FROM ecombd_star_schema.fact_table t " \
              "JOIN ecombd_star_schema.store_dim st on st.store_key=t.store_key " \
              "JOIN ecombd_star_schema.item_dim it on it.item_key=t.item_key " \
              "GROUP BY CUBE(st.store_key,it.item_name) "\
              "ORDER BY st.store_key asc, SUM(t.quantity) desc"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_key','item_name','quantity_sales'])
        pd_data = pd_data.dropna()
        pd_data['quantity_sales'] = pd_data['quantity_sales'].astype('int64')

        top3_of_each_store = pd_data.groupby('store_key').head(3)
        #print(top3_of_each_store)

        grouped = top3_of_each_store.groupby('store_key')

        final_result=[]

        for store_key, indices in grouped.groups.items():
            temp_dict = {}
            temp_dict['store_key'] = store_key
            group = top3_of_each_store.loc[indices]
            temp_dict['Sales'] = group['item_name'].to_list()

            final_result.append(temp_dict)

        print(final_result)

        return final_result


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    #print(data)
