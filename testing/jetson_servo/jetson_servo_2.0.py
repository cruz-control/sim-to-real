from adafruit_servokit import ServoKit
kit = ServoKit(address=0x60, channels=16)
kit.servo[0].angle = 90
kit.servo[15].angle = 90