from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.item_name, p.division, SUM(t.total_price) " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Item_dim\" s on s.item_key=t.item_key " \
                      "JOIN star_schema.\"Store_dim\" p on p.store_key=t.store_key " \
                      "GROUP BY s.item_name, p.division " \
                      "ORDER BY s.item_name, SUM(t.total_price) DESC"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=['Item Name', 'Division', 'Total Sales'])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query9 = Query9()
    data = query9.execute()
    print(data)
