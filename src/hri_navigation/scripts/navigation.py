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

# Initialize values and constants
position = {'x': 0.0, 'y': 0.0, 'theta': 0.0}
velocity = {'lv': 0, 'av': 0}
next_goal = [5.0, 5.0]
reached = False
goal_radius = 0.2

STOP_TWIST = Twist()


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

    rospy.loginfo("Position: [ x: %f, y: %f, theta: %f ]"%(msg.x, msg.y, msg.theta))

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

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
        rospy.loginfo("Current position: [ x: %f, y: %f, theta: %f ]"%(position['x'], position['y'], position['theta']))
        # rospy.loginfo("Current velocity: [ linear_velocity: %f, angular_velocity: %f ] "%(velocity['lv'], velocity['av']))

        #checking variables to find most recent position and velocity
        #do navigation rules here
        
        #check if reached goal: if within goal radius, publish to game_status. Message is string "capture!"
        if distance([position['x'], position['y']], next_goal) < goal_radius:
            rospy.loginfo("Reached a goal! Waiting for next goal information")
            global reached
            reached = True

            cv_publisher.publish(STOP_TWIST)
        else:
            # nav_twist = calculate
            rospy.loginfo("Goal not reached!")
        #if reached, set a control boolean to true, and send 0 velocity
        #publish to cmd_vel if not reached goal
        rate.sleep()

if __name__ == '__main__':
    try:
        navigation()
    except rospy.ROSInterruptException:
        pass
