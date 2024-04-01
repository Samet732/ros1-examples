#!/usr/bin/env python3
import rospy
from road_data.msg import RoadStatus
from random import randint

rospy.init_node('roadstatus_sender')
pub = rospy.Publisher('road_status', RoadStatus, queue_size=1)
rate = rospy.Rate(100)

while not rospy.is_shutdown():
    msg = RoadStatus()
    msg.distance_to_front_obj = randint(0, 1000000)
    msg.distance_to_left_obj = randint(0, 1000000)
    msg.distance_to_right_obj = randint(0, 1000000)
    msg.distance_to_back_obj = randint(0, 1000000)

    pub.publish()
    rate.sleep()
