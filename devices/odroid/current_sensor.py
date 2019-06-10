


import sys
import os
import subprocess
import serial



try:
	ser = serial.Serial('/dev/ttyUSB0', 115200)
except:
	try:
		ser = serial.Serial('/dev/ttyUSB1',115200)
	except:
		try:
			ser = serial.Serial('/dev/ttyUSB2',115200)
		except:
			print("PACL: could not open current sensor port!")
			sys.exit()

# read sensor

def get_sensor():

	tmp = ser.readline()

	if tmp:
	#	print(tmp)
		readings = tmp.split(',')
	else:
		print("PACL: Sensor data was not obtained")
		sys.exit()

	# close serial connection
	#ser.close()

	return readings


def get_power():
	power = get_sensor()
	return power[2]

def get_current():
	current = get_sensor()
	return current[1]


def main():

	while True:
		pwr = get_sensor()
		print("Power = {} " .format(pwr[2]))
		print("Current = {}".format(pwr[1]))


if __name__ == '__main__':
	main()
