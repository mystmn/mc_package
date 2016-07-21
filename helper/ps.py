import subprocess, schedule, os, sys
from datetime import datetime
from subprocess import check_output
import helper

feeding_file_list = os.getcwd() + r'\test2.txt'


def input_test():
    fs = helper.FileManagement('campus_restart_log1.txt')
    fs.main_station(['1', '12', '123', '1234'], "n")


def campus_implode():
    computer_list = []
    ts = ('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
    fs = helper.FileManagement('campus_restart_log.txt')
    computer_list.extend("start: {} \n".format(ts))

    with open(feeding_file_list) as f:
        content = f.readlines()
        start_timer = datetime.now()
        for each in content:
            # print(sys.getsizeof(each))

            each_filtered = each.replace(" ", "").rstrip()
            cmd_one = ['powershell.exe', 'test-connection', '-Computername ' + each_filtered + ' -Count', '1', '-Quiet']

            l = check_output(cmd_one, stderr=subprocess.STDOUT)

            device_name = l.rstrip()
            device_on = device_name.decode("utf-8")  # removes new line and bytes

            if device_on == str(True):
                # cmd_two = ['powershell.exe', 'stop-computer', '-force', '-Computername ' + each.rstrip()]

                # check_output(cmd_two, stderr=subprocess.STDOUT)
                def_message = "{}, Rebooted,\n ".format(each_filtered)
                computer_list.append(def_message)
            else:
                def_message = "{}, Failed,\n".format(each_filtered)
                computer_list.append(def_message)

    computer_list.append(
        '\nfinished {:%Y-%m-%d %H:%M:%S}... took {}'.format(datetime.now(), datetime.now() - start_timer))
    fs.main_station(computer_list, 'n')

    print("finished running task")
    return schedule.CancelJob
