#!/usr/bin/env python3
import rospy
from road_data.msg import RoadStatus

def print_screen(msg):
    print(f"""Distance to front object: {msg.distance_to_front_obj} mm
    Distance to left object: {msg.distance_to_left_obj} mm
    Distance to right object: {msg.distance_to_right_obj} mm
    Distance to back object: {msg.distance_to_back_obj} mm""")

rospy.init_node('roadstatus_printer')
sub = rospy.Subscriber('road_status', RoadStatus, print_screen, queue_size=1)
rospy.spin()
