from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT sd.store_key,id.item_name, SUM(t.quantity) " \
              "FROM star_schema.fact_table t " \
              "JOIN star_schema.item_dim id on id.item_key=t.item_key " \
                "JOIN star_schema.store_dim sd on sd.store_key=t.store_key " \
                "GROUP BY CUBE(sd.store_key,id.item_name) " \
                "ORDER BY sd.store_key,SUM(t.quantity) DESC"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store_id','item', 'quantity'])
        pd_data['quantity'] = pd_data['quantity'].astype('float64')
        pd_data = pd_data.dropna()
        top3 = pd_data.groupby('store_id').head(3)
        grouped_items_by_storeID = top3.groupby('store_id')

        result = []
        for store_id, indices in grouped_items_by_storeID.groups.items():
            temp_dict = {}
            temp_dict['store_id'] = store_id
            group = top3.loc[indices]
            temp_dict['items'] = group['item'].to_list()

            result.append(temp_dict)

        return result


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)