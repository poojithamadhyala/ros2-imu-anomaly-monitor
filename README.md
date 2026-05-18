# ROS2 IMU Anomaly Monitor

Real-time sensor fault detection on live IMU streams — built to mirror autonomous vehicle test engineering workflows.

![IMU Anomaly Detection](imu_plot.png)

---

## What's happening in that plot?

A ROS2 pipeline publishes simulated IMU data at **10Hz** on `/imu/data`. A subscriber node watches every reading in real time — the moment acceleration magnitude exceeds **12 m/s²**, it flags a fault, logs it with a timestamp, and marks it on the stream.

This is exactly what AV test engineers do: instrument a vehicle, stream sensor data over ROS topics, and catch anomalies before they reach production.

---

## Stack

| Layer | Tools |
|-------|-------|
| Robotics Middleware | ROS2 Humble, rclpy, sensor_msgs |
| Data Recording | rosbag2 — 3,188 msgs @ 10Hz on `/imu/data` |
| Visualization | matplotlib — live stream + anomaly markers |
| Deployment | Docker — single-command reproducible environment |
| Language | Python 3 |

---

## Architecture
imu_publisher node                anomaly_detector node
──────────────────                ─────────────────────
Publishes sensor_msgs/Imu   ───►  Subscribes to /imu/data
@ 10Hz with random fault          Computes |a| = sqrt(ax2+ay2+az2)
injection (~2% spike rate)        Flags if |a| > 12 m/s2
Logs fault count + magnitude

---

## Nodes

| Node | Topic | Type | Role |
|------|-------|------|------|
| `imu_publisher` | `/imu/data` | `sensor_msgs/Imu` | Simulates 10Hz IMU stream with fault injection |
| `anomaly_detector` | `/imu/data` | `sensor_msgs/Imu` | Real-time fault detection with threshold logic |

---

## Run

```bash
docker pull osrf/ros:humble-desktop

docker run -it --rm \
  -v $(pwd):/ros2_ws \
  osrf/ros:humble-desktop bash

source /opt/ros/humble/setup.bash
cd /ros2_ws
colcon build --packages-select imu_monitor
source install/setup.bash
ros2 launch imu_monitor imu_monitor.launch.py
```

---

## Record and Replay

```bash
ros2 bag record -o imu_session /imu/data
ros2 bag info imu_session
ros2 bag play imu_session
```

---

## Generate Visualization

```bash
python3 plot_imu.py
# Saves imu_plot.png — 300 samples with anomalies marked in red
```

---

## Related Projects

- [AI-Driven MLOps Pipeline](https://github.com/poojithamadhyala) — real-time anomaly detection on industrial sensor streams  
- [Pothole Detection AI](https://github.com/poojithamadhyala) — YOLOv8 edge inference at 41ms CPU latency

---

*Built as part of an AV test engineering portfolio — targeting autonomous vehicle sensor validation roles.*
