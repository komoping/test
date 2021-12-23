#include <stdio.h>
#include <stdlib.h>
#include <ros/ros.h>
#include <iostream>
using namespace std;
int main(int argc,char **argv)
{
        ros::init(argc,argv,"C_third");
        ros::NodeHandle nh;
 
        printf("hello\n");
        return 0;
}
