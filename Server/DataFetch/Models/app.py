from .db import *
import xmltodict
from time import sleep

db = dbModel()

class extr:
    def __init__(self, filename, fetchedUID):
        self.batch = fetchedUID
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.object = doc['sdnList']['sdnEntry']
        entity = self.object
        for i in range(0, len(self.object)):
            if isinstance(entity[i], dict):
                self.step_one(entity[i], self.batch)
                self.step_two(entity[i], self.batch)
                self.step_three(entity[i], self.batch)
                self.step_four(entity[i], self.batch)
                self.step_five(entity[i], self.batch)
            else:
                pass

    # Extracts the sdnentry table(sdnUid, lastName, sdnType)
    def step_one(self, arg, iUid):
        lastname = arg['lastName'].replace("'", ' ')
        db.t_sdn_entry(arg['uid'], lastname, arg['sdnType'], iUid)
        print (lastname)


    def step_two(self, arg, iUid):
        if 'firstName' in arg.keys():
            name = arg['firstName'].replace("'", ' ')
            db.t_sdn_firstname(arg['uid'], name, iUid)
            print(name)
        else:
            pass

    def step_three(self, arg, iUid):
        if 'title' in arg.keys():
            tit = arg['title'].replace("'", ' ')
            db.t_sdn_title(arg['uid'], tit, iUid)
            print (arg['lastName'], ':', tit)
        else:
            pass

    def step_four(self, arg, iUid):
        if 'remarks' in arg.keys():
            remark = arg['remarks'].replace("'", ' ')
            db.t_sdn_remarks(arg['uid'], remark, iUid)
            print(arg['lastName'], ':', remark)
        else:
            pass


    def step_five(self, arg, iUid):

        def stringer(ls):
            emgr = ''
            if isinstance(ls, list):
                for each in ls:
                    emgr +=' {}'.format(each)
                db.t_sdn_programlist(arg['uid'], str(emgr), iUid)
            else:
                pass

        def inner(val):
            if isinstance(val, dict):
                for key, value in val.items():
                    if isinstance(value, dict):
                        inner(value)
                    else:
                        if isinstance(value, list):
                            stringer(value)
                        else:
                            db.t_sdn_programlist(arg['uid'], value, iUid)
                            # pass
            else:
                db.t_sdn_programlist(arg['uid'], val, iUid)
                print(arg['uid'], val)

        if 'programList' in arg.keys():
            if isinstance(arg['programList'], dict):
                inner(arg['programList'])
            else:
                db.t_sdn_programlist(arg['uid'], arg['programList'], iUid)
                print(arg['uid'], arg['programList'])
        else:
            pass
