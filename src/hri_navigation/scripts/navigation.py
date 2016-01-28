#!/usr/bin/env python

## Navigation Node
##      Subscribes to 
##          'board_position', 'board_velocity', and 'next_goal'
##      Publishes to:
##          'cmd_vel', sends geometry_msgs/Twist
##          'game_status', sends a std_msgs/String message on game status. 

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from hri_navigation.msg import Goal
from math import atan
from math import pi

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

def distance(point1, point2):
    # Takes in point1: [float, float] and point2: [float, float]
    # Returns the absolute Euclidean distance between the two points
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def angle(point1, point2):
    # Takes in point1: [float, float] and point2: [float, float]
    # Returns the angle in radians between the two points, relative to the x-axis.
    # Use should be: angle(position, goal)
    dif_x = point2[0] - point1[0]
    dif_y = point2[1] - point1[1]
    if dif_x == 0.0:
        if dif_y >= 0:
            angle = pi/2
        else:
            angle = 3*pi/2
    else:
        # Quadrant I: angle between 0 and pi/2
        angle = atan(dif_y / dif_x)
        if dif_x < 0:
            # Quadrant II and III: angle between pi/2 and 3*pi/2
            angle = angle + pi
        elif dif_y < 0:
            # Quadrant IV: angle between 3*pi/2 and 2*pi
            angle = angle + 2*pi
    return angle

def normalize_angle(theta):
    # Take in an angle between -2pi and 2pi and convert it to an angle between 0 and 2pi.
    if theta < 0:
        return theta + 2*pi
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
        # rospy.loginfo("Current position: [ x: %f, y: %f, theta: %f ]"%(position['x'], position['y'], position['theta']))
        # rospy.loginfo("Current velocity: [ linear_velocity: %f, angular_velocity: %f ] "%(velocity['lv'], velocity['av']))

        # Check if we've reached the current goal
        if distance([position['x'], position['y']], next_goal) < goal_radius:
            rospy.loginfo("Reached a goal! Waiting for next goal information")

            # To sent more info: `rostopic pub -1 /next_goal hri_navigation/Goal -- 7.2 3.4`
            # Replace 7.2 and 3.4 with own values
 
            global reached
            reached = True

            gs_publisher.publish("capture!")
            cv_publisher.publish(STOP_TWIST)
        else:
            nav_twist = Twist()
            goal_angle = angle([position['x'], position['y']], next_goal)
            norm_theta = normalize_angle(position['theta'])
            angle_offset = goal_angle - norm_theta

            if abs(angle_offset) < 0.085:
                nav_twist.linear.x = 2.0
                rospy.loginfo("Heading straight for goal! Linear velocity: 2.0")
            else:
                # Proportional control
                if angle_offset  > 0.1745:
                    # 0.1745 rad ~= 10 deg
                    nav_twist.angular.z = 2.0
                    rospy.loginfo("Need to go positive angle! Angular velocity: 2.0")
                elif angle_offset < -0.1745:
                    nav_twist.angular.z = -2.0
                    rospy.loginfo("Need to go negative angle! Angular velocity: 2.0")
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
