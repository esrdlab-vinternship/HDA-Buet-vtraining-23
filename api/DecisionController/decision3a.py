from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision3a:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT item_name, sales " \
                      "FROM (" \
                      "SELECT p.item_name, SUM(t.total_price) AS sales, " \
                      "RANK() OVER (ORDER BY SUM(t.total_price) DESC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Item_dim\" p on p.item_key=t.item_key " \
                      "WHERE p.description = 'a. Beverage - Soda' " \
                      "GROUP BY p.item_name " \
                      ") subquery " \
                      "ORDER BY rank"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Name", "Sales"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision3a = Decision3a()
    data = decision3a.execute()
    print(data)
