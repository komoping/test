#! /usr/bin/env python
import rospy
rospy.init_node("hello_python_node")
rospy.loginfo("hello world")
print("user_name: iclab_xiao_ming" )
password=input("please input password:")
code="aa"
if password==code:
    print("login successfully")
else:
    print("password not correct")
