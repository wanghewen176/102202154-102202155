import datetime


class mydateTimeTool(object):
    def __init__(self):
        pass

    def get_current_date_time(self):
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d')

    def get_current_date_time_HMS(self):
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def get_current_date_time_HMSF(self):
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    def date_to_string(self, date):
        return date.strftime('%Y-%m-%d')

    def date_to_string_HMS(self, date):
        return date.strftime('%Y-%m-%d %H:%M:%S')

    def date_to_string_HMSF(self, date):
        return date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    def string_to_date(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%d")

    def string_to_date_HSM(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    def string_to_date_HSMF(self, date_string):
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
