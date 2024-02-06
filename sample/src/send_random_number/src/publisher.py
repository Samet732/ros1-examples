#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random

rospy.init_node('random_number_publisher')
pub = rospy.Publisher('random', Float32, queue_size=1)
rate = rospy.Rate(2)

while not rospy.is_shutdown():
	pub.publish(random.random())
	rate.sleep()
