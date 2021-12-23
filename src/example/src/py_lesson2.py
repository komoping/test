#! /usr/bin/env python
import rospy
rospy.init_node("py_lesson2")

num=[]
j=0
for i in range (1,10,2):
   num=num+[i]
   print(num[j],end=' ')
   j+=1
print("\n")
print("max=",max(num))
print("min=",min(num))
print("sum=",sum(num))
