# fashion_docker

## Introduction

Given a person-level ROI as input, ``face_docker`` can classify multiple attributes about the clothing and accessories a person is wearing.

This container interfaces with clients via ROS2 topics.

## Folders and Files

- ``fashion_att_pkg``: An implementation of a ROS2 node for ``fashion_docker``
- ``fashion2_aai4r.Dockerfile``: A dockerfile for creating a ``fashion_docker`` container image
- ``dockerbuild.sh``: A shell script for creating a container image with the ``fashion2_aai4r.Dockerfile`` and tagging it properly
- ``ros_entrypoint.sh``: An entrypoint shell script for the container
- ``run_colcon.sh``: A shell script to build the ROS2 node inside the container
- ``run_container.sh``: A shell script to create a container and execute
- ``run.sh``: A shell script to run the ROS2 node inside the container

## Instructions

To create a docker container:

```
dockerbuild.sh
```

To create and run a ``fashion_docker`` container:

```
run_container.sh
```

## ROS2 Interface

### Subscribed Topics

#### ``/camera/robot_image_info`` ([RobotImageInfo](https://github.com/aai4r/ai-containers/blob/main/aai4r_edge_interfaces/msg/RobotImageInfo.msg))


### Published Topics

#### ``/aai4r/fashion`` ([std_msgs/String](https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/String.msg))

This topic publishes a string which contains all the recognition results. The string is formatted in ``JSON`` and the content is structured as the following sample:

```json
{
  "id": 1, 
  "t_color": "green", 
  "t_pattern": "checker",
  "t_gender": "woman",
  "t_season": "spring",
  "t_type": "t-shirt",
  "t_sleeves": "long-sleeves"
  "t_texture": "normal"
  "t_button": "none"
  "t_length": "medium"
  "t_fit": "slim"
  "t_collar": "round-neck"
  "b_color" : "black"
  "b_pattern": "plain",
  "b_gender": "woman",
  "b_season": "spring",
  "b_length": "long"
  "b_type": "pants",
  "b_legpose": "standing"
  "gender": "woman"
  "glasses": "sun-glasses"
  "style": "casual"
}
```

#### ``/aai4r/fashion/monitor`` ([sensor_msgs/Image](https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Image.msg))


This topic publishes an image containing visualizations of the recognitions predicted by ``fashion_docker``.

