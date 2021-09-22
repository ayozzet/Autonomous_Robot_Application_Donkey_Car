import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def kanan():
	kit.servo[1].angle = 50 #kanan max 50
	#kit.continuous_servo[0].throttle = 0
	time.sleep(2)

def kiri():
	kit.servo[1].angle = 150 #kiri max 150
	#kit.continuous_servo[0].throttle = 0
	time.sleep(2)

def tengah():
    kit.servo[1].angle = 90
    #kit.continuous_servo[0].throttle = 0
    time.sleep(2)

while True:
    kanan()
	tengah()
    kiri()
	tengah()
