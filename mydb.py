import pymysql

class mydb (object):
    """docstring for mydb """
    def __init__(self):
        self.conn = pymysql.connect(host='remotemysql.com', user='flxflmYig3', passwd='kLhQeLLUnm', db='flxflmYig3')
        
    def query( self, sql ) :
        
        cur = self.conn.cursor()
        cur.execute(sql)
        try:
            res = cur.fetchall()
            return res
        except:
            return 1
        cur.close()

    def close(self):

        self.conn.close()

# if __name__ == '__main__':
#     bd = mydb()
#     salida = bd.query('SELECT * FROM tblServerRssNoticias')
#     bd.close()
#     print(salida)