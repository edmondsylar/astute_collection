from db import *
import xmltodict
from time import sleep
conn = {
    'host':'localhost',
    'user':'root',
    'passwd':None,
    'database':'development_sdn'
}

inner_con = pymysql.connect(**conn)
cur = inner_con.cursor()


db = dbModel()

class extrid:
    def __init__(self, filename):
        with open(filename) as file:
            doc = xmltodict.parse(file.read())
        self.uids = []
        self.exist = []

        sql = "SELECT sdnUid FROM t_sdn_vesselinfo"
        cur.execute(sql)
        data = cur.fetchall()
        for each in data:
            for all in each:
                self.exist.append(all)
                # for one in all:

        self.object = doc['sdnList']['sdnEntry']
        entity = self.object
        for i in range(0, len(self.object)):
            if isinstance(entity[i], dict):
                self.vessel(entity[i])

            else:
                pass

        for each in self.uids:
            if each in self.exist:
                pass
            else:
                db.t_sdn_vesselInfo(each, None)
                print ('Inserted')

    def vessel(self, arg):
        def insider(arg1):
            # print (arg1)
            if isinstance(arg1, dict):
                for one in arg1.values():
                    if isinstance(one, dict):
                        for key, value in one.items():
                            print (key, value)
                    else:
                        pass

            else:
                print ('Else')
                # sleep(5)
            # print (keys)

        if 'vesselInfo' in arg.keys():
            self.uids.append(arg['uid'])



test=extrid('testfile.xml')
