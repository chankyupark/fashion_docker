#!/usr/bin/bash
source "/opt/ros/$ROS_DISTRO/setup.bash"
source /aai4r/install/setup.bash
export PYTHONPATH=/aai4r/fashion_att_pkg/:$PYTHONPATH
export PYTHONPATH=/aai4r/fashion_att_pkg/fashion_attribute:$PYTHONPATH
export ROS2_SRC=/aai4r
ros2 run fashion_att_pkg fashion_attribute