from constants import INTERPORTURL
from trackee import Trackee
from utils import make_soup
from datetime import datetime


class Interport:
    def __init__(self):
        self.trackee_data = Trackee.load_db_from_depot_id(11)

    def __get_containers_from_db(self):
        raw_containers = []

        # Formats containers loaded from DB into query param format for URL
        for index, trackee in enumerate(self.trackee_data):
            if index != (len(self.trackee_data) - 1):
                container = trackee.container_number + '%0D%0A'
                raw_containers.append(container)
            else:
                container = trackee.container_number
                raw_containers.append(container)

        return ''.join(raw_containers)

    def get_offhire_dates(self):
        containers = self.__get_containers_from_db()

        url = INTERPORTURL.format(containers)
        html = make_soup(url)
        table_row_elements = html.find_all('tr')

        container_statuses = []
        for row in table_row_elements:
            row_text = row.text.split()
            container_number = row_text[0] + row_text[1].replace('-', '')
            print('Updating container no. {}'.format(container_number))

            if row_text[2]:
                offhire_date = datetime.strptime(row_text[2], '%m/%d/%Y').strftime('%Y-%m-%d')
                container_statuses.append(dict(container_number=container_number,
                                               offhire_date=offhire_date))

        return container_statuses
