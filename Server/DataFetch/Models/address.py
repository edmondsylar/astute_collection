import xmltodict
from time import sleep
import pymysql
from .db import dbModel

db= dbModel()
class dictbreak_down:
    def __init__(self, filename, batch):
        self.batch = batch
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.my_obj = doc['sdnList']['sdnEntry']
        # self.report = open('report.txt', 'w+')
        for i in range(0, len(self.my_obj)):
            if 'addressList' in self.my_obj[i].keys():
                print (self.my_obj[i]['addressList'])
                if isinstance(self.my_obj[i]['addressList'], dict):
                    for one in self.my_obj[i]['addressList'].keys():
                        if one == 'address':
                            print ()
                            # exit()
                            if isinstance(self.my_obj[i]['addressList']['address'], dict):
                                self.dictor(self.my_obj[i]['addressList']['address'], self.my_obj[i]['uid'], self.batch)

                            elif isinstance(self.my_obj[i]['addressList']['address'], list):
                                self.lister(self.my_obj[i]['addressList']['address'], self.my_obj[i]['uid'], self.batch)

                        else:
                            pass




    def lister(self, arg, uid, iUid):
        print ('Received In Dictor')
        if isinstance(arg, list):
            for each in arg:
                if isinstance(each, dict):
                    self.dictor(each, uid, iUid)
                elif isinstance(each, list):
                    self.lister(each, uid, iUid)
                else:
                    print (each)
        else:
            print ('Wrong dataType received.')

        print ('Exiting Lister')
        # sleep(0.5)



    def dictor(self, arg, uid, iUid):
        print ('Received in Lister')
        if isinstance(arg, dict):
            print (arg.keys())
            if 'address2' in arg.keys():
                print ('Found Address2 ')
                print (arg['uid'], uid, arg['address2'])
                add = arg['address2'].replace("'", ' ')
                db.t_sdn_addressList_address2(uid, arg['uid'], add, iUid)
                # sleep(5)
            elif 'address3' in arg.keys():
                print ('Found Address3 ')
                print (arg['uid'], uid, arg['address3'])
                add = arg['address3'].replace("'", ' ')
                db.t_sdn_addressList_address3(uid, arg['uid'], add, iUid)
                # print(uid, arg['uid'], add, iUid)
                # sleep(5)

            elif 'postalCode' in arg.keys():
                print ('Found Postal code.')
                print (arg['uid'], uid, arg['postalCode'])
                add = arg['postalCode'].replace("'", ' ')
                db.t_sdn_addressList_postalCode(uid, arg['uid'], add, iUid)
                # sleep(5)


            elif 'address1' in arg.keys():
                print ('Found Address1 ')
                print (arg['uid'], uid, arg['address1'])
                add = arg['address1'].replace("'", ' ')
                db.t_sdn_addressList_address1(uid, arg['uid'], add, iUid)

            elif 'city' in arg.keys():
                print ('Found City ')
                print (arg['uid'], uid, arg['city'])
                add = arg['city'].replace("'", ' ')
                db.t_sdn_addressList_city(uid, arg['uid'], add, iUid)
                # sleep(5)

            elif 'stateOrProvince' in arg.keys():
                print ('Found StateOrProvice Key.')
                print (arg['uid'], uid, arg['stateOrProvince'])
                add = arg['stateOrProvince'].replace("'", ' ')
                db.t_sdn_addressList_stateorProvince(uid, arg['uid'], add, iUid)
                # sleep(0.5)

            elif 'country' in arg.keys():
                print ('Found country ')
                print (arg['uid'], uid, arg['country'])
                add = arg['country'].replace("'", ' ')
                db.t_sdn_addressList_country(uid, arg['uid'], add, iUid)
                # sleep(1)

            for value in arg.values():
                if isinstance(value, dict):
                    self.dictor(value, uid)
                elif isinstance(value, list):
                    self.lister(value, uid)
                else:
                    print (type(value), value)
        else:
            print ('wrong datatype presented')

        print ('Exiting Dictor')
        # sleep(0.5)
