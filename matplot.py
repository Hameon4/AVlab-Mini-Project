#! /usr/bin/python3

import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('pose_subscriber_loc.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[1])
        y.append(row[2])
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Coordinates")
  
plt.xticks(rotation = 25)
plt.xlabel('X-Points')
plt.ylabel('Y-Points')
plt.title('Coordinates Turtlesim', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
plt.savefig('dia1.png')
