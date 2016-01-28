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

#initial values
position = {'x': 0.0, 'y': 0.0, 'theta': 0.0}
velocity = {'lv': 0, 'av': 0}
next_goal = [0.0, 0.0]
reached = False

def next_goal_callback():
    #set new position of goal
    #set reached control boolean to False
    reached = False

def pose_callback(msg):
    #set most recent position variables
    global position
    position = {'x': msg.x, 'y': msg.y, 'theta': msg.theta}

    #set most recent velocity variables
    global velocity
    velocity = {'lv': msg.linear_velocity, 'av': msg.angular_velocity}

    # rospy.loginfo("Received a turtle1/pose update!")
    rospy.loginfo("Position: [ x: %f, y: %f, theta: %f ]"%(msg.x, msg.y, msg.theta))
    # rospy.loginfo("Velocity: [ linear_velocity: %f, angular_velocity: %f ] "%(msg.linear_velocity, msg.angular_velocity))

def next_goal_callback(msg):
    #update next goal we are going for
    next_goal = [1.0, 1.0]

def navigation():
    #create node
    rospy.init_node('navigation', anonymous=True)
    rate = rospy.Rate(20) # 10hz

    

    #create subscribers
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    rospy.Subscriber("next_goal", Goal, next_goal_callback)

    #create publishers
    cv_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    gs_publisher = rospy.Publisher('game_status', String, queue_size=10)

    while not rospy.is_shutdown():
        rospy.loginfo("Current position: [ x: %f, y: %f, theta: %f ]"%(position['x'], position['y'], position['theta']))
        # rospy.loginfo("Current velocity: [ linear_velocity: %f, angular_velocity: %f ] "%(velocity['lv'], velocity['av']))

        # pub.publish(hello_str)

        #checking variables to find most recent position and velocity
        #do navigation rules here
        
        #check if reached goal: if within goal radius, publish to game_status. Message is string "capture!"
        #if reached, set a control boolean to true, and send 0 velocity
        #publish to cmd_vel if not reached goal
        rate.sleep()

if __name__ == '__main__':
    try:
        navigation()
    except rospy.ROSInterruptException:
        pass
