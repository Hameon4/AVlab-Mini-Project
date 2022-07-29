# AVlab-Mini-Project

Robot Name: pose_subscriber<br>
DNS: 34.125.188.221<br>
Coordinate API: http://34.125.188.221/pose_subscriber/1/2 <i>[replace 1 and 2 with any other number]</i><br>
Plot Diagram API: http://34.125.188.221/pose_subscriber<br><hr>
Regarding the files attached here, the <<i>py_log.py</i>> file is responsible for receiving the coordinates from the turtlesim in ROS. <br>
It then appends the data into a csv file called <pose_subscriber_loc.csv>.<br> 
The csv file is divided into three columns: [Date with time, x coordinates, y coordinates]<br>
The other python file, <matplot.py>, extracts the data from the csv file created, and plots them into a diagram.<hr>

The web.sh file displays the plotted file into the html page under the Plot Diagram API 
