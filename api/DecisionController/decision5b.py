from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision5b:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT description, quarter, item_name, quantity_sold " \
                      "FROM (" \
                      "SELECT p.description, p.item_name, s.quarter, SUM(t.quantity) AS quantity_sold, " \
                      "RANK() OVER (PARTITION BY p.description, s.quarter ORDER BY SUM(t.quantity) DESC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Item_dim\" p on p.item_key=t.item_key " \
                      "WHERE p.description like 'Food%' AND s.year = 2020 " \
                      "GROUP BY p.description, s.quarter, p.item_name " \
                      ") subquery " \
                      "WHERE rank <= 2 " \
                      "ORDER BY description, quarter, rank"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Type", "Quarter", "Item Name", "Quantity Sold"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision5b = Decision5b()
    data = decision5b.execute()
    print(data)
