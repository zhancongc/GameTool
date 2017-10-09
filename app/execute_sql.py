import pymysql


class ExecuteSQL(object):
    def __init__(self, host, port, user, password, database, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.con = self.connect_db()
        self.cur = self.con.cursor()

    def connect_db(self):

        con = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.database,
            charset='utf8'
        )
        return con

    def execute(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.con.commit()
        return result

    def close(self):
        self.con.close()

