#! /usr/bin/env python
import rospy
import random
rospy.init_node("py_lesson5")

"""def welcome(name):
    print("hi",name,"good morning!")
welcome("everyone")
"""
"""def subtract(x1,x2):
     result=x1-x2
     print(result)
subtract(5,3)

a=15
b=5
subtract(a,b)
"""
'''def interest(interest_type,subject):
     print("i like"+interest_type+"~~")
     print("in"+interest_type+",i most like"+subject)
interest(interest_type="move",subject="baseketball")
interest(subject="baseketball",interest_type="move")
'''
'''def subtract(x1,x2):
     return x1-x2
def addition(x1,x2):
     return x1+x2


print("please in put what count")
print("1:add")
print("2:sub")
op=int(input("input1 or 2"))
a=int(input("a="))
b=int(input("b="))
if op==1:
   print("a+b=",addition(a,b))
elif op==2:
   print("a-b=",subtract(a,b))
else:
   print("input error")
'''

'''def calculate(x1,x2):
    addition=x1+x2
    subtract=x1-x2
    mulresult=x1*x2
    divresult=x1/x2
    return addition,subtract,mulresult,divresult

x1=x2=10
add,sub,mul,div =calculate(x1,x2)
print("add=",add)
print("sub=",sub)
print("mul=",mul)
print("div=",div)
'''
'''def list_trans(num):
    a=list(range(len(num)))
    for i in range(len(num)):
        a[i]=num[i]+30
    return a

number=[0,20,40]
ans=list_trans(number)
print(ans)
'''
'''def build_member(name,gender,tel):
    member={"name":name,"gender":gender}
    if tel:
       member["tel"]=tel
    return member
member_name =input("please input name")
member_gender =input("please input gender")
member_tel=input("please input tel")
print(build_member(member_name,member_gender,member_tel))
'''
'''
def forword(left,right,now,start):
    forword={"left":left,"right":right,"now":now,}
    if start:
         if forword["left"]>forword["now"]:
             angle="right turn"
         elif forword["right"]>forword["now"]:
             angle="left turn"
         else:
             angle="go straight"
         return angle


turn_left=10
turn_right=70
start=False
start=int(input("1=start,0=don't start"))
turn_now=int(input("input imw: "))
print(forword(turn_left,turn_right,turn_now,start)) 
'''
'''def filters(x):
    return x if(50<x<100) else None
mydata=[61,66,110,57,256,23,78,95]
filters_object=filter(filters,mydata)
print("right data:",[item for item in filters_object])
'''
'''def square(x):
    return x**2
mydata=[5,10,15,20,25]
squarelist=map(square,mydata)
print("square:",[item for item in squarelist])
'''
"""
x=1
def increase():
   global x
   x+=1
print("before",x)
increase()
print("after",x)
"""
def decide(go_not,now,left,right):
    if go_not==1:
         if left>now:
             ans=("turn right")
         elif right<now:
             ans=("turn left")
         else:
             ans=("go straight")
         return(ans)
go_or_not=int(input("go=1 stay=0\n"))
now_value=int(input("input now robot angle\n"))
left_edge=20
right_edge=80
print(decide(go_or_not,now_value,left_edge,right_edge))





























