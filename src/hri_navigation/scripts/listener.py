#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def cv_callback(msg):
    rospy.loginfo("Received a /cmd_vel update!")
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))

    #May have to do velocity processing here
    #Call services here maybe
    # Calculate new velocity to send

def pose_callback(msg):
    rospy.loginfo("Received a /pose update!")
    rospy.loginfo("Position: [ x: %f, y: %f, theta: %f ]"%(msg.x, msg.y, msg.theta))
    rospy.loginfo("Velocity: [ linear_velocity: %f, angular_velocity: %f ] "%(msg.linear_velocity, msg.angular_velocity))


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/turtle1/cmd_vel", Twist, cv_callback)
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    # spin() simply keeps python from exiting until this node is stopped
    
    while not rospy.is_shutdown():
        #TODO
        #check a flag and 



        rate.sleep()

    # rospy.spin()

if __name__ == '__main__':
    listener()
