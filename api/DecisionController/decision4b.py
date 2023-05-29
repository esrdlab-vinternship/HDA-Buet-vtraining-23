from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision4b:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT store_key, cartons_sold " \
                      "FROM (" \
                      "SELECT p.store_key, SUM(t.quantity) AS cartons_sold, " \
                      "RANK() OVER (ORDER BY SUM(t.quantity) DESC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Store_dim\" p on p.store_key=t.store_key " \
                      "WHERE t.unit = 'cartons' " \
                      "GROUP BY p.store_key " \
                      ") subquery " \
                      "WHERE rank <= 5 " \
                      "ORDER BY rank"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Store Key", "Quantity Sold"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision4b = Decision4b()
    data = decision4b.execute()
    print(data)
