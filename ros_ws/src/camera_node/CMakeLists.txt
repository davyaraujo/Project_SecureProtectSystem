cmake_minimum_required(VERSION 3.0.2)
project(camera_node)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/camera_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)