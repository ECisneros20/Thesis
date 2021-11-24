# Thesis

## Description
It contains the simulations of the mobile robot developed in my thesis. It uses the world from [1].

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

This second line will initiate RVIZ with the previous configuration. By default, LaserScan, PointCloud2 and IMU are not working in RVIZ.

## References

[1] https://github.com/LTU-RAI/gazebo_cave_world/tree/master#readme
	
