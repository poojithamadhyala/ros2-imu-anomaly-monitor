# ROS2 IMU Anomaly Monitor

Real-time IMU sensor fault detection pipeline built with ROS2 Humble — directly relevant to autonomous vehicle test engineering.

## Demo
![IMU Anomaly Detection](imu_plot.png)

## What it does
Publishes simulated IMU data at 10Hz, detects acceleration anomalies in real time, and records rosbag artifacts for post-session analysis — mirroring AV sensor validation workflows.

## Stack
- ROS2 Humble (Dockerized)
- Python, rclpy, sensor_msgs/Imu
- rosbag2 — 3,188 messages recorded on /imu/data
- matplotlib — live sensor stream visualization
- Docker — single-command reproducible environment

## Nodes
| Node | Topic | Role |
|------|-------|------|
| `imu_publisher` | `/imu/data` | Publishes sensor_msgs/Imu at 10Hz |
| `anomaly_detector` | `/imu/data` | Flags readings where |a| > 12 m/s² |

## Run
```bash
docker pull osrf/ros:humble-desktop
docker run -it -v $(pwd):/ros2_ws osrf/ros:humble-desktop bash
source /opt/ros/humble/setup.bash && cd /ros2_ws
colcon build --packages-select imu_monitor
source install/setup.bash
ros2 launch imu_monitor imu_monitor.launch.py
```
