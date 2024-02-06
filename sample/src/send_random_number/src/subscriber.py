#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(msg):
	print(msg.data)

rospy.init_node('random_subscriber')
sub = rospy.Subscriber('random', Float32, callback, queue_size=1)
rospy.spin()
