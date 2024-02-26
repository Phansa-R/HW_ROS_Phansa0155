#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

text = rospy.get_param("/Talker/text") #add
if __name__ == '__main__':
    pub = rospy.Publisher("chatter",String,queue_size=10) #queue_size = ขนาดคิวของข้อมูลที่pubที่สามารถส่งได้
    rospy.init_node("Talker")
    rate = rospy.Rate(0.5) #ความถี่ในการส่งข้อมูลของตัวpub # 0.5 = ส่งข้อมูลทุกๆ 2 วินาที
    
    while(not rospy.is_shutdown()):
        pub.publish(text) #add
        rospy.loginfo("Node1;" + str(text)) #add
        rate.sleep()