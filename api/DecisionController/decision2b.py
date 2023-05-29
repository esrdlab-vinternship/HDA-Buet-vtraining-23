from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision2b:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT name, days " \
                      "FROM (" \
                      "SELECT p.name, COUNT(DISTINCT s.date) AS days, " \
                      "RANK() OVER (ORDER BY COUNT(DISTINCT s.date) DESC) AS rank " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Customer_dim\" p on p.customer_key=t.customer_key " \
                      "WHERE s.year = 2016 " \
                      "GROUP BY p.name " \
                      ") subquery " \
                      "WHERE rank <= 20 " \
                      "ORDER BY rank"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Name", "Days"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision2b = Decision2b()
    data = decision2b.execute()
    print(data)
