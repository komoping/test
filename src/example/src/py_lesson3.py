#! /usr/bin/env python
import rospy
import random
rospy.init_node("py_lesson3")



print("number<125 ==0,,number>125 ==1\n")
base=[[[0 for i in range(3)]for j in range(3)]for k in range(3)]
print(base)
print("\n")

for l in range(3):
   for m in range(3):
      for n in range(3):
         a=random.randint(0,255)
         base[l][m][n]=a

print(base)
print("\n")

for o in range(3):
   for p in range(3):
      for q in range(3):
         if base[o][p][q]<125:
            base[o][p][q]=0
         else :
            base[o][p][q]=1

print(base)
print("\n")
print("=========================================================\n")

print("from small to big\n")
x=int(input("please input first number:\t"))
y=int(input("please input second number:\t"))
z=int(input("please input third number:\t"))
number=[x,y,z]
number.sort()
print(number)

'''aa=sorted(number)
print(aa)'''

number.sort(reverse = True)
print(number)

'''bb=sorted(number,reverse = True)
print(bb)'''















