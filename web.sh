#!/usr/bin/bash

echo -e "Content-type: text/html\n\n"
echo "<h2>Turtlesim Coordinates Graph</h2>"
./matplot.py
echo " <img src="http://34.125.188.221/cgi/dia1.png" width="500" height="600">"
