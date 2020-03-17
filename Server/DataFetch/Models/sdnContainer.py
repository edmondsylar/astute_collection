import schedule
from time import sleep
from restOfVars import rest
from app import extr
from aka import akaExtract
from id import extrid
from address import dictbreak_down

class container:
    # This is the main call to all the other scripts.
    def __init__(self, file):
        self.file = file
        self.executions(file)

    def executions(self, file):
        extr(file)
        print ("Done main Entries..")
        sleep(2)

        akaExtract(file)
        print ("one aka's")
        sleep(2)

        extrid(file)
        print ("Done Id's")
        sleep(2)

        dictbreak_down(file)
        print ("Done addresses")
        sleep(2)

        





container('testfile.xml')
# This will come last
rest(file)
print ('Step One Done........!')
sleep(2)
