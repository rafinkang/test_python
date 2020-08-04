import cx_Oracle

class DbConnect:
    def __init__(self, host, dbname, user, password, port=1521):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.connection = cx_Oracle.connect(self.user, self.password, self.host+":"+self.port+"/"+self.dbname)
        print(self.connection)

    def execute(self, sql):
        self.sql = sql
        cur = self.connection.cursor()
        cur.execute(sql)
        
        resultList = cur.fetchall()
        # resultList = []
        # for x in cur:
        #     resultList.append(x)

        self.connection.close()
        return resultList

db = DbConnect("192.168.0.68", "orcl", "scott", "tiger", "1521")
print(db.execute("SELECT * FROM dept"))
