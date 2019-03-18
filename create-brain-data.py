import requests
import sys
import sched, time
import csv

s = sched.scheduler(time.time, time.sleep)
braindata = []

filename=sys.argv[2]

with open(filename, mode='w') as employee_file:
    print(sys.argv[1])
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['signal_strength', 'attention', 'meditation', 'delta', 'theta', 'low_alpha', 'high_alpha', 'low_beta', 'high_beta', 'low_gamma', 'high_gamma', 'activity_type'])

    def do_something(sc): 
        lols = requests.get('your shiftr.io url')
        activity_type=sys.argv[1]
        dataFromBrain = lols.text.split(',')
        dataFromBrain.append(activity_type)
        employee_writer.writerow(dataFromBrain)
        print(dataFromBrain)    
        s.enter(1, 1, do_something, (sc,))

    s.enter(1, 1, do_something, (s,))
    s.run()

