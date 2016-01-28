#!/usr/bin/env python

## Navigation Node
##      Subscribes to 
##          '/turtle1/pose', and 'next_goal'
##      Publishes to:
##          '/turtle1/cmd_vel', sends geometry_msgs/Twist
##          'game_status', sends a std_msgs/String message on game status. 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from hri_navigation.msg import Goal
from math import atan2, pi
from numpy.linalg import norm

# Initialize values and constants
position = {'x': 0.0, 'y': 0.0, 'theta': 0.0}
velocity = {'lv': 0, 'av': 0}
next_goal = [5.0, 5.0]
reached = False
goal_radius = 0.2

STOP_TWIST = Twist()

############################
##  Subscriber Callbacks  ##
############################

def next_goal_callback(msg):
    # Update new next_goal
    global next_goal
    next_goal = [msg.x, msg.y]

    # Update reached control boolean
    global reached
    reached = False

def pose_callback(msg):
    # Update position variables
    global position
    position = {'x': msg.x, 'y': msg.y, 'theta': msg.theta}

    # Update velocity variables
    global velocity
    velocity = {'lv': msg.linear_velocity, 'av': msg.angular_velocity}



##########################
##  Navigation Helpers  ##
##########################

def normalize_angle(theta):
    # Take in an angle between -2pi and 2pi and convert it to an angle between -pi and pi.
    if theta < -pi:
        return theta + 2*pi
    elif theta > pi:
        return theta - 2*pi
    else:
        return theta


############################
##  Main Navigation Node  ##
############################

def navigation():
    # Create node
    rospy.init_node('navigation', anonymous=True)
    rate = rospy.Rate(20) # 20Hz

    # Create subscribers
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    rospy.Subscriber("next_goal", Goal, next_goal_callback)

    # Create publishers
    cv_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    gs_publisher = rospy.Publisher('game_status', String, queue_size=10)

    while not rospy.is_shutdown():
        # Check if we've reached the current goal
        if norm([position['x'] - next_goal[0], position['y'] - next_goal[1]]) < goal_radius:
            rospy.loginfo("Reached a goal! Waiting for next goal information")

            # To send more info: `rostopic pub -1 /next_goal hri_navigation/Goal -- 7.2 3.4`
            # Replace 7.2 and 3.4 with own values
 
            global reached
            reached = True

            gs_publisher.publish("capture!")
            cv_publisher.publish(STOP_TWIST)
        else:
            nav_twist = Twist()
            goal_angle = atan2(next_goal[1] - position['y'], next_goal[0] - position['x'])
            norm_theta = normalize_angle(position['theta'])
            angle_offset = normalize_angle(goal_angle - norm_theta)

            if abs(angle_offset) < 0.085:
                nav_twist.linear.x = 2.0
                rospy.loginfo("Heading straight for goal! Linear velocity: 2.0")
            else:
                # Proportional control
                if angle_offset  > 0.1745:
                    # 0.1745 rad ~= 10 deg
                    nav_twist.angular.z = 2.0
                    rospy.loginfo("Need to go positive angle! Angular velocity: 2.0")
                    rospy.loginfo("goal_angle: %f, norm_theta: %f"%(goal_angle, norm_theta))
                    rospy.loginfo("angle_offset: %f"%(angle_offset))
                elif angle_offset < -0.1745:
                    nav_twist.angular.z = -2.0
                    rospy.loginfo("Need to go negative angle! Angular velocity: 2.0")
                    rospy.loginfo("goal_angle: %f, norm_theta: %f"%(goal_angle, norm_theta))
                    rospy.loginfo("angle_offset: %f"%(angle_offset))
                else:
                    nav_twist.angular.z = angle_offset * 2.0 / 0.1745
                    nav_twist.linear.x = 2.0 * 0.085 / abs(angle_offset)
                    rospy.loginfo("Between -10 deg and 10 deg off! Angular velocity: %f and linear velocity: %f"%(nav_twist.angular.z, nav_twist.linear.x))
            cv_publisher.publish(nav_twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        navigation()
    except rospy.ROSInterruptException:
        pass
