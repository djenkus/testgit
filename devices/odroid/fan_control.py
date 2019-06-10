#!/usr/bin/env python
import  serial 
import sys
import subprocess
import os
import time



cmd_set_mode = "echo  | sudo tee /sys/devices/platform/pwm-fan/hwmon/hwmon0/automatic"
cmd_set_speed = "echo  | sudo tee /sys/devices/platform/pwm-fan/hwmon/hwmon0/pwm1 "


def set_fan(**settings):


	if settings['mode'] == "manual":
		cmd_manual = cmd_set_mode[:5] + str(0) + cmd_set_mode[5:]
		cmd_speed = cmd_set_speed[:5] + str(settings['speed']) + cmd_set_speed[5:]
		subprocess.call(cmd_manual, shell = True)
		subprocess.call(cmd_speed, shell = True)

	elif settings['mode'] == "auto":
		cmd_mode = cmd_set_mode[:5] + str(1) + cmd_set_mode[5:]
		subprocess.call(cmd_mode, shell = True)

