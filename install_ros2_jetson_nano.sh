#! /bin/bash

sudo apt update

sudo apt update && sudo apt install curl gnupg2 lsb-release -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key  -o /usr/share/keyrings/ros-archive-keyring.gpg

sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture)] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F42ED6FBAB17C654

sudo apt update

# Desktop Install (Recommended): ROS, RViz, demos, tutorials.
sudo apt install ros-foxy-desktop -y

# Install argcomplete (optional)
sudo apt install -y python3-pip
pip3 install -U argcomplete


# Install Gazeobo 
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update

$ sudo apt install gazebo11 libgazebo11-dev -y

# Gazebo ROS 패키지들도 설치해줍니다.
sudo apt install ros-foxy-gazebo-ros-pkgs -y

# Install Colcon Build system
sudo apt install python3-colcon-common-extensions