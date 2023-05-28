from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.store_key, p.month, AVG(t.total_price) " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Store_dim\" s on s.store_key=t.store_key " \
                      "JOIN star_schema.\"Time_dim\" p on p.time_key=t.time_key " \
                      "GROUP BY s.store_key, p.month " \
                      "ORDER BY s.store_key, p.month"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=['Store Key', 'Month', 'Average Sales'])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query10 = Query10()
    data = query10.execute()
    print(data)
