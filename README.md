# fashion_docker

## Introduction

Given a person-level ROI as input, ``face_docker`` can classify multiple attributes about the clothing and accessories a person is wearing.

This container interfaces with clients via ROS2 topics.

## Folders and Files

- ``loom-ros2``: An implementation of a ROS2 node for ``loom``
- ``loom_aai4r.Dockerfile``: A dockerfile for creating a ``loom`` container image
- ``dockerbuild_loom.sh``: A shell script for creating a container image with the ``loom_aai4r.Dockerfile`` and tagging it properly
- ``ros_entrypoint.sh``: An entrypoint shell script for the container
- ``run_colcon.sh``: A shell script to build the ROS2 node inside the container
- ``run_container_loom.sh``: A shell script to create a container and execute
- ``run_loom.sh``: A shell script to run the ROS2 node inside the container

## Instructions

To create a docker container:

```
dockerbuild_loom.sh
```

To create and run a ``loom`` container:

```
run_container_loom.sh
```

## ROS2 Interface

### Subscribed Topics

#### ``/camera/robot_image_info`` ([RobotImageInfo](https://github.com/aai4r/ai-containers/blob/main/aai4r_edge_interfaces/msg/RobotImageInfo.msg))

#### ``/aai4r/detrack`` ([std_msgs/String](https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/String.msg))

#### ``/aai4r/facial`` ([std_msgs/String](https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/String.msg))

#### ``/aai4r/meal`` ([std_msgs/String](https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/String.msg))

#### ``/aai4r/hhobjects`` ([std_msgs/String](https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/String.msg))


### Published Topics

#### ``/aai4r/situation`` ([std_msgs/String](https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/String.msg))

This topic publishes a string which contains all the detection and recognition results. The string is formatted in ``JSON`` and the content is structured as the following sample:

```json
{
  "domain": 1, 
  "robot_id": "robot01", 
  "robot_type": 1, 
  "zone": 2, 
  "time": "2021-05-16T23:07:42", 
  "distance": -1, 
  "situation": {}, 
  "group": {}, 
  "personal_context": [
    {"id": "2ae1090a-4f16-4843-9029-20e6641f0b61", "mask": 1, "has_cup": 1}, ...
  ],
  "meal_context": [
    {"category": "food", "name": "pasta", "amount": 0.2}, ...
  ]
}
```

#### ``/aai4r/loom/monitor`` ([sensor_msgs/Image](https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Image.msg))


This topic publishes an image containing visualizations of the detections and recognitions predicted by ``facial``.

