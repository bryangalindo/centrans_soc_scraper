from constants import CGIURL, cgi_data, headers, cgi_cookies
from bs4 import BeautifulSoup
from datetime import datetime
from trackee import Trackee
import requests


class Conglobal:
    def __init__(self):
        self.trackee_data = Trackee.load_db_from_depot_id(20)

    def __get_containers_from_db(self):
        containers = []
        for trackee in self.trackee_data:
            containers.append(trackee.container_number)

        return containers

    def __get_page_source(self, container):
        cgi_data['ctl00$MainContent$gUnitTxt'] = container
        session = requests.Session()
        r = session.post(CGIURL, data=cgi_data, cookies=cgi_cookies, headers=headers)

        return BeautifulSoup(r.content, 'html.parser')

    def __get_offhire_date(self, html, container_number):
        if 'Get EIR Results' in html.text:
            date_results = html.findAll('td')[1].text.split(' ')
            offhire_date = datetime.strptime(date_results[0], '%m/%d/%Y').strftime('%Y-%m-%d')
            container_status = dict(container_number=container_number, offhire_date=offhire_date)
            return container_status

    def get_offhire_dates(self):
        containers = self.__get_containers_from_db()
        container_statuses = []
        for container in containers:
            print('Updating container no. {}'.format(container))
            html = self.__get_page_source(container)
            container_status = self.__get_offhire_date(html, container)
            if container_status is not None:
                container_statuses.append(container_status)

        return container_statuses
