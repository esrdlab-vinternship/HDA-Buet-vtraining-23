from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision3b:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT description, item_name, supplier_final " \
                      "FROM (" \
                      "SELECT p.description, p.item_name, SUM(t.total_price) AS sales, " \
                      "CONCAT  (supplier, ', ', man_country) AS supplier_final, " \
                      "RANK() OVER (PARTITION BY p.description ORDER BY SUM(t.total_price) DESC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Item_dim\" p on p.item_key=t.item_key " \
                      "GROUP BY p.description, p.item_name, supplier_final " \
                      ") subquery " \
                      "WHERE rank = 1 ORDER BY rank"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Item Type", "Item Name", "Supplier"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision3b = Decision3b()
    data = decision3b.execute()
    print(data)
