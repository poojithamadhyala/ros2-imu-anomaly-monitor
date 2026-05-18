import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import math

THRESHOLD = 12.0  # m/s^2 — flag anything above this

class AnomalyDetector(Node):
    def __init__(self):
        super().__init__('anomaly_detector')
        self.sub = self.create_subscription(
            Imu, 'imu/data', self.callback, 10)
        self.anomaly_count = 0
        self.get_logger().info('Anomaly Detector started')

    def callback(self, msg):
        az = msg.linear_acceleration.z
        magnitude = math.sqrt(
            msg.linear_acceleration.x**2 +
            msg.linear_acceleration.y**2 +
            az**2
        )
        if magnitude > THRESHOLD:
            self.anomaly_count += 1
            self.get_logger().error(
                f'ANOMALY #{self.anomaly_count} detected! '
                f'|a| = {magnitude:.2f} m/s^2'
            )

def main(args=None):
    rclpy.init(args=args)
    node = AnomalyDetector()
    rclpy.spin(node)
    rclpy.shutdown()
