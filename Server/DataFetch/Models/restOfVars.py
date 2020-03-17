from .db import *
import xmltodict
from time import sleep

db = dbModel()

class rest:
    def __init__(self, filename, batch):
        self.batch = batch
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.object = doc['sdnList']['sdnEntry']
        entity = self.object
        for i in range(0, len(self.object)):
            if isinstance(entity[i], dict):
                self.idList(entity[i], self.batch)
                self.akaname(entity[i], self.batch)

            else:
                print (type(entity[i]))


    def idList(self, arg, iUid):
        if 'idList' in arg.keys():
            if isinstance(arg['idList'], dict):
                for key, value in arg['idList'].items():
                    if key == 'id':
                        iddata = arg['idList']['id']
                        if isinstance(iddata, dict):
                            for a, b in iddata.items():
                                if a == 'expirationDate':
                                    print (arg['uid'],iddata['uid'], iddata[a])
                                    db.t_sdn_idList_expirationDate(arg['uid'], iddata['uid'], iddata[a], iUid)
                                elif a == 'idNumber':
                                    db.t_sdn_idList_idnumber(arg['uid'], iddata['uid'], iddata[a], iUid)
                                    # print (arg['uid'], iddata[a])

    def akaname(self, arg, iUid):
        print ('Aka Extractions')
        if 'akaList' in arg.keys():
            aka = arg['akaList']
            if isinstance(aka, dict):
                for key, value in aka.items():
                    if key == 'aka':
                        akList = arg['akaList'][key]
                        if isinstance(akList, dict):
                            # print(akList.keys())
                            for a, b in akList.items():
                                if a == 'firstName':
                                    name = akList[a].replace("'", ' ')
                                    db.t_sdn_akaList_firstName(arg['uid'], akList['uid'], name, iUid)
                                    print (arg['uid'], akList['uid'], akList[a])
        # print(arg.keys())
