import sys
import json
import numpy as np

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from aai4r_edge_interfaces.msg import RobotImageInfo

import cv2
import json
#from PIL import Image as 
import PIL

from fashion_attribute.file_demo_outer_ros2 import FashionAttributeDetection


class FashionNode(Node):
    def __init__(self):
        super().__init__('fashion_attribute')

        self.fashion_attribute_detector = FashionAttributeDetection()
        self.fashion_attribute_detector.load_models()

        self.subscription = self.create_subscription(
            RobotImageInfo,
            '/camera/robot_image_info',
            self.callback,
            1)
        self.subscription  # prevent unused variable warning

        self.publisher_ = self.create_publisher(String, '/aai4r/fashion', 10)

        self.visualize_flag = True

        self.monitor_publisher = self.create_publisher(Image, '/aai4r/fashion/monitor', 1)
        self.cv_bridge = CvBridge()

        self.get_logger().info("fashion node initialized!")


    def publish_img(self, img):
        self.monitor_publisher.publish(self.cv_bridge.cv2_to_imgmsg(img, "bgr8"))


    def callback(self, msg):
        self.get_logger().info("callback called!")
        stamp = msg.stamp
        now = self.get_clock().now().to_msg()
        nano_diff = stamp.nanosec - now.nanosec
        if abs(nano_diff) > 50000000:
            return
        np_arr = np.frombuffer(msg.data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        #frame = imutils.resize(im, width=400)

        img , results = self.fashion_attribute_detector.predict(frame)

        if results != []:
            #self.get_logger().info(json.dumps(msg_data))
            msg_data = {"timestamp":(stamp.sec,stamp.nanosec), "agent_id":msg.agent_id, "fashion": []}
            msg_data["fashion"] = results
            pub_msg = String()
            pub_msg.data = json.dumps(msg_data)
            
            self.get_logger().info(pub_msg.data)
            
            self.publisher_.publish(pub_msg)
            #cv2.imshow("Frame", img)
            #cv2.waitKey(1)
            if self.visualize_flag:
                self.publish_img(img)


def main(args=None):
    rclpy.init(args=args)

    node = FashionNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

