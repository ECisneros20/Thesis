#!/usr/bin/env python
import tf
import rospy

if __name__ == '__main__':

    x=0.311
    y=0.3455
    z=0.1638

    rospy.init_node('thesis_tf_broadcaster')
    
    transform = tf.TransformBroadcaster()

    rate = rospy.Rate(50)

    while not rospy.is_shutdown():

        transform.sendTransform((x, -y, z),
            tf.transformations.quaternion_from_euler(0, 0, 0),
            rospy.Time.now(),"ruedafrentederecha","base_link")

        transform.sendTransform((-x, -y, z),
            tf.transformations.quaternion_from_euler(0, 0, 0),
            rospy.Time.now(),"ruedatraseraderecha","base_link")

        transform.sendTransform((x, y, z),
            tf.transformations.quaternion_from_euler(0, 0, 0),
            rospy.Time.now(),"ruedafrenteizquierda","base_link")

        transform.sendTransform((-x, y, z),
            tf.transformations.quaternion_from_euler(0, 0, 0),
            rospy.Time.now(),"ruedatraseraizquierda","base_link")

        transform.sendTransform((0.4090, 0.0, 0.4430),
            tf.transformations.quaternion_from_euler(0, 0, 0),
            rospy.Time.now(),"hokuyo_link","base_link")
#z 0.371
        transform.sendTransform((0.5, 0.0, 0.371),
            tf.transformations.quaternion_from_euler(0, 0, 0),
            rospy.Time.now(),"depth_link","base_link")
