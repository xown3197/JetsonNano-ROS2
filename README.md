# JetsonNano-ROS2

## ROS2 설치
<details>
<summary> 설치 방법 </summary>
<div markdown="1">

```
$ sh ./install_ros2_jetson_nano.sh
$ sh ./plus.sh
```

### SD 카드 파티션 늘리는 방법

[참고 사이트](https://omorobot.gitbook.io/manual/product/omo-r1mini/r1mini-pro/jetson-nano)
```
$ sudo apt update
$ sudo apt install -y gparted
$ sudo gparted
```
</div>
</details>

-----

## Real-time Detection 

```
$ source /opt/ros/foxy/setup.bash
$ colcon build
$ source ./install/local_setup.bash
```

termainal 1
```
$ ros2 run image_tools cam2image
```

terminal 2
```
$ ros2 run live_detection live_detector

# (option)
$ ros2 run live_detection live_detector -P {ckpt_path}
or
$ ros2 run live_detection live_detector --ckpt-path {ckpt_path}
```
