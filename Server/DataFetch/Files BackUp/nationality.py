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
                self.akaList(entity[i])

            else:
                pass

    def akaList(self, arg):
        keys = []
        def insider(arg1):
            if isinstance(arg1, dict):
                for one in arg1.values():
                    if isinstance(one, dict):
                        for key, value in one.items():
                            db.t_sdn_nationalityList(arg['uid'],one['uid'], one['country'], one['mainEntry'], None)
                            print('Iserted')
                    else:
                        pass
            else:
                pass
            # print (keys)

        if 'nationalityList' in arg.keys():
            if isinstance(arg['nationalityList'], dict):
                insider(arg['nationalityList'])
            else:
                print (arg['nationalityList'])

test=extrid('testfile.xml')
