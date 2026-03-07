FROM ros:noetic-ros-base

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-opencv \
    ros-noetic-cv-bridge \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests ultralytics

WORKDIR /ros_ws

COPY . .

RUN /bin/bash -c "source /opt/ros/noetic/setup.bash && catkin_make"

CMD ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source devel/setup.bash && roslaunch camera_node camera.launch"]