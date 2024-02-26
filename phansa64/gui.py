#!/usr/bin/env python3

from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
frame = Tk()
frame.title("REMOTE")
frame.geometry("480x180")
rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
def fw():
    print("fw")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)

def bw():
    print("bw")
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)

def lt():
    print("lt")
    cmd = Twist()
    # cmd.linear.x = 1.0
    # cmd.angular.z= 1.0
    cmd.linear.y = 1.0
    cmd.angular.z= 1.0

    pub.publish(cmd)

def rt():
    print("rt")
    cmd = Twist()
    # cmd.linear.x = 1.0
    # cmd.angular.z= -1.0
    cmd.linear.y = 1.0
    cmd.angular.z= -1.0
    pub.publish(cmd)

def rtr():
    print("rtl")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= -1.0
    pub.publish(cmd)

def rtl():
    print("rtl")
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 1.0
    pub.publish(cmd)

def rs():
    print("Reset")
    rospy.wait_for_service('/reset')  # รอให้บริการ "reset" พร้อมใช้งาน
    try:
        reset_service = rospy.ServiceProxy('/reset', Empty)
        response = reset_service()
        rospy.loginfo("Reset Turtlesim Service Response: %s", response)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)


    
B1 = Button(text = "FW", command=fw)
B1.place(x=163, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=163, y=130)

B3 = Button(text = "SL", command=lt)
B3.place(x=20, y=80)

B4 = Button(text = "SR", command=rt)
B4.place(x=300, y=80)

B5 = Button(text = "Rotate L", command=rtl)
B5.place(x=90, y=80)

B6 = Button(text = "Rotate R", command=rtr)
B6.place(x=190, y=80)

B7 = Button(text = "RESET", command=rs)
B7.place(x=390, y=130)


frame.mainloop()