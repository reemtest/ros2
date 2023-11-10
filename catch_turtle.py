#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import random
from turtlesim.srv import Kill
from my_robot_controller import spawned_turtle, turtle_controller
import random
from turtlesim.srv import Spawn



class CatchTurtleNode(Node):
   
    def __init__(self):
       super().__init__("catch_turtle") 

       self.publisher_=self.create_publisher(
           Twist,"/turtle1/cmd_vel",10)
    
       self.subscriber_ = self.create_subscription (
           Pose,"/turtle1/pose",self.prey_pose_callback,10)
       
       self.get_logger().info("Turtle catcher has been started")
    

          
    def prey_pose_callback(self,pose:Pose):
        self.publisher_.publish(Pose)

    def catch(self,pose:Pose):
        
        if self.distance():
         cmd_vel=Pose()
         cmd_vel.linear_velocity=0.1
         self.publisher_.publish(cmd_vel)

    def kill():
        x=turtle_controller.TurtleControllerNode()
        CatchTurtleNode.catch(x)
        CatchTurtleNode.kill.Request()
        turtle_controller.TurtleControllerNode()


    def distance(base_turtle,spawned_turtle):
       
        distance=math.sqrt((base_turtle.xcor()-spawned_turtle.xcor)**2)+((base_turtle.ycor()-spawned_turtle.ycor)**2)
        if distance<0.1:
            return True
        else:
            return False

    
def main(args=None):
    rclpy.init(args=args)
    node=CatchTurtleNode()
    rclpy.spin(node)
    rclpy.shutdown()