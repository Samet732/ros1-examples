#!/usr/bin/env python3
# this program is mixture of publisher and subscriber
import rospy
from std_msgs.msg import Float32
import random

def callback(msg):
	print("Message received:", msg.data)

rospy.init_node('mixture_random')
pub = rospy.Publisher('random', Float32, queue_size=1)
rate = rospy.Rate(2)
sub = rospy.Subscriber('random', Float32, callback, queue_size=1)

while not rospy.is_shutdown():
	print("Sending messsage")
	pub.publish(random.random())
	rate.sleep()
