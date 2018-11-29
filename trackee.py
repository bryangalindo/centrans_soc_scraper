from database import CursorFromConnectionFromPool


class Trackee:
    def __init__(self, container_number, vendor_id, depot_id, date_returned=None):
        self.container_number = container_number
        self.vendor_id = vendor_id
        self.depot_id = depot_id
        self.date_returned = date_returned

    @classmethod
    def save_date_returned_to_db(cls, date, container_number):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('UPDATE tracker '
                           'SET date_returned = %s '
                           'WHERE container_number = %s ',
                           (date, container_number))

    @classmethod
    def load_db_from_vendor_id(cls, vendor_id):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * '
                           'FROM tracker '
                           'WHERE vendor_id = %s AND date_returned IS NULL', (vendor_id,))
            return cls.get_trackee_list(cursor=cursor)

    @classmethod
    def load_db_from_depot_id(cls, depot_id):
        with CursorFromConnectionFromPool() as cursor:
            cursor.execute('SELECT * '
                           'FROM tracker '
                           'WHERE depot_id = %s AND date_returned IS NULL', (depot_id,))
            return cls.get_trackee_list(cursor=cursor)

    @classmethod
    def get_trackee_list(cls, cursor):
        # Returns a list of tracked containers where date returned is empty
        trackee_list = []
        trackee_data = cursor.fetchall()
        for trackee in trackee_data:
            if trackee_data:
                trackee = cls.match_param_with_index(trackee)
                trackee_list.append(trackee)
        return trackee_list

    @classmethod
    def match_param_with_index(cls, var):
        # When executing SELECT *, query returns a tuple with multiple indexes, only need the following
        return cls(container_number=var[2],
                   vendor_id=var[7],
                   depot_id=var[8],
                   date_returned=var[6])
