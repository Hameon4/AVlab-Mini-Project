#! /usr/bin/python3
import os
from datetime import datetime

now = datetime.now() # current date and time

c = os.getenv('QUERY_STRING')
w = [i.split('=')[1] for i in c.split('&')]
x = round(float(w[0]), 2)
y = round(float(w[1]), 2)

date_time = now.strftime('%Y-%m-%d %H:%M:%S')

with open('pose_subscriber_loc.csv', 'a') as f:
        f.write(f'{date_time}, {x}, {y}\n')
