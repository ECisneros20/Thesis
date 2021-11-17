#!/usr/bin/env python
import tf
import rospy

if __name__ == '__main__':

    x=0.21
    y=0.30
    z=-0.05

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

