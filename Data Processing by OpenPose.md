Data Processing by OpenPose
==========================

## Contents
1. [Prerequisites](#prerequisites)
2. [Install and Build](#install-build)
3. [Run OpenPose](#run)

## Prerequisites
After you clone [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose/) and before building OpenPose, make sure you have the prerequisites listed on this page: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/prerequisites.md#mac-os-prerequisites
As a Mac user, here're the prerequisite that I had to install:
1. Install CMake GUI: Run the command ```brew cask install cmake```
2. Install Caffe, OpenCV, and Caffe prerequisite using the file in OpenPose package: Run ```bash scripts/osx/install_deps.sh```
3. Install protobuf: Run ```brew install protobuf```
If you have installed it in conda, uninstall it by ```conda uninstall libprotobuf```
Check your version: Run ```protoc --version```
My version is libprotoc 3.10.0

Possible Error:
```No download info given for 'openpose_caffe' and its source directory:```
The solution is to manually clone caffe into folder:
```cd 3rdparty```
```git clone https://github.com/CMU-Perceptual-Computing-Lab/caffe/tree/b5ede488952e40861e84e51a9f9fd8fe2395cc8a```
Now, run cmake gui to Configure and Generate.

Note that Caffe auto build is incompatible with Anaconda, need to uninstall caffe and then build.

## Install and Build
Follow the installation instructions here: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md#installation

## Run OpenPose
1. To run on webcam and showing real-time detection in a GUI, use: ```./build/examples/openpose/openpose.bin --number_people_max 1 --face```
2. To process a video and write the output into JSON without invoking the GUI, run: ```./build/examples/openpose/openpose.bin --video /path_to_video/video.mp4 --face --number_people_max 1 --write_json ./output/ --display 0```
