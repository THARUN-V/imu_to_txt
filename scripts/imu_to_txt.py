#! /usr/bin/env python

import os
import rospy
from sensor_msgs.msg import Imu

class ImuToTxt:

    def __init__(self):

        self.file_name = rospy.get_param("/file_name")
        self.imu_topic = rospy.get_param("/imu_topic")
        self.imu_sub = rospy.Subscriber(self.imu_topic,Imu,self.ImuCb)
        
        ## check whether file already exists in the name provided
        if(os.path.exists(self.GetFilePath())):
            os.remove(self.GetFilePath())
            self.imu_file = open(self.GetFilePath(),"w")
        else:
            self.imu_file = open(self.GetFilePath(),"w")

    def ImuCb(self,msg):
        rospy.loginfo_once("Writing Imu Data to txt file ....")
        self.imu_file.write(str(msg.header.stamp)+" "+ 
                            str(msg.angular_velocity.x)+" "+str(msg.angular_velocity.y)+" "+str(msg.angular_velocity.z)+" "+
                            str(msg.linear_acceleration.x)+" "+str(msg.linear_acceleration.y)+" "+str(msg.linear_acceleration.z)+"\n")

    # utility function to get path for saving imu data
    # to a file in txt folder
    def GetFilePath(self):
        return "/"+"/".join(__file__.split("/")[1:-2])+"/txt/"+self.file_name

if __name__ == "__main__":
    rospy.init_node("ImuToTxtPythonNode")
    ImuToTxt()
    rospy.spin()