#! /usr/bin/env python
import cv2
import os
import rospy
import numpy as np
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

DATA_PATH = '/home/xilm/Cityscapes/sequence/leftImg8bit/demoVideo/'
if __name__ == '__main__':
    frame = 1
    rospy.init_node('Cityscapes_node', anonymous=True)
    cam_pub_left = rospy.Publisher('Cityscapes_cam_l', Image, queue_size=10)
    bridge = CvBridge()
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if frame == 0:
            frame = 1
        img_l = cv2.imread(os.path.join(DATA_PATH, 'stuttgart_00/stuttgart_00_000000_%06d_leftImg8bit.png'%frame))
        
        header = Header()
        header.stamp = rospy.Time.now()
        header.frame_id = 'map'
        
        cam_pub_left.publish(bridge.cv2_to_imgmsg(img_l, "bgr8"))
        
        rospy.loginfo("camera images have published")
        rate.sleep()
        frame += 1
        frame %= 599