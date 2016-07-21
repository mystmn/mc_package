import os, io, linecache
from datetime import datetime


class FileManagement(object):
    def __init__(self, log_results):
        self.user_request = log_results
        self.error_log = "log.csv"

    def main_station(self, device_class, x=''):

        # Let's always confirm the file exist
        if not self.confirm():
            self.create()
        closer = self.modify(device_class, x)
        closer.close()

    def create(self):
        open(self.user_request, 'w')

    def modify(self, device_class, status='y'):
        log_path = open(self.user_request, 'w')

        log_path.write('Devices, Status, Model\n')

        if status is "n":
            for device, msg, model in zip(device_class['device'], device_class['msg'], device_class['model']):
                log_path.write('{}, {}, {} \n'.format(device, msg, model))

        elif status is "y":
            pass

        else:
            # needs a log filed for errors
            pass

        # Time stamp the log
        #log_path.write('\n{}'.format(device_class['start']))
        #log_path.write('\n{}'.format(device_class['finish']))

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
