
import serial

port = serial.Serial("/dev/ttyUSB0", baudrate=115200)

#while True:
    #port.write("\r\nSay something:")
rcv = port.read(23)


power = rcv.split(',')
#port.close()
print(rcv)
print(power[2])
    #port.write("\r\nYou sent:" + repr(rcv))
