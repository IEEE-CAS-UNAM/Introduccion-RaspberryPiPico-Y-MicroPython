import serial, time

ser = serial.Serial('COM4',9600)

time.sleep(2)

encendido = 'a\n\r'

ser.write(encendido.encode('ascii'))

ser.close()

