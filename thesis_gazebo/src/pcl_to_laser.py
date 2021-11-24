#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header
from sensor_msgs import point_cloud2
from math import sin, cos

laser_msg = LaserScan()

laser_msg_header = Header()
laser_msg_header.frame_id = 'depth_link'
laser_msg.header = laser_msg_header

# Valores acordes al gazebo.xacro
laser_msg.angle_min = -0.523599
laser_msg.angle_max = 0.523599
#laser_msg.angle_increment = 

#laser_msg.range_min = 
#laser_msg.range_max = 
laser_msg.ranges = list()

def callback(data):

    global laser_msg

    x = list()
    y = list()
    z = list()
    i = 0

    assert isinstance(data, PointCloud2)
    gen = point_cloud2.read_points(data, field_names = ("x", "y", "z"), skip_nans = True)
    print(type(gen))

    for p in gen:

        if (p[1] <= 0.000249 and p[1] >= 0.0):

#        if (abs(p[1])-0.00025 <= 0):
            i = i+1

            a = p[0]
            b = p[1]
            c = p[2]

            #x_a = a
            #y_b = b*cos(angulo) - c*sin(angulo)
            #z_c = b*sin(angulo) + c*cos(angulo)
        
            x.append(a)
            y.append(b)
            z.append(c)

    try:
        print(max(x), min(x), max(y), min(y), max(z), min(z))
    except:
        print('No points')
    print(i)
    

if __name__ == '__main__':

    try:
        print("Running")
        
        rospy.init_node('tranform_pcl_to_laser', anonymous=True)
        pub = rospy.Publisher('/depth_camera/laser_scan', LaserScan, queue_size=10)
        sub = rospy.Subscriber('/depth_camera/depth/points', PointCloud2, callback)
        rate = rospy.Rate(30)
        
        while not rospy.is_shutdown():
            pub.publish(laser_msg)
            rate.sleep()
      
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")
