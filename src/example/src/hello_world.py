#! /usr/bin/env python
import rospy
rospy.init_node("hello_python_node")
rospy.loginfo("hello world")

for i in range(1,10):
   for j in range(1,10):
       print("%d*%d=%2d\t"%(i,j,i*j),end='')
   print("\n")


