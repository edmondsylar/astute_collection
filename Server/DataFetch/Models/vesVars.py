from .db import *
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

class vessel:
    def __init__(self, filename, batch):
        self.batch = batch
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.exist = []

        sql = "SELECT sdnUid FROM t_sdn_vesselinfo"
        cur.execute(sql)
        data = cur.fetchall()
        for each in data:
            for all in each:
                self.exist.append(all)

        self.object = doc['sdnList']['sdnEntry']
        entity = self.object
        for i in range(0, len(self.object)):
            if isinstance(entity[i], dict):
                self.akaList(entity[i], self.batch)

            else:
                pass

    def akaList(self, arg, iUid):
        keys = []
        def insider(arg1):
            # print (arg1)
            if isinstance(arg1, dict):
                for one in arg1.values():
                    if isinstance(one, dict):
                        for key, value in one.items():
                            print (key, value)
                    else:
                        pass

                # print ('\nElse:')
                # sleep(3)
                for one in arg1.keys():
                    if isinstance(one, dict):
                        for key, value in one.items():
                            print (key, value)
                    else:
                        if one == 'vesselFlag':
                            vs = ''
                            sql = "SELECT sdnVesselInfoUuid FROM t_sdn_vesselinfo WHERE sdnUid='{}'".format(arg['uid'])
                            cur.execute(sql)
                            data = cur.fetchall()
                            for all in data:
                                for this in all:
                                    vs = this

                            flag =  arg1[one].replace("'", ' ')
                            print ('\n\t',arg['uid'], vs)
                            db.t_sdn_vesselInfo_vesselFlag(vs, arg['uid'], flag, iUid)

                        elif one == 'vesselType':
                            vs = ''
                            sql = "SELECT sdnVesselInfoUuid FROM t_sdn_vesselinfo WHERE sdnUid='{}'".format(arg['uid'])
                            cur.execute(sql)
                            data = cur.fetchall()
                            for all in data:
                                for this in all:
                                    vs = this

                            flag =  arg1[one].replace("'", ' ')
                            print ('\n\t',arg['uid'], vs)
                            db.t_sdn_vesselInfo_vesselType(vs, arg['uid'], flag, iUid)

                        elif one == 'callSign':
                            vs = ''
                            sql = "SELECT sdnVesselInfoUuid FROM t_sdn_vesselinfo WHERE sdnUid='{}'".format(arg['uid'])
                            cur.execute(sql)
                            data = cur.fetchall()
                            for all in data:
                                for this in all:
                                    vs = this

                            flag =  arg1[one].replace("'", ' ')
                            print ('\n\t',arg['uid'], vs)
                            db.t_sdn_vesselInfo_callSign(vs, arg['uid'], flag, iUid)


                        elif one == 'vesselOwner':
                            vs = ''
                            sql = "SELECT sdnVesselInfoUuid FROM t_sdn_vesselinfo WHERE sdnUid='{}'".format(arg['uid'])
                            cur.execute(sql)
                            data = cur.fetchall()
                            for all in data:
                                for this in all:
                                    vs = this

                            flag =  arg1[one].replace("'", ' ')
                            print ('\n\t',arg['uid'], vs)
                            db.t_sdn_vesselInfo_vesselOwner(vs, arg['uid'], flag, iUid)

                        elif one == 'tonnage':
                            vs = ''
                            sql = "SELECT sdnVesselInfoUuid FROM t_sdn_vesselinfo WHERE sdnUid='{}'".format(arg['uid'])
                            cur.execute(sql)
                            data = cur.fetchall()
                            for all in data:
                                for this in all:
                                    vs = this

                            flag =  arg1[one].replace("'", ' ')
                            print ('\n\t',arg['uid'], vs)
                            db.t_sdn_vesselInfo_tonnage(vs, arg['uid'], flag, iUid)

                        elif one == 'grossRegisteredTonnage':
                            vs = ''
                            sql = "SELECT sdnVesselInfoUuid FROM t_sdn_vesselinfo WHERE sdnUid='{}'".format(arg['uid'])
                            cur.execute(sql)
                            data = cur.fetchall()
                            for all in data:
                                for this in all:
                                    vs = this

                            flag =  arg1[one].replace("'", ' ')
                            print ('\n\t',arg['uid'], vs)
                            db.t_sdn_vesselInfo_grossRegisteredTonnage(vs, arg['uid'], flag, iUid)

            else:
                print ('Else')
                # sleep(5)
            # print (keys)

        if 'vesselInfo' in arg.keys():
            if isinstance(arg['vesselInfo'], dict):
                insider(arg['vesselInfo'])
            else:
                print ('failed........!')
