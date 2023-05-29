from numpy.ma import count

from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Decision1b:
    def __init__(self, year, month, days_start, days_end):
        self.year = year
        self.month = month
        self.days_start = days_start
        self.days_end = days_end
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT division, district, sales " \
              "FROM (" \
                "SELECT p.division, p.district, SUM(t.total_price) AS sales, " \
                "RANK() OVER (PARTITION BY p.division ORDER BY SUM(t.total_price) DESC) AS rank " \
                "FROM star_schema.\"Fact_table\" t " \
                "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                "JOIN star_schema.\"Store_dim\" p on p.store_key=t.store_key " \
                "WHERE s.year = {} AND s.month = {} AND s.day >= {} AND s.day < {} AND " \
                "p.division != p.district " \
                "GROUP BY p.division, p.district " \
               ") subquery " \
               "WHERE rank <= 3 " \
               "ORDER BY division".format(self.year, self.month, self.days_start, self.days_end)
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Division", "District", "Sales"])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    decision1b = Decision1b(year=2018, month=5, days_start=1, days_end=30)
    data = decision1b.execute()
    print(data)
