import pymysql

class mydb (object):
    """docstring for mydb """
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.0.22', user='quique', passwd='dilema', db='bot')
        
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
