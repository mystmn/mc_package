import subprocess, schedule, os, sys
from datetime import datetime
from subprocess import check_output
import helper

feeding_file_list = os.getcwd() + r'\results\test.txt'


def campus_implode():
    computer_push_list = {
        'start': '',
        'device': [],
        'msg': [],
        'model': [],
        'finish': ''
    }

    msg = [
        'Live',
        'No response',
        'Model',
        'Error',
    ]

    ts = ('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))
    fs = helper.FileManagement('results\campus_restart_log.csv')
    computer_push_list['start'] = "start: {} \n".format(ts)

    try:
        with open(feeding_file_list, 'rb') as f:
            print("Found file")

    except IOError:
        print("Could not read file:".format(feeding_file_list))

    with open(feeding_file_list) as f:
        content = f.readlines()
        start_timer = datetime.now()
        for each in content:
            # print(sys.getsizeof(each))

            stripped_var = strip_var(each)
            cmd_ping = ['powershell.exe', 'test-connection', '-Computername ' + stripped_var + ' -Count', '1', '-Quiet']

            device_name = check_output(cmd_ping, stderr=subprocess.STDOUT).rstrip()
            device_on = strip_var(device_name.decode("utf-8").replace("\n", ""))

            if device_on == str(True):
                # REBOOT DEVICE = ['powershell.exe', 'stop-computer', '-force', '-Computername ' + each.rstrip()]

                # subprocess errors: http://stackoverflow.com/questions/23420990/subprocess-check-output-return-code
                try:
                    cmd_model = ['powershell.exe', 'Get-WmiObject', '-Class', 'Win32_ComputerSystem', \
                                 '-computername ' + stripped_var + ' |', 'Select-Object', '-Property', 'Model']
                    device_model = check_output(cmd_model, stderr=subprocess.STDOUT).rstrip()
                    stripped_model = strip_var(device_model.decode("utf-8").replace("\n", ""))[13:]

                except subprocess.CalledProcessError:
                    stripped_model = msg[3]

                computer_push_list['device'].append(stripped_var)
                computer_push_list['msg'].append(msg[0])
                computer_push_list['model'].append(stripped_model)  # Remove Bytes preset information
            else:
                computer_push_list['device'].append(stripped_var)
                computer_push_list['msg'].append(msg[1])
                computer_push_list['model'].append('na')

        computer_push_list['finish'] = 'finished: {:%Y-%m-%d %H:%M:%S} - difference of {}' \
        .format(datetime.now(), datetime.now() - start_timer)

    fs.main_station(computer_push_list, 'n')

    return schedule.CancelJob


def strip_var(x):
    if isinstance(x, str):
        return x.replace(" ", "").rstrip()
    else:
        return "Bogus"
