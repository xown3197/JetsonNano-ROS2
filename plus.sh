#! /bin/bash

## VSCODE
git clone https://github.com/JetsonHacksNano/installVSCode.git & cd installVSCode
sh ./installVSCode.sh

cd .. & rm -r installVSCode

# [Jeton Nano] cv_bridge 에러 이슈
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1
echo “export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1” >> ~/.bashrc
source ~/.bashrc

# Vision task messages package 
sudo apt install ros-foxy-vision-msgs