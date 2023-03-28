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
  "t_sleeves": "long-sleeves",
  "t_texture": "normal",
  "t_button": "none",
  "t_length": "medium",
  "t_fit": "slim",
  "t_collar": "round-neck",
  "b_color" : "black",
  "b_pattern": "plain",
  "b_gender": "woman",
  "b_season": "spring",
  "b_length": "long",
  "b_type": "pants",
  "b_legpose": "standing",
  "gender": "woman",
  "glasses": "sun-glasses",
  "style": "casual"
}
```

#### ``/aai4r/fashion/monitor`` ([sensor_msgs/Image](https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Image.msg))


This topic publishes an image containing visualizations of the recognitions predicted by ``fashion_docker``.

## Clothing multi-attributes definition

<span class="c9"></span>

<a id="t.a6c6345e9a73b3ad660c800fb95cf5cfd611401e"></a><a id="t.0"></a>

<table class="c11">

<tbody>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">1</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">2</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">3</span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0">4</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">5</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">6</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">7</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">8</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">9</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">10</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">11</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">12</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">13</span>

</td>

</tr>

<tr class="c10">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">GT values</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">Top color(14)</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">Top pattern(6)</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">Top gender(2)</span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0">Top season(4)</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">Top type(7)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Top sleeves(3)</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">Bottom color(14)</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">Bottom pattern(6)</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">Bottom gender(2)</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">Bottom season(4)</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">Bottom length(2)</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">Bottom type(2)</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">leg pose(3)</span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">0</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">null</span>

</td>

</tr>

<tr class="c10">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">1</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">white</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">plain</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">man</span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0">spring</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">shirt</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">short sleeves</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">white</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">plain</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">man</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">spring</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">short pants</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">pants</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">standing</span>

</td>

</tr>

<tr class="c10">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">2</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">black</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">checker</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">woman</span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0">summer</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">jumper</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">long sleeves</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">black</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">checker</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">woman</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">summer</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">long pants</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">skirt</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">sitting</span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">3</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">gray</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">dotted</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0">autunm</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">jacket</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">no sleeves</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">gray</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">dotted</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">autunm</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">lying</span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">4</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">pink</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">floral</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0">winter</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">vest</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">pink</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">floral</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">winter</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">5</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">red</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">striped</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">parka</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">red</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">striped</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">6</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">green</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0">mixed</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">coat</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">green</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0">mixed</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">7</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">blue</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">dress</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">blue</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">8</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">brown</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">brown</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">9</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">navy</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">navy</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">10</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">beige</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">beige</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">11</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">yellow</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">yellow</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">12</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">purple</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">purple</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">13</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">orange</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">orange</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

<tr class="c8">

<td class="c2" colspan="1" rowspan="1">

<span class="c0">14</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">mixed</span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c5" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0">mixed</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c1" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c0"></span>

</td>

</tr>

</tbody>

</table>

<span class="c9"></span>	
