#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from time import sleep

class StopTurtle(Node):

    def __init__(self):
        super().__init__("stop_turtle_node")
        self.get_logger().info("stop_node_start")
        self.cmd_vel_publisher = self.create_publisher(Twist,"/cmd_vel",10)

    def stop(self):
        cmd = Twist()
        for i in range(1,10):
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.cmd_vel_publisher.publish(cmd)
            sleep(0.2)

def main(args=None):
    rclpy.init(args=args)
    node = StopTurtle()
    node.stop()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


