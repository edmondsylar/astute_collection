from .db import *
import xmltodict
from time import sleep

db = dbModel()

class POB:
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
                            place = one['placeOfBirth'].replace("'", ' ')
                            db.t_sdn_placeOfBirthList(arg['uid'],one['uid'], place, one['mainEntry'], iUid)
                            print (arg['uid'],one['uid'], one['placeOfBirth'], one['mainEntry'], iUid)

                    else:
                        # print (arg['uid'], one, type(one))
                        if isinstance(one, list):
                            for each in one:
                                if isinstance(each, dict):
                                    for key, value in each.items():
                                        pass
                                        # print ('{}_{}:\n \t{} : {}'.format(arg['uid'], key, key, value))
                                        # sleep(1)

            else:
                pass
            # print (keys)

        if 'placeOfBirthList' in arg.keys():
            if isinstance(arg['placeOfBirthList'], dict):
                insider(arg['placeOfBirthList'])
            else:
                print (arg['placeOfBirthList'])
