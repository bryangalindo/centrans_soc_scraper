from interport import Interport
from textainer import Textainer
from conglobal import Conglobal
from database import Database
from trackee import Trackee
from caru import Caru
from ues import UES


Database.initialize(database='SOCtracking', user='postgres',
                    password='1234', host='localhost')


def update_containers(func):
    containers = func.get_offhire_dates()
    for container in containers:
        Trackee.save_date_returned_to_db(container['offhire_date'], container['container_number'])


def app():
    caru = Caru()
    update_containers(caru)

    ues = UES()
    update_containers(ues)

    conglobal = Conglobal()
    update_containers(conglobal)

    textainer = Textainer()
    update_containers(textainer)

    interport = Interport()
    update_containers(interport)


if __name__ == '__main__':
    app()
