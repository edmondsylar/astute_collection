import xmltodict
from time import sleep
import pymysql
from db import dbModel


class dictbreak_down:
    def __init__(self, filename):
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.my_obj = doc['sdnList']['sdnEntry']
        self.report = open('report.txt', 'w+')

        count = (len(self.my_obj))
        for i in range(0, count):
            self.obj = self.my_obj[i]
            vals = []
            keys = []
            for each in self.obj.values():
                vals.append(each)

            for key in self.obj.keys():
                keys.append(key)

            print (keys)
            self.report.write('\n\n{}'.format(keys))

            x = iter(vals)
            for i in range(0, len(vals)):
                your_keys = keys
                y = next(x)
                if isinstance(y, dict):
                    self.dictor(y)
                    continue
                else: #This is else One.
                    print ('\n{} : {}'.format(your_keys[i], y))
                    self.report.write('\n{} : {}\n'.format(your_keys[i], y))
                    if your_keys[i] == 'firstName':
                        # continue
                        pass
                    elif your_keys[i] == 'lastName' or 'sdnUid' or 'uid':
                        # continue
                        pass
                    # This is my t_sdnenrty table
                # continue

            # print ('Done {}'.format(i))
            # This is the step for the actual dtabase call.
            self.report.write('End Of entity\n\n')
            continue

    def dictor(self, arg):
        for a, b in arg.items():
            if isinstance(b, dict):
                self.sorter(a, b)
            elif isinstance(a, dict):
                self.sorter(a, a)
            else:
                pass
                # continue
                # print ('{}: {}'.format(a, b))
        # continue
            # sleep(2)

    def sorter(self, a, arg):
        self.report.write('{}:\n'.format(a))
        print ('\n{}:'.format(a))
        for v, z in arg.items():
            if isinstance(z, dict):
                self.dictor(z)
            else:
                print ('\t{}_{} : {}'.format(a, v, z))
                self.report.write('\t{}_{} : {}\n'.format(a, v, z))
                # continue
            # continue

        # print ('Done one')



test= dictbreak_down('testfile.xml')
