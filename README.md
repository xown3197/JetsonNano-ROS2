# JetsonNano-ROS2

### ROS2 설치
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

### test Real-time Detection 
```
$ source /opt/ros/foxy/setup.bash
$ colcon build
$ ./install/local_setup.bash
```

termainal 1
```
ros2 run image_tools cam2images
```

terminal 2
```
ros2 run live_detection live_detector
```