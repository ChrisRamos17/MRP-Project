import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Robot():	
 def __init__(self, *args, **kwargs):
  self.left_motor = [35,36]						                                   #Nvidia pins for left motor {OUT 1, OUT 2}
  self.right_motor = [37,38]						                                  #Nvidia pins for right motor {OUT 3, OUT 4}
  self.left_speed = 0							                                        #Initial values
  self.right_speed = 0
  self.speed = 0
  GPIO.setup(32,GPIO.OUT)						                                     #Setting pins as outputs
  GPIO.setup(33,GPIO.OUT) 						                                    #For PWM [32, 33]
  self.pwm=[GPIO.PWM(32,1000),GPIO.PWM(33,1000)] 			                #1000 Hz pwm signal
  GPIO.setup(self.left_motor[0],GPIO.OUT,initial=GPIO.LOW)		        #This is left motor foward {35} OFF
  GPIO.setup(self.right_motor[0],GPIO.OUT,initial=GPIO.LOW) 	      	#This is right motor foward {37} OFF
  GPIO.setup(self.left_motor[1],GPIO.OUT,initial=GPIO.LOW)	        	#This is left motor backward {36} OFF
  GPIO.setup(self.right_motor[1],GPIO.OUT,initial=GPIO.LOW)       		#This is right motor backward {38} OFF
  self.pwm[0].start(0)
  self.pwm[1].start(0)
    
 def forward(self, speed):						                                    #Foward
  GPIO.output(self.left_motor[0],GPIO.HIGH)				                     #This is left motor foward {35}
  GPIO.output(self.right_motor[0],GPIO.HIGH) 			                   	#This is right motor foward {37}
  GPIO.output(self.left_motor[1],GPIO.LOW)				
  GPIO.output(self.right_motor[1],GPIO.LOW) 				
  self.speed = speed*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  print("forward")
  print(self.speed)

 def backward(self, speed):						                                   #Backward
  GPIO.output(self.left_motor[0],GPIO.LOW)				
  GPIO.output(self.right_motor[0],GPIO.LOW) 				
  GPIO.output(self.left_motor[1],GPIO.HIGH)			                    	 #This is left motor backward {36}
  GPIO.output(self.right_motor[1],GPIO.HIGH)				                    #This is right motor backward {38}
  self.speed = speed*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  print("backward")
  print(self.speed)

 def left(self, speed):							                                      #Left
  GPIO.output(self.left_motor[0],GPIO.LOW)				
  GPIO.output(self.right_motor[0],GPIO.HIGH) 			                    #This is right motor foward {37}
  GPIO.output(self.left_motor[1],GPIO.HIGH)				                     #This is left motor backward {36}
  GPIO.output(self.right_motor[1],GPIO.LOW) 				
  self.speed = speed*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  print("left")

 def right(self, speed):					                                       #Right
  GPIO.output(self.left_motor[0],GPIO.HIGH)			                     	#This is left motor foward {35}
  GPIO.output(self.right_motor[0],GPIO.LOW) 				
  GPIO.output(self.left_motor[1],GPIO.LOW)				
  GPIO.output(self.right_motor[1],GPIO.HIGH) 				                   #This is right motor backward {38}
  self.speed = speed*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
  print("right")

 def stop(self):							                                             #Stop
  GPIO.output(self.left_motor[0],GPIO.LOW)				                      #This is left motor foward {35} OFF
  GPIO.output(self.right_motor[0],GPIO.LOW) 			                    	#This is right motor foward {37} OFF
  GPIO.output(self.left_motor[1],GPIO.LOW)				                      #This is left motor backward {36} OFF
  GPIO.output(self.right_motor[1],GPIO.LOW) 		                    		#This is rightt motor backward {38} OFF
  self.left_speed = 0
  self.right_speed = 0
  self.pwm[0].ChangeDutyCycle(0)
  self.pwm[1].ChangeDutyCycle(0)
  print("stop")


if __name__ == "__main__":				                                    		#Main program to call all the functions
    robot = Robot()							                                          #Having the class as a variable
    robot.forward(speed=1)						                                    #This is 100% of duty cycle
    time.sleep(3)							                                            #Run this cycle for 3 seconds
    robot.forward(speed=0.1)					                                  	#This is 100% of duty cycle
    time.sleep(3)
    robot.stop()
    time.sleep(3)
    robot.backward(speed=1)
    time.sleep(3)
    robot.backward(speed=0.2)
    time.sleep(3)
    robot.stop()
    time.sleep(3)
    GPIO.cleanup()
  
