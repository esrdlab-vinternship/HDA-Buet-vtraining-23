from numpy.ma import count

from DBConnection.dbconf import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()

        select_stmt = "SELECT p.item_name " \
                      "FROM star_schema.\"Fact_table\" t " \
                      "JOIN star_schema.\"Time_dim\" s on s.time_key=t.time_key " \
                      "JOIN star_schema.\"Item_dim\" p on p.item_key=t.item_key " \
                      "JOIN star_schema.\"Trans_dim\" r on r.payment_key=t.payment_key " \
                      "WHERE s.date > (CURRENT_DATE - INTERVAL '{} day') AND " \
                      "(r.trans_type = 'card' OR r.trans_type = 'mobile')".format(self.days)
        cur.execute(select_stmt)
        records = cur.fetchall()

        df = pd.DataFrame(records, columns=["Item Name"])
        return df['Item Name'].tolist()


if __name__ == '__main__':
    query7 = Query7(days=2000)
    data = query7.execute()
    print(count(data))
