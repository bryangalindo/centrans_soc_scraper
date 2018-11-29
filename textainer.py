from constants import MONTHTONUMDICT, csv_base_url, textainer_search_url, textainer_data, headers
from bs4 import BeautifulSoup
from trackee import Trackee
import requests
import csv


class Textainer:
    def __init__(self):
        self.trackee_data = Trackee.load_db_from_vendor_id(1)

    def __get_containers_from_db(self):
        containers = []
        for trackee in self.trackee_data:
            container = trackee.container_number + '\n'
            containers.append(container)

        return ''.join(containers)

    def __get_containers_csv_list(self):
        with requests.Session() as Session: # Used Session() method since new requests.get returned new query param
            containers = self.__get_containers_from_db()
            textainer_data['ctl00$bodyContent$ucEqpIds$txtEqpId'] = containers
            cntr_search_resp = Session.post(url=textainer_search_url,
                                            data=textainer_data,
                                            headers=headers)
            cntr_results_html = BeautifulSoup(cntr_search_resp.content, 'html.parser')

            # Script element contains req'd post data for csv url query params (ReportSession & Control ID)
            script_element = cntr_results_html.find('script', {'language': 'javascript'})
            unformatted_params = script_element.text.split('\"')[5].split('=')

            query_params = '{}={}='.format(unformatted_params[1], unformatted_params[2])
            view_container_url = csv_base_url.format(query_params)
            csv_session = Session.get(view_container_url, headers=headers)

        decoded_content = csv_session.content.decode('utf-8')
        csv_reader = csv.reader(decoded_content.splitlines(), delimiter=',')

        return list(csv_reader)

    def get_offhire_dates(self):
        csv_containers_list = self.__get_containers_csv_list()
        csv_containers_list.pop(0)  # removes header in csv

        offhired_containers = []
        for row in csv_containers_list:
            if 'OFF HIRE' in row:
                offhired_containers.append(row)

        container_statuses = []
        for container in offhired_containers:
            container_number = container[0].replace('-', '')
            print('Updating container no. {}'.format(container_number))
            unformatted_date = container[4].split('-')
            month = MONTHTONUMDICT[unformatted_date[1]]
            formatted_date = '{}-{}-{}'.format(unformatted_date[0], month, unformatted_date[2])
            container_info = dict(container_number=container_number, offhire_date=formatted_date)
            container_statuses.append(container_info)

        return container_statuses

