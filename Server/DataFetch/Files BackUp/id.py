from db import *
import xmltodict
from time import sleep

db = dbModel()

class extrid:
    def __init__(self, filename):
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.object = doc['sdnList']['sdnEntry']
        entity = self.object
        for i in range(0, len(self.object)):
            if isinstance(entity[i], dict):
                self.idList(entity[i])

            else:
                pass

    def idList(self, arg):

        def insider(arg1):
            if isinstance(arg1, dict):
                for one in arg1.values():
                    if isinstance(one, dict):
                        for key, value in one.items():
                            if 'idCountry' in one.keys():
                                db.t_sdn_idList_idCountry(arg['uid'], one['uid'], one['idCountry'], None)
                                print ('This is the idCountry:\n\t{}'.format(one['idCountry']))

                            elif 'issueDate' in one.keys():
                                db.t_sdn_idList_issueDate(arg['uid'], one['uid'], one['issueDate'], None)
                                print ('This is an Issue date\n\t',one['issueDate'])
                                # sleep(2)
                            # print ('Not present.')
                            elif 'idType' in one.keys():
                                db.t_sdn_idList_idytype(arg['uid'], one['uid'], one['idType'], None)
                                print ('This is the idType:\n\t{}'.format(one['idType']))

                            elif 'idNumber' in one.keys():
                                db.t_sdn_idList_idnumber(arg['uid'], one['uid'], one['idNumber'], None)
                                print ('This is the idNumber:\n\t{}'.format(one['idNumber']))
                                sleep(2)

                            elif 'expirationDate' in one.items():
                                print ('This is the expriryDate:\n\t{}'.format(one['expirationDate']))
                                sleep(2)

                            else:
                                print ('{}, {}'.format(arg['uid'], one['uid']))
                                # db.t_sdn_idList(arg['uid'], one['uid'], None)
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

test=extrid('testfile.xml')
