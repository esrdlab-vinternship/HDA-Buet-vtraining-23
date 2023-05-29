from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision5a:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT item_name, year, quarter, quantity_sold " \
                      "FROM (" \
                      "SELECT p.item_name, s.year, s.quarter, SUM(t.quantity) AS quantity_sold, " \
                      "RANK() OVER (PARTITION BY s.year, p.item_name ORDER BY SUM(t.quantity) DESC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Item_dim\" p on p.item_key=t.item_key " \
                      "WHERE p.description = 'Medicine' " \
                      "GROUP BY p.item_name, s.year, s.quarter " \
                      ") subquery " \
                      "WHERE rank = 1 OR rank = 4 " \
                      "ORDER BY year, item_name, quantity_sold DESC"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Name", "Year", "Quarter", "Quantity"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision5a = Decision5a()
    data = decision5a.execute()
    print(data)
