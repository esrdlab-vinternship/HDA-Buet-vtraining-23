from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT item_name, quarter " \
                      "FROM (" \
                      "SELECT p.item_name, s.quarter, SUM(t.total_price) AS sum, " \
                      "RANK() OVER (PARTITION BY p.item_name ORDER BY SUM(t.total_price) ASC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Item_dim\" p on p.item_key=t.item_key " \
                      "GROUP BY p.item_name, s.quarter" \
                      ") subquery " \
                      "WHERE rank = 1 " \
                      "ORDER BY item_name"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Item Name", "Worst Quarter"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query8 = Query8()
    data = query8.execute()
    print(data)
