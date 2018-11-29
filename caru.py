import requests
from bs4 import BeautifulSoup
from datetime import datetime
from constants import CARUURL, headers
from trackee import Trackee
import multiprocessing


class Caru:
    def __init__(self):
        self.trackee_data = Trackee.load_db_from_vendor_id(14)

    def __get_containers_from_db(self):
        containers = []
        for trackee in self.trackee_data:
            containers.append(trackee.container_number)

        return containers

    def get_offhire_date(self, container_number):
        print('Updating container no. {}'.format(container_number))
        session = requests.Session()

        response = session.get(CARUURL.format(container_number), headers=headers)
        html = BeautifulSoup(response.content, 'html.parser')

        table_element = html.find('table', {'class': 'aa_details'})
        tr_row_elements = table_element.find_all('tr')
        container_number = tr_row_elements[2].text.split(':')[1]

        for row in tr_row_elements[2:]:
            if 'Transit completed :' in row.text:
                date_string = row.text.split(':')[1]
                offhire_date = datetime.strptime(date_string, '%d-%m-%Y').strftime('%Y-%m-%d')
                
                return dict(container_number=container_number, offhire_date=offhire_date)

    def get_offhire_dates(self):
        containers_list = self.__get_containers_from_db()

        pool = multiprocessing.Pool(processes=len(containers_list))
        with pool as p:
            return p.map(self.get_offhire_date, containers_list)
