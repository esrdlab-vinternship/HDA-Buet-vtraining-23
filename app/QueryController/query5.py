from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.year, p.division, SUM(t.total_price) " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Store_dim\" p on p.store_key=t.store_key " \
                      "WHERE s.year = 2015 AND p.division = 'BARISAL'" \
                      "GROUP BY s.year, p.division"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=['Year', 'Division', 'Total Sales'])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query5 = Query5()
    data = query5.execute()
    print(data)
