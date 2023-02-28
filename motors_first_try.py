import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
class Robot():

 def __init__(self, *args, **kwargs):
  super(Robot, self).__init__(*args, **kwargs)
  self.left_motor = [35,36]
  self.right_motor = [37,38]
  self.left_speed = 0
  self.right_speed = 0
  GPIO.setup(32,GPIO.OUT)                                         #This is the PWM signal, setting up that pin as output
  GPIO.setup(33,GPIO.OUT)                                         #This is the PWM signal, setting up that pin as output
  self.pwm=[GPIO.PWM(32,50),GPIO.PWM(33,50)]                      #50 Hz PWM signal on that GPIO pin using the GPIO.PWM() function
  GPIO.setup(self.left_motor[0],GPIO.OUT,initial=GPIO.LOW)        #This is left motor forward
  GPIO.setup(self.right_motor[0],GPIO.OUT,initial=GPIO.LOW)       #This is right motor forward
  GPIO.setup(self.left_motor[1],GPIO.OUT,initial=GPIO.LOW)        #This is left motor backward
  GPIO.setup(self.right_motor[1],GPIO.OUT,initial=GPIO.LOW)       #This is right motor backward
  self.pwm[0].start(0)                                            #PWM signal for left motor
  self.pwm[1].start(0)                                            #PWM signal for right motor
  
def set_motors(self, left_speed=1.0, right_speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.HIGH)
  GPIO.output(self.right_motor[0],GPIO.HIGH) 
  self.left_speed = ((left_speed - (-1))/2)*100
  self.right_speed = ((right_speed - (-1))/2)*100
  print()
  print()
  self.pwm[0].ChangeDutyCycle(self.left_speed)
  self.pwm[1].ChangeDutyCycle(self.right_speed)
    
def forward(self, speed=1.0, duration=None):
  GPIO.output(self.left_motor[0],GPIO.HIGH)
  GPIO.output(self.right_motor[0],GPIO.HIGH) 
  GPIO.output(self.left_motor[1],GPIO.LOW)
  GPIO.output(self.right_motor[1],GPIO.LOW) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  
def backward(self, speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.LOW)
  GPIO.output(self.right_motor[0],GPIO.LOW) 
  GPIO.output(self.left_motor[1],GPIO.HIGH)
  GPIO.output(self.right_motor[1],GPIO.HIGH) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  
def left(self, speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.LOW)
  GPIO.output(self.right_motor[0],GPIO.HIGH) 
  GPIO.output(self.left_motor[1],GPIO.HIGH)
  GPIO.output(self.right_motor[1],GPIO.LOW) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  
def right(self, speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.HIGH)
  GPIO.output(self.right_motor[0],GPIO.LOW) 
  GPIO.output(self.left_motor[1],GPIO.LOW)
  GPIO.output(self.right_motor[1],GPIO.HIGH) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  
def stop(self):
  GPIO.output(self.left_motor[0],GPIO.LOW)
  GPIO.output(self.right_motor[0],GPIO.LOW) 
  GPIO.output(self.left_motor[1],GPIO.LOW)
  GPIO.output(self.right_motor[1],GPIO.LOW) 
  self.left_speed = 0
  self.right_speed = 0
  self.pwm[0].ChangeDutyCycle(self.left_speed)
  self.pwm[1].ChangeDutyCycle(self.right_speed)
  
  def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)
