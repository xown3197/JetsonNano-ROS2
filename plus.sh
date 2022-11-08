#! /bin/bash

# [Jeton Nano] cv_bridge 에러 이슈
echo “export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1” >> ~/.bashrc
source ~/.bashrc

# Vision task messages package 
sudo apt install ros-foxy-vision-msgs