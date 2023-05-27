from numpy.ma import count

from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT i.item_name, t.t_date " \
                "FROM star_schema.fact_table f " \
                "JOIN star_schema.item_dim i ON i.item_key = f.item_key " \
                "JOIN star_schema.time_dim t ON t.time_key = f.time_key " \
                "JOIN star_schema.trans_dim trans ON trans.payment_key = f.payment_key " \
                "WHERE t.t_date > (CURRENT_DATE - INTERVAL '" + str(self.days) + " day') AND (trans.trans_type = 'card' or trans.trans_type='mobile') "  
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item', 'date'])
        pd_data = pd_data.dropna()
        # return pd_data['item'].tolist()
        return pd_data.to_dict(orient='records')



if __name__ == '__main__':
    query7 = Query7(days=1000)
    data = query7.execute()
    print(count(data))
