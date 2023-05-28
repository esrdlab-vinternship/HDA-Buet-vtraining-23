from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_stmt = "SELECT s.bank_name, SUM(t.total_price) " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Trans_dim\" s on s.payment_key=t.payment_key " \
                      "GROUP BY CUBE(s.bank_name) " \
                      "ORDER BY s.bank_name "
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=['Bank Name', 'sales'])
        df = df.drop(df.index[-1])
        return df.to_dict(orient='records')


if __name__ == '__main__':
    query2 = Query2()
    data = query2.execute()
    print(data)
