from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='imu_monitor',
            executable='imu_publisher',
            name='imu_publisher',
            output='screen'
        ),
        Node(
            package='imu_monitor',
            executable='anomaly_detector',
            name='anomaly_detector',
            output='screen'
        ),
    ])
