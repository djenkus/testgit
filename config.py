
#!/usr/bin/env python


import os
import sys
import os.path as path
import configparser

# read config file
config = configparser.ConfigParser()
#CONFIG_INI_PATH = os.path.abspath + "/config.ini"
CONFIG_INI_PATH = os.path.abspath(os.path.join(__file__, "../")) + "/config.ini"
print(CONFIG_INI_PATH)

config.read(CONFIG_INI_PATH)
# identify user's device
RTM_DEVICE = config['USER']['DEVICE']
# set device directory
if RTM_DEVICE == "KALEAO":
	RTM_DEVICE_DIR = config['KALEAO']['DEVICE_DIR']
elif RTM_DEVICE == "ODROID":
	RTM_DEVICE_DIR = config['ODROID']['DEVICE_DIR']	

dev_module_path = os.path.abspath(os.path.join(__file__,"../")) + RTM_DEVICE_DIR
print("dev = {}".format(dev_module_path))

# import device-specific modules
sys.path.insert(0, dev_module_path)

from current_sensor import *
from freqScaling import *


if __name__ == '__main__':
	
	print("RTM DEVICE = {}".format(RTM_DEVICE))
	print("RTM DEVICE DIR = {}".format(RTM_DEVICE_DIR))

