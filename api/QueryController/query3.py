from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.division, SUM(t.total_price) " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Store_dim\" s on s.store_key=t.store_key " \
                      "WHERE s.division = 'BARISAL'" \
                      "GROUP BY s.division"
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=['District', 'Total Sales'])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query3 = Query3()
    data = query3.execute()
    print(data)
