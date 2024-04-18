import Jetson.GPIO as GPIO
pin = 33
freq = 100

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, freq)

pwm.start(0)
try:
        while True:
                pwm.ChangeDutyCycle(25)

except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
        