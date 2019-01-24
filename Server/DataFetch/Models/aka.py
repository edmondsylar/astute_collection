from .db import *
import xmltodict
from time import sleep

db = dbModel()

class akaExtract:
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
                            db.t_sdn_akaList(arg['uid'], one['uid'], one['type'],one['category'], iUid)
                            print ('This is else:\n\t',one['uid'], one['type'], one['category'],)
                            # print ('akaListTable',arg['uid'], one['type'], one['uid'],one['category'])
                            keys.append(key)
                            if 'lastName' in one.keys():
                                lname = one['lastName'].replace("'", ' ')
                                db.t_sdn_akaList_lastName(arg['uid'], one['uid'], lname, iUid)
                                print ('\nLast Name is :', one['lastName'], one['uid'])
                                # sleep(2)
                            # print ('Not present.')
                            elif 'firstName' in one.keys():
                                fname = one['lastName'].replace("'", ' ')
                                db.t_sdn_akaList_firstName(arg['uid'], one['uid'], fname, iUid)
                                print ('\nFirst Name is :', one['firstName'])

                            elif 'category' in one.keys():
                                pass
                                print ('This is else:\n\t',one['uid'], one['type'], one['category'],)
                                db.t_sdn_idList(arg['uid'], one['uid'], iUid)
                        # exit()
                    else:
                        pass
            else:
                pass
            # print (keys)

        if 'akaList' in arg.keys():
            if isinstance(arg['akaList'], dict):
                insider(arg['akaList'])
            else:
                print (arg['akaList'])
