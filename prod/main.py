# coding:utf-8
import RPi.GPIO as GPIO
import time
import bridgeMotor as Motor

leSensor = 5
reSensor = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(leSensor, GPIO.IN)
GPIO.setup(reSensor, GPIO.IN)

if __name__ == '__main__':
    try:
        while True:
            
            le = GPIO.input(leSensor)
            re = GPIO.input(reSensor)
            print("esq = ", le, "dir = ", re)

            Motor.setMotorMode(1, 100)
            if (le == 0 and re == 1):
                Motor.setMotorMode(5, 100)
                le = GPIO.input(leSensor)
                re = GPIO.input(reSensor)


            if (re == 0 and le == 1):
                Motor.setMotorMode(4, 100)
                le = GPIO.input(leSensor)
                re = GPIO.input(reSensor)


    except KeyboardInterrupt:
        Motor.setMotorMode(3, 0)
        print("Stooped by user")
        
