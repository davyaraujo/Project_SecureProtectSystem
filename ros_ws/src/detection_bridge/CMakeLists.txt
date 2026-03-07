cmake_minimum_required(VERSION 3.0.2)
project(detection_bridge)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/detection_subscriber.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)