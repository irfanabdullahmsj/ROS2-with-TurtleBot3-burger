#!/usr/bin/env python3
import rclpy
import random
from rclpy.node import Node
from geometry_msgs.msg import Twist
from time import sleep


class RandwalkTurtle(Node):

    def __init__(self):
        super().__init__("randwalk_turtle_node")
        self.get_logger().info("randwalk_node_start")
        self.cmd_vel_publisher = self.create_publisher(Twist,"/cmd_vel",10)

    def random_move(self):
        cmd = Twist()
        for i in range(1,30):
            cmd.linear.x = random.randint(-10,10) / 10.0
            cmd.angular.z = random.randint(-10,10) / 10.0
            self.cmd_vel_publisher.publish(cmd)
            sleep(2)

def main(args=None):
    rclpy.init(args=args)
    node = RandwalkTurtle()
    node.random_move()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()