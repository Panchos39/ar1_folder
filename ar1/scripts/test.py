import serial

ser = serial.Serial('/dev/ttyACM0')

ser.write("780A")