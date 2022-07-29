#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
import requests


def coordinate_receiver(msg):
	rospy.loginfo("Message received : ")
	rospy.loginfo(f'{msg.x} | {msg.y}')
	requests.post(f'http://34.125.188.221/pose_subscriber/{msg.x}/{msg.y}')

if __name__ == '__main__':
	rospy.init_node('pose_subscriber')

	sub = rospy.Subscriber("/turtle1/pose",Pose, coordinate_receiver)
	
	rospy.spin()
