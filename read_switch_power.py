import serial
import time
import string

var="COM"
var += raw_input("Enter the COM port number: ")
ser = serial.Serial(var, 115200, timeout=0)
max_data=-999
max_hex=0
try:
	while 1:
		ser.write(b'i2c 40 8c 2\r')
		x=ser.readlines()
		length=len(x)
		while length < 1 :
			y=ser.readlines()
			if len(y) > 0:
			
				x=x+y
				length=length+ len(x)
			#print ('current length is'+str(length))
		#print ('data read was:'+str(x)+"!")
		try:
			dataline=x[1]
		except IndexError:
			print ("...")
			continue
			
		if ( len(dataline.split(" ")) > 4 ) :
			# split the data received and see if they are both a 2 bit hex number
			data0=dataline.split(" ")[2]
			data1=dataline.split(" ")[3]
			hex_data=data1+data0
			try:
				dec_data=int(hex_data, 16)
				print("the Iout value is:"+str(dec_data))
			except ValueError:
				print("---")
				continue
			if dec_data > max_data:
				max_data = dec_data
				max_hex=hex_data
			
		else:
			continue
except KeyboardInterrupt:
	power=0.0000124*(max_data-2048)*1000
	print ("The max value was:"+str(max_data)+"("+str(hex_data)+"), that current was:"+str(power))
	ser.close()