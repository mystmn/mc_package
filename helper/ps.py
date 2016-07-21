import subprocess, schedule, os, sys
from datetime import datetime
from subprocess import check_output
import helper

feeding_file_list = os.getcwd() + r'\test2.txt'


def campus_implode():
    computer__push_list = {
        'start': '',
        'device': [],
        'msg': [],
        'finish': ''
    }
    ts = ('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
    fs = helper.FileManagement('campus_restart_log.csv')
    computer__push_list['start'] = "start: {} \n".format(ts)

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
                computer__push_list['device'].append(each_filtered)
                computer__push_list['msg'].append("Rebooted,\n")
                # check_output(cmd_two, stderr=subprocess.STDOUT)
            else:
                computer__push_list['device'].append(each_filtered)
                computer__push_list['msg'].append("Failed,\n")

    computer__push_list['finish'] = '\nfinished {:%Y-%m-%d %H:%M:%S}... took {}' \
        .format(datetime.now(), datetime.now() - start_timer)

    fs.main_station(computer__push_list, 'n')

    return schedule.CancelJob
