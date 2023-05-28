from numpy.ma import count

from DBconnection.dbconf import PostgresConnection
import pandas as pd


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Connected with Postgres DB")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        stmt1 = "SELECT it.item_name " \
                "FROM ecombd_star_schema.fact_table t " \
                "JOIN ecombd_star_schema.time_dim tm on tm.time_key=t.time_key " \
                "JOIN ecombd_star_schema.item_dim it on it.item_key=t.item_key " \
                "JOIN ecombd_star_schema.trans_dim tr on tr.payment_key=t.payment_key " \
                "WHERE (tr.trans_type = 'card' or tr.trans_type='mobile' ) and tm.date > (CURRENT_DATE - INTERVAL"
        stmt2 = " '" + str(self.days) + " day')"
        query = stmt1 + stmt2
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['item_name'])
        pd_data = pd_data.dropna()
        # print(pd_data['item_name'].tolist())
        temp_result = pd_data['item_name'].tolist()
        final_result=[]
        result_dict={}
        result_dict['item'] = temp_result
        final_result.append(result_dict)
        return final_result


if __name__ == '__main__':
    query7 = Query7(days=900)
    data = query7.execute()
    #print(count(data))
