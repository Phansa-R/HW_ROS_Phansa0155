#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def run(val): # val = value ค่าที่รับมา
    if val.data == 'Hello Wrold': #.data เพราะว่าเวลาปริ้นค่าออกมาเป็น ค่า.data
        rospy.loginfo("Node2:" + "Hello Wrold too")
    else:
        rospy.loginfo("Node2:" + "No msg")

if __name__ == '__main__':
    sub = rospy.Subscriber("chatter",String,callback= run) #call fn ที่รันขึ้นมา
    rospy.init_node("Listener")
    rospy.spin() #spin คือให้ทำงานค่อไปเรื่อยๆ 
