import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import random, math

class IMUPublisher(Node):
    def __init__(self):
        super().__init__('imu_publisher')
        self.pub = self.create_publisher(Imu, 'imu/data', 10)
        self.timer = self.create_timer(0.1, self.publish_imu)  # 10 Hz
        self.get_logger().info('IMU Publisher started')

    def publish_imu(self):
        msg = Imu()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'imu_link'
        # Simulate normal + occasional spike (anomaly)
        msg.linear_acceleration.x = random.gauss(0.0, 0.1)
        msg.linear_acceleration.y = random.gauss(0.0, 0.1)
        msg.linear_acceleration.z = random.gauss(9.8, 0.05)
        # Inject anomaly every ~50 msgs
        if random.random() < 0.02:
            msg.linear_acceleration.z = random.uniform(15.0, 20.0)
            self.get_logger().warn('Anomalous reading injected!')
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = IMUPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
