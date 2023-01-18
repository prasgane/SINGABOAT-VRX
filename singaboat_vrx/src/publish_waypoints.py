#!/usr/bin/env python3

import rospy
from geographic_msgs.msg import GeoPath, GeoPoseStamped

pub = rospy.Publisher('vrx/waypoints', GeoPath, queue_size=10)
rospy.init_node('waypoint_publisher')
r = rospy.Rate(2) # 10hz
mode = rospy.get_param('mode_of_operation', "overtaking")

if mode == "overtaking":
    lat = -33.7226013209
    lon = 150.67504609858

gps_msg = GeoPoseStamped()
gps_msg.pose.position.latitude = lat
gps_msg.pose.position.longitude = lon
gps_msg.pose.position.altitude = 0
gps_msg.pose.orientation.x = 0
gps_msg.pose.orientation.y = 0
gps_msg.pose.orientation.z = 0
gps_msg.pose.orientation.w = 1

geopath_msg = GeoPath()
geopath_msg.poses.append(gps_msg)

while not rospy.is_shutdown():
    pub.publish(geopath_msg)
    r.sleep()