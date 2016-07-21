# https://github.com/dbader/schedule/blob/master/FAQ.rst
import helper, schedule, time

'''
# Created by Paul Cameron
# This script was created to shutdown a list of desktops via Power Shell
'''

'''
Set the Timer to which this needs to be run
'''
#helper.ps.input_test()

helper.campus_implode()
print("finished running task")

#schedule.every().friday.at("09:23").do(helper.ps.campus_implode)

#while True:
#    schedule.run_pending()
#    time.sleep(1)
