#include <stdio.h>
#include <stdlib.h>
#include <ros/ros.h>
#include <iostream>
using namespace std;


class data{
          public:
                 char id;
                 float height;
                 float weight;
                 float BMI();
}member1;
float data::BMI(){
       return weight/(height*height);
}

int main(int argc,char **argv)
{
        ros::init(argc,argv,"C_third");
        ros::NodeHandle nh;
        
        member1.id = 'A';
        member1.weight = 85;
        member1.height = 1.80;
        printf("id=%c\n",member1.id);
        printf("size=%f\n",member1.BMI());
        return 0;
}
