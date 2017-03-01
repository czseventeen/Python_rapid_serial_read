# Python_rapid_serial_read
This is used to constantly read the Efuse I_out value via serial, and eventually output what was the max value read over time

To start, run the script by doing "python read_switch_power.py" in windows command prompt
Make sure that you install pyserial using "pip install pyserial"

Then you will be asked to input the serial port, just need to input the number.
The program will start to loop and read the efuse Iout until Ctrl+C is hit. 
