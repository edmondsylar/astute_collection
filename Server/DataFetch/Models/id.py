from .db import *
import xmltodict
from time import sleep

db = dbModel()

class extrid:
    def __init__(self, filename, batch):
        self.batch = batch
        print (self.batch)
        # exit()
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.object = doc['sdnList']['sdnEntry']
        entity = self.object
        for i in range(0, len(self.object)):
            if isinstance(entity[i], dict):
                self.idList(entity[i], self.batch)

            else:
                pass

    def idList(self, arg, iUid):

        def insider(arg1):
            if isinstance(arg1, dict):
                for one in arg1.values():
                    if isinstance(one, dict):
                        db.t_sdn_idList(arg['uid'], one['uid'], iUid)
                        print (arg['uid'], one['uid'])
                        # exit()
                        for key, value in one.items():
                            if 'idCountry' in one.keys():
                                db.t_sdn_idList_idCountry(arg['uid'], one['uid'], one['idCountry'],  iUid)
                                print ( iUid)
                                print ('This is the idCountry:\n\t{}'.format(one['idCountry']))

                            elif 'issueDate' in one.keys():
                                db.t_sdn_idList_issueDate(arg['uid'], one['uid'], one['issueDate'],  iUid)
                                print ( iUid)
                                print ('This is an Issue date\n\t',one['issueDate'])
                                # sleep(2)
                            # print ('Not present.')
                            elif 'idType' in one.keys():
                                db.t_sdn_idList_idytype(arg['uid'], one['uid'], one['idType'],  iUid)
                                print ( iUid)
                                print ('This is the idType:\n\t{}'.format(one['idType']))

                            elif 'idNumber' in one.keys():
                                db.t_sdn_idList_idnumber(arg['uid'], one['uid'], one['idNumber'],  iUid)
                                print ( iUid)
                                print ('This is the idNumber:\n\t{}'.format(one['idNumber']))
                                sleep(2)

                            elif 'expirationDate' in one.items():
                                print ('This is the expriryDate:\n\t{}'.format(one['expirationDate']))
                                sleep(2)

                            else:
                                print ('{}, {}'.format(arg['uid'], one['uid']))
                                # db.t_sdn_idList(arg['uid'], one['uid'], self.batch)
                        # exit()
                    else:
                        pass
            else:
                pass

        if 'idList' in arg.keys():
            if isinstance(arg['idList'], dict):
                insider(arg['idList'])
            else:
                print (arg['idList'])
