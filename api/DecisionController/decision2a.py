from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision2a:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT name, sales " \
                      "FROM (" \
                      "SELECT p.name, SUM(t.total_price) AS sales, " \
                      "RANK() OVER (ORDER BY SUM(t.total_price) DESC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Customer_dim\" p on p.customer_key=t.customer_key " \
                      "WHERE s.hour >= 14 AND s.hour <= 17 AND s.year = 2020 " \
                      "GROUP BY p.name " \
                      ") subquery " \
                      "WHERE rank <= 30 " \
                      "ORDER BY rank"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Name", "Sales"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision2a = Decision2a()
    data = decision2a.execute()
    print(data)
