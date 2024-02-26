#!/usr/bin/env python3

from tkinter import *
import rospy
from std_msgs.msg import Int16

frame = Tk()
frame.geometry("200x200")

label = Label(frame, font= ('Arail', 60) , text= '0')
label.pack()

rospy.init_node("GUI_read_sensor")
rate = rospy.Rate(10)
rate.sleep()

pub = rospy.Publisher("Topic_Sensor", Int16, queue_size= 10)

def read(num):
    sensor_read = num.data
    label.config(text = str(sensor_read))

sub= rospy.Subscriber("Topic_Sensor", Int16, callback=read)

frame.mainloop()