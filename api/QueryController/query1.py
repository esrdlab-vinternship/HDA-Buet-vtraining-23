from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.division, SUM(t.total_price) " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Store_dim\" s on s.store_key=t.store_key " \
                      "GROUP BY CUBE(s.division) " \
                      "ORDER BY s.division "
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=['division', 'sales'])
        df = df.drop(df.index[-1])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query1 = Query1()
    data = query1.execute()
    print(data)
