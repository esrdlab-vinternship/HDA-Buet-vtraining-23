from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT sd.store_key,td.month, AVG(f.total_price) " \
              "FROM star_schema.fact_table f " \
              "JOIN star_schema.time_dim td on td.time_key=f.time_key " \
                "JOIN star_schema.store_dim sd on sd.store_key=f.store_key " \
                "GROUP BY CUBE(sd.store_key,td.month) "\
                "ORDER BY sd.store_key,td.month ASC"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['store','month', 'average_sales'])
        pd_data = pd_data.dropna()

        grouped_items = pd_data.groupby('store')

        result = []
        for item, indices in grouped_items.groups.items():
            temp_dict = {}
            temp_dict['store_id'] = item
            group = pd_data.loc[indices]
            temp_dict['sales'] = group[['month', 'average_sales']].to_dict(orient='records')

            result.append(temp_dict)

        return result


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)