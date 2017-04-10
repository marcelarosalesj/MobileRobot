#!/bin/sh
# launcher.sh
# navigate home dir, then this dir, then execute my python script, then back home

cd /
cd home/pi/Repos/rpi-demos/launchOnStartup
sudo python launchOnStartup.py
cd /
