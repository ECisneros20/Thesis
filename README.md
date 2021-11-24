# Thesis

## Description

This repository contains the simulations of the mobile robot developed in my thesis. It uses the world from [1].

## Installation

Clone the package into your workspace:

	https://github.com/ECisneros20/Thesis.git

Also, in order to get the world to simulate, you have to clone this package:

	https://github.com/LTU-RAI/gazebo_cave_world.git

This map was based on the DARPA Subterranean Challenge

## Usage

First, you have to load the world:

	roslaunch gazebo_cave_world cave_world.launch

Then, spawn the robot:

	roslaunch thesis_description spawn_robot.launch

This second line will initiate RVIZ with the previous configuration. By default, LaserScan, PointCloud2 and IMU are not enabled in RVIZ in order to slow down any computer.

## Next steps

*Implement Hector SLAM with IMU information
*Implement Global and Local planners
*Inclue FlexBE state machines: http://wiki.ros.org/flexbe/Tutorials/Using%20the%20Statemachine%20Editor

## License

MIT License

## References

[1] https://github.com/LTU-RAI/gazebo_cave_world/tree/master#readme
	
