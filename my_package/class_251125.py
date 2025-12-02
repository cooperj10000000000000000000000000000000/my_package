import rclpy
import math
from rclpy.node import Node

from nav_msgs import Odometry
from geometry_msgs.msg import Twist

class MyFirstController(Node):
	def __init__(self):
		print('starting node init')
		super().__init__('myfirstrosnode')
		
		self.timer_period = 0.1
		self.b = 0.1
		self.x = 0
		self.y = 0
		self.yaw = 0
		
		self.xd = 2.0
		self.yd = 2.0
		
		self.kx = 0.1
		self.ky = 0.1
		
		#order, pub sub time
		self.cmd_publisher = self.create_publisher(Twist, '/cmd_vel', 0)
		self.subscription = self.create_subscription(Odometry, '/odom', self.odom_callback, 0)
		self.control_timer = self.create_timer(self.timer_period, self.control_callback)
		
		
		print('end node init')
		
	
	def odom_callback(self, msg):
		self.x = msg.pose.pose.position.x
		self.y = msg.pose.pose.position.y
		
		yaw = math.atan2(2.0*(msg.pose.pose.orientation.w*msg.pose.pose.orientation.z + msg.pose.pose.orientation.x*msg.pose.pose.orientation.y), 1.0 - 2*msg.pose.pose.orientation.w*msg.pose.pose.orientation.y + msg.pose.pose.orientation.z*msg.pose.pose.orientation.z);

	def control_callback(self):
		print(self.x. self.y, self.yaw)
		ex = self.xd - self.x
		ey = self.yd - self.y
		
		u1 = self.kx * ex
		u2 = self.ky * ey
		
		v = math.cos(self.yaw)*u1 + math.sin(self.yaw)*u2
		


def main():
    


if __name__ == '__main__':
    main()
