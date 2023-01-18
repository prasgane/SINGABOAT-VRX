#!/usr/bin/env python3

import rospy
from geographic_msgs.msg import GeoPath, GeoPoseStamped

pub = rospy.Publisher('wamv1/vrx/waypoints', GeoPath, queue_size=10)
pub1 = rospy.Publisher('wamv2/vrx/waypoints', GeoPath, queue_size=10)
rospy.init_node('waypoint_publisher')
r = rospy.Rate(2) # 10hz
mode = rospy.get_param('mode_of_operation', "headon")
geopath_msg_1 = GeoPath()
geopath_msg_2 = GeoPath()

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
    geopath_msg_1.poses.append(gps_msg)
    geopath_msg_2.poses.append(gps_msg)

if mode == "headon":
    gps_msg = GeoPoseStamped()
    gps_msg.pose.position.latitude = -33.7226013209
    gps_msg.pose.position.longitude = 150.67504609858
    gps_msg.pose.position.altitude = 0.
    gps_msg.pose.orientation.x = 0
    gps_msg.pose.orientation.y = 0
    gps_msg.pose.orientation.z = 0
    gps_msg.pose.orientation.w = 1

    geopath_msg_1.poses.append(gps_msg)

    gps_msg_1 = GeoPoseStamped()
    gps_msg_1.pose.position.latitude = -33.72250941580836
    gps_msg_1.pose.position.longitude = 150.67398695490027
    gps_msg_1.pose.position.altitude = 0.
    gps_msg_1.pose.orientation.x = 0
    gps_msg_1.pose.orientation.y = 0
    gps_msg_1.pose.orientation.z = 0
    gps_msg_1.pose.orientation.w = 1

    geopath_msg_2.poses.append(gps_msg_1)


while not rospy.is_shutdown():
    pub.publish(geopath_msg_1)
    pub1.publish(geopath_msg_2)
    r.sleep()