import pymysql

connection = {
    'host':'localhost',
    'user':'root',
    'passwd':None,
    'database':'sanctions'
}


class dbWork:
    def __init__(self):
        self.conn = pymysql.connect(**connection)
        self.cur = self.conn.cursor()
        self.uids = []
        self.info = []
        self.count = 0

        sql = "SELECT sdnFetchedInformationUid FROM t_sdnfetchedinformation"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for all in data:
            for one in all:
                self.uids.append(one)

        sql_2 = "SELECT sdnUid FROM t_sdnentry"
        self.cur.execute(sql_2)
        data2 = self.cur.fetchall()
        for all in data2:
            for one in all:
                self.info.append(one)

    def one(self):
        now = ''
        self.col = self.uids[-1] #Instances where there are no records in the database yet.
        try:
            print ('step one...')
            sql_3 = "SELECT fetchedInformationUid FROM t_arranged_information"
            self.cur.execute(sql_3)
            data2 = self.cur.fetchall()
            print ('step two')
            print (data2)
            for all in data2:
                for one in all:
                    if one in self.uids:
                        print ('exists...')
                        pass
                    else:
                        now = one
                        sql_insert = """REPLACE INTO t_arranged_entry(listUid, type, FetchedInformationUid)
                        SELECT sdnUid, sdnType, sdnFetchedInformationUid FROM t_sdnentry WHERE sdnFetchedInformationUid='{}'""".format(one)
                        self.cur.execute(sql_insert)
                        self.conn.commit()
                        print ('added...')
                        self.count += 1
                continue
        except Exception as err:
            print (err)

        self.next(now)

    def next(self,arg):
        print ('step three...')
        sql_FUID = """
        INSERT INTO t_arranged_information (records_picked, fetchedInformationUid)
        VALUES ('{}', '{}')
        """.format(self.count, arg)
        self.cur.execute(sql_FUID)
        self.conn.commit()
        print ('Process complete........!')
        print ('{} records kept'.format(self.count))
        exit()


test = dbWork()
test.one()
