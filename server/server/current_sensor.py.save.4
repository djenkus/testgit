



#!/usr/bin/env python
import  serial 
import sys
import subprocess
import os
import time


FAN_SPEED = 180

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

def get_power():


	# set cooler fan speed settings
	set_fan(mode="manual", speed = FAN_SPEED)


	try:
		port = serial.Serial("/dev/ttyUSB0", baudrate=115200)
	except:
		print("PACL: ttyUSB0 was not found!")
		try:
			print("Trying ttyUSB1..")
			port = serial.Serial("/dev/ttyUSB1", baudrate=115200)
		except:
			print("PACL: ttyUSB1 was not found!")
			try:
				print("Trying ttyUSB2..")
				port = serial.Serial("/dev/ttyUSB2", baudrate=115200)	
			except:
				print("PACL: ttyUSB2 was not found!")
				sys.exit()
       	meterData = port.read(23)
	tmpData = meterData.split(',')
	power = tmpData[2]

	port.close
	if power:
		return float(power)

def main():

	pwr = get_power()
	print(pwr)

if __name__ == '__main__':
	main()

