# AVlab-Mini-Project

Robot Name: pose_subscriber<br>
DNS: 34.125.188.221<br>
Coordinate API: http://34.125.188.221/pose_subscriber/1/2 <i>[replace 1 and 2 with any other number]</i><br>
Plot Diagram API: http://34.125.188.221/pose_subscriber<br><hr>
The <x_y_script.py> manages the reception of the turtlesim's coordinates and transmits them to my server to the <py_log.py><br>
The <<i>py_log.py</i>> file is responsible for receiving the coordinates from the turtlesim in ROS. <br>
It then appends the data into a csv file called <pose_subscriber_loc.csv>.<br> 
The csv file is divided into three columns: [Date with time, x coordinates, y coordinates]<br>
The other python file, <matplot.py>, extracts the data from the csv file created, and plots them into a diagram.<hr>

The web.sh file displays the plotted file into the html page under the Plot Diagram API <hr>
NOTE: The server is closed at the moment as you're reading this. Do let me know when you need me to start it.
