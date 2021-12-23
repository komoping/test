#include <stdio.h>
#include <stdlib.h>
#include <ros/ros.h>
#include <string>
#include <iostream>
using namespace std;
int main(int argc,char **argv)
{
        ros::init(argc,argv,"C_two");
        ros::NodeHandle nh;
        
        char array1[100]="hello";
        char array2[10]="world";
        strcat(array1,array2);
        printf("%s\n",array1);


        char a1[20]="hello";
        char a2[20]="world";
        strcpy(a1,a2);
        printf("%s\n",a1);

        char a3[20]="hello";
        int i=0;
        i=strlen(a1);
        printf("%d\n",i);
        return 0;
}

