**gripper-rollpawkit** - integration of `Standard Gripper Kit Paw for Robotic Arm Rollarm DIY Robot` with ROS (Robot Operating System)

This is a ROS package which provides an URDF model of the gripper.

This is not 1:1 mapping which means some elements from the gripper parts (like screw holes etc.) are not present. It is done to reduce model complexity for faster simulations.

# Hardware

[Standard Gripper Kit Paw for Robotic Arm Rollarm DIY Robot](https://www.sunfounder.com/products/standard-gripper-kit)

# Prereq

- ROS2

Install dependencies:

``` bash
apt install -y ros-humble-joint-state-publisher-gui
```

# Build

``` bash
mkdir -p gripper_ws/src
cd gripper_ws
colcon build
```

# Run

``` bash
source install/setup.zsh
ros2 launch gripper-rollpawkit simulate_launch.py
```

# Demonstration video

[![Demo](demo/gripper-in-rviz.png)](demo/gripper-in-rviz.mp4)

# Download

You can download from <https://github.com/pinorobotics/gripper-rollpawkit>

# Documentation

Documentation available here <http://pinorobotics.atwebpages.com/>

# Contributors

aeon_flux <aeon_flux@eclipso.ch>
