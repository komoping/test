#! /usr/bin/env python
import rospy
import random
rospy.init_node("py_lesson4")

'''
a="h","e","l","l","o"
b=tuple(a)
print(b)
print("========================================\n")


tuple1=("a","b")
tuple2=("c","d")
c=tuple1+tuple2
print(c)
print("========================================\n")


tuple3=("a","b")
d=tuple3*2
print(d)
print("========================================\n")


tuple4=("red","green","blue")
(R,G,B)=tuple4
print(R)
print(G)
print(B)
print("========================================\n")


tuple5=(13,1,23,6,45,7,7,45,5,123,1)
e=tuple5.index(5)
print(tuple5)
print(e)
print("========================================\n")


x=("key1","key2","key3")
y=1
keydict=dict.fromkeys(x,y)
print(keydict)
print("========================================\n")
'''
'''
gender={'boy':'xiao min','girl':'xiao mei'}
gender['?']='zi xian'
print(gender)
print("\n")

print(gender['boy'])
print(gender.get('boy'))
print(gender.get('no'))
print("\n")

print(gender.keys())
print("\n")
print("========================================\n")
'''
'''
fruit_dict={'red':'apple','purple':'grape','orange':'orange'}
print(fruit_dict)
print("delete red")
fruit_dict.pop('red')
print(fruit_dict)
print("========================================\n")


delete_dict={'trash':'deleted files','space':'installatio file'}
print(delete_dict)
del delete_dict
print("delete_dict has been delete")
print("========================================\n")
'''

a='pneumonoultramicroscopicsilico-volcanoconiosis/volcanoconiosis'
print(a)
for i in a:
   if i=='l':
     continue
   print(i,end='')
print("========================================\n")














