#!/bin/sh
sudo apt-get update # update just in case
sudo apt-get install libzbar-dev libopencv-dev libjpeg-dev python-dev doxygen swig # get dependencies for libwallaby
git clone https://github.com/kipr/libwallaby.git
cd libwallaby
mkdir build
cd build
cmake ..
make
sudo make install
export PATH=$PATH:.