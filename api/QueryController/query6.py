from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT store_key, item_name, quantity " \
                      "FROM (" \
                      "SELECT s.store_key, p.item_name, SUM(t.quantity) AS quantity, " \
                      "ROW_NUMBER() OVER (PARTITION BY s.store_key ORDER BY SUM(t.quantity) DESC) AS row_num " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Store_dim\" s on s.store_key=t.store_key " \
                      "JOIN star_schema.\"Item_dim\" p on p.item_key=t.item_key " \
                      "GROUP BY s.store_key, p.item_name " \
                      ") subquery " \
                      "WHERE row_num <= 3 " \
                      "ORDER BY store_key, quantity DESC"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=['Store Key', 'Item Name', 'Quantity Sales'])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query6 = Query6()
    data = query6.execute()
    print(data)
