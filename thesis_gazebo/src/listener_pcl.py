#!/usr/bin/env python
import rospy
from math import cos, sin, pi
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2, PointField
from sensor_msgs import point_cloud2
import time
#import csv

pub = rospy.Publisher('/pcl_xyz', String, queue_size=1000)

def callback_pointcloud(data):

    cloud_points = list()

    x = list()
    y = list()
    z = list()

    mensaje = ""
    
    gen = point_cloud2.read_points(data, field_names = ("x", "y", "z"), skip_nans = True)
    
    angulo = -0.0326#37657    # Angulo de inclicacion de la camara 3D
    i = 0

    # En total la camara 3D detecta 462080 puntos
    tiempo_inicio = time.time()
    for p in gen:
        a = p[0] #x
        b = p[1] #y
        c = p[2] #z

        x.append(a)
        y.append(b)
        z.append(c)

#        mensaje = mensaje + " x: " + "{:.3f}".format(a) + ", y: " + "{:.3f}".format(b) + ", z: " + "{:.3f}".format(c) + ";\n"
        #mensaje = mensaje + a + b + c + '\n'
        mensaje = mensaje + str(a)

    print(max(x), min(x), max(y), min(y), max(z), min(z))

        # Rotacion eje x
'''        x = a*cos(angulo) - c*sin(angulo)
        y = b
        z = a*sin(angulo) + c*cos(angulo)
        #i = i + 1

        if z > 0.35 and z < 0.40:
            cloud_points.append(z)
        #print(x, y, z)

        if abs(x) < 2.0 and (0.5976-y)< 0.2 and abs(z) < 1.5:
        #if abs(x) < 0.5 and abs(z) < 1.5:
        
            i = i + 1
            #print(str(i) + " x: " + "{:.3f}".format(x) + " y: " + "{:.3f}".format(0.5976-y) + " z: " + "{:.3f}".format(z))
            #mensaje = mensaje + " x: " + "{:.3f}".format(x) + ", y: " + "{:.3f}".format(0.5976-y) + ", z: " + "{:.3f}".format(z) + ";\n"
            mensaje = mensaje + "{:.3f}".format(x) + "," + "{:.3f}".format(0.5976-y) + "," + "{:.3f}".format(z) + ";"
            
            # write a row to the csv file
            #writer.writerow("{:.3f}".format(x) + "," + "{:.3f}".format(0.5976-y) + "," + "{:.3f}".format(z))
    #print("*******************", "y_max")
    '''
    #print(cloud_points)
    
    #print(i, time.time()-tiempo_inicio)
    #pub.publish(mensaje)


def ejecutarNodo():
    rospy.init_node('listener_pcl', anonymous=True)

    rospy.Subscriber("/depth_camera/depth/points", PointCloud2, callback_pointcloud)
    
    rospy.spin()
    

if __name__ == '__main__':
    try:
        print("Running")
        ejecutarNodo()
    
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")