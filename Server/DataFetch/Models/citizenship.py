from .db import *
import xmltodict
from time import sleep

db = dbModel()

class citizen:
    def __init__(self, filename, batch):
        self.batch = batch
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

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
            if isinstance(arg1, dict):
                for one in arg1.values():
                    if isinstance(one, dict):
                        for key, value in one.items():
                            db.t_sdn_citizenshipList(arg['uid'],one['uid'], one['country'], one['mainEntry'], iUid)
                            print('Iserted')
                    else:
                        pass
            else:
                pass
            # print (keys)

        if 'citizenshipList' in arg.keys():
            if isinstance(arg['citizenshipList'], dict):
                insider(arg['citizenshipList'])
            else:
                print (arg['citizenshipList'])
