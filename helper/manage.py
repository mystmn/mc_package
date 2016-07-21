import os, io, linecache
from datetime import datetime


class FileManagement(object):
    def __init__(self, file_path):
        self.user_request = file_path
        self.error_log = "log.txt"

    def main_station(self, msg, x=''):

        # Let's always confirm the file exist
        if not self.confirm():
            self.create()

        self.modify(msg, x)

        print("finished FileManagement")

    def create(self):
        open(self.user_request, 'w')

    def modify(self, msg, status='y'):

        if status is "n":
            log_path = open(self.user_request, 'w')
            for each in msg:
                each.replace(" ", "")
                log_path.write("{}".format(each))

        elif status is "y":
            pass

        else:
            log_path = open(self.error_log, 'w')
            log_path.write("{} failed on {:%Y-%m-%d %H:%M:%S}".format(msg, datetime.now()))

        return log_path

    def deletion(self):
        pass

    def confirm(self):
        log_path = self.user_request
        if os.path.isfile(log_path):
            print("file exist")
            return True
        else:
            print("file doesn't exist")
            return False
