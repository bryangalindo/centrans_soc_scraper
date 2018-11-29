from constants import UESURL, ues_data
from bs4 import BeautifulSoup
from trackee import Trackee
import requests


class UES:
    def __init__(self):
        self.trackee_data = Trackee.load_db_from_vendor_id(4)

    def __get_containers_from_db(self):
        containers = []
        for trackee in self.trackee_data:
            containers.append(trackee.container_number + '\n')

        return ''.join(containers)

    def get_offhire_dates(self):
        session = requests.Session()
        ues_data['seach'] = self.__get_containers_from_db()

        with session as s:
            response = s.post(UESURL, data=ues_data)
            html = BeautifulSoup(response.content, 'lxml')
            table_row_elements = html.find_all('tr')

            container_statuses = []
            for row in table_row_elements[1:]:
                table_cell_elements = row.find_all('td')

                # Container number split up into 3 cells, need them as one
                container_number = ''.join([cell.text for cell in table_cell_elements[:3]])
                print('Updating container no. {}'.format(container_number))
                offhire_date = table_cell_elements[-2].text
                if offhire_date != 'null':
                    container_statuses.append(dict(container_number=container_number,
                                                   offhire_date=offhire_date))

        return container_statuses




