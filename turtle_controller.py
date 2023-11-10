#!/usr/bin/env python3
from functools import partial

from matplotlib import offsetbox
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import math
import random

class TurtleControllerNode(Node):
   def __init__(self):
       super().__init__ ("turtle_controller")
       self.cmd_vel_publisher_=self.create_publisher(
         Twist,"/turtle1/cmd_vel",10)
       self.pose_subscriber_ = self.create_subscription (
         Pose,"/turtle1/pose",self.pose_callback,10)
       #self.get_logger().info("Turtle controller has been started")
       #self.timer_= self.create_timer(0.5,self.pose_callback(Pose))
       self.create_timer(1.5,self.call_spawn_service(2,1,2.3))
       self.get_logger().info("Turtle controller has been started")


   def pose_callback(self,pose:Pose):
       cmd = Twist()
       if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
           cmd.linear.x=1.0
           cmd.angular.z=0.9
           self.cmd_vel_publisher_.publish(cmd)
           #self.get_logger().info("Turtle controller has been started 4")
       else:
           cmd.linear.x = 5.0
           cmd.angular.z = 0.0
           #self.cmd_vel_publisher_.publish(cmd)
           #self.get_logger().info("Turtle controller has been started 5")

       #self.create_timer(1.5,self.call_spawn_service(2,1,2.3))

       #self.call_spawn_service(2,1,2.3)
       
      

   def call_spawn_service(self,x,y,theta):
       
       
       client=self.create_client(Spawn,'/spawn')
       while not client.wait_for_service(1.0):
           self.get_logger().warn("waiting foe service")
       request=Spawn.Request()
       #self.get_logger().info("Turtle controller has been started 1")
       #pose=Pose
       request.x=random.uniform(0,11)
       request.y=random.uniform(0,11)
       request.theta= theta
       #request.intial_pose=pose
       future=client.call_async(request)
       future.add_done_callback(partial(self.callback_spawn))
       #self.get_logger().info("Turtle controller has been started2")

   def callback_spawn(self,future):
       try:
           response=future.result()
       except Exception as e:
           self.get_logger().error("Service call failed:%r"%(e,))
       
       #self.get_logger().info("Turtle controller has been started3")

def main(args=None):
    rclpy.init(args=args)
    node=TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

