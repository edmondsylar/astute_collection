# import schedule
from time import sleep
from .Models.restOfVars import rest
from .Models.app import extr
from .Models.aka import akaExtract
from .Models.id import extrid
from .Models.address import dictbreak_down
from .Models.nationality import nationality
from .Models.citizenship import citizen
from .Models.birthday import birth
from .Models.placeOfbirth import POB
from .Models.vesell import ves
from .Models.vesVars import vessel
from .Models.restOfVars import rest


class container:
    # This is the main call to all the other scripts.
    def __init__(self, file, batch):
        self.file = file
        self.batch = batch
        self.executions(self.file, self.batch)

    def executions(self, file, arg):
        extr(file, arg)
        print ("Done main Entries..")

        akaExtract(file, arg)
        print ("Done with aka's")


        extrid(file, arg)
        print ("Done Id's")
        # sleep(2)

        dictbreak_down(file, arg)
        print ("Done addresses")

        nationality(file, arg)
        print ('Done with nationalities.')

        citizen(file, arg)
        print ('Done with citizenShip table.')

        birth(file, arg)
        print ('Done this birthdays')

        POB(file, arg)
        print ('Done places of birth.')

        ves(file, arg)
        print('Done with the vessel infomation.')

        vessel(file, arg)
        print ('Done with vessel Variables.')

        rest(file, arg)
        print ('Completed all the extractions from the document.')
