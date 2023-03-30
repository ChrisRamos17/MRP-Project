int motorPinsLeft[6] = {13, 12, 11, 10, 9, 8};  //Pins for left motor
int motorPinsRight[6] = {7, 6, 5, 4, 3, 2};  //Pins for right motor

int maxSpeed = 255;  //Max bits, representing x00ff
int leftSpeed, rightSpeed;
int theSpeed, theTurn;
int theTorque = 1.0625;  //Convertion of how many bits will result in 1rpm

void setup() {
  // put your setup code here, to run once:  Setting everything as output
  for (int i = 0; i < 6; i++) {
    pinMode (motorPinsLeft[i], OUTPUT);
    pinMode (motorPinsRight[i], OUTPUT);
  }
Serial.begin(9600);  //Baud rate selected
}

void moveRobot(float theSpeed, float theTurn, int t = 0)  { 
  //Disered speed, turn and duration t
  theSpeed *= maxSpeed;  //The per unit speed provided times the maximum bits, to see how many bits it corresponds to
  theTurn *= maxSpeed;  //The per unit turn provided times the maximum bits, to see how many bits it corresponds to
  theTorque *= theSpeed;  //Math conversion of the bits to rpm for the motors

  // Individual Speeds
  leftSpeed = int(theSpeed - theTurn);  //If my turn is positive it will turn to the left by making left motors slower and right motors faster
  rightSpeed = int(theSpeed + theTurn); //If my turn is negative it will turn to the right by making left motors faster and right motors slower

  // Limit
  leftSpeed = constrain(leftSpeed, -maxSpeed, maxSpeed);  //Constrain the values to not surpass -255 to 255. As that is 100%
  rightSpeed = constrain(rightSpeed, -maxSpeed, maxSpeed);  //In case if someone enters more than 1.0 to mySpeed or myTurn

  // Send Speed
  analogWrite(motorPinsLeft[0], abs(leftSpeed));  //Pin 7
  analogWrite(motorPinsLeft[5], abs(leftSpeed));  //Pin 2
  analogWrite(motorPinsRight[0], abs(rightSpeed));  //Pin 13
  analogWrite(motorPinsRight[5], abs(rightSpeed));  //Pin 8
  //char buffer[40];
  //sprintf(buffer, "Speed for the left motors is %d ", leftSpeed");
  //Serial.printls(buffer);
  //
  Serial.println("Speed for the left motors");
  Serial.println(leftSpeed);
  Serial.println("Speed for the right motors");
  Serial.println(rightSpeed);
  Serial.println("Speed for the left motors");
  Serial.println(theTorque);

  if (leftSpeed > 0)  {                 //Forward Left
    digitalWrite(motorPinsLeft[1], 1);  //Pin 6, int1
    digitalWrite(motorPinsLeft[2], 0);  //Pin 5, int2
    digitalWrite(motorPinsLeft[3], 1);  //Pin 4, int4
    digitalWrite(motorPinsLeft[4], 0);  //Pin 3, int3
    Serial.println("Forward Left");
    
  }
  else {                                //Backward Left
    digitalWrite(motorPinsLeft[1], 0);
    digitalWrite(motorPinsLeft[2], 1);
    digitalWrite(motorPinsLeft[3], 0);
    digitalWrite(motorPinsLeft[4], 1);
    Serial.println("Backward Left");
  }

  if (rightSpeed > 0)  {                 //Forward Right
    digitalWrite(motorPinsRight[1], 1);  //Pin 12, int1
    digitalWrite(motorPinsRight[2], 0);  //Pin 11, int2
    digitalWrite(motorPinsRight[3], 0);  //Pin 10, int4
    digitalWrite(motorPinsRight[4], 1);  //Pin 9, int3
    Serial.println("Forward Right");
  }
  else {                                 //Backwars Right
    digitalWrite(motorPinsRight[1], 0);
    digitalWrite(motorPinsRight[2], 1);
    digitalWrite(motorPinsRight[3], 1);
    digitalWrite(motorPinsRight[4], 0);  
    Serial.println("Backward Right");  
  }
   delay(2000);  //Time it will take in this action
// delay(t);   
} 

void loop() {
  // put your main code here, to run repeatedly:
  moveRobot(0,0,2000);               //Inputted to gradually increase speed and then decrease it
  moveRobot(0.2,0,2000);             //With no turn and a 2 seconds wait in each action
  moveRobot(0.4,0,2000);
  moveRobot(0.5,0,2000);
  moveRobot(0.6,0,2000);
  moveRobot(0.7,0,2000);
  moveRobot(0.8,0,2000);
  moveRobot(0.9,0,2000);
  moveRobot(1,0,2000);               //Max speed
  moveRobot(0.9,0,2000);
  moveRobot(0.8,0,2000);
  moveRobot(0.7,0,2000);
  moveRobot(0.6,0,2000);
  moveRobot(0.4,0,2000);
  moveRobot(0.2,0,2000);
  moveRobot(0,0,2000);               //Until here
  moveRobot(0,0.3,2000);             //The impact of a turn to the left
  moveRobot(0,0.5,2000);
  moveRobot(0,0.3,2000);
  moveRobot(0,0,2000);               //Until here
  moveRobot(0,-0.3,2000);            //The impact of a turn to the right
  moveRobot(0,-0.5,2000);
  moveRobot(0,-0.3,2000);
  
}

//Testing and troubleshooting

//  void moveRobot(int theSpeed)  {

    
//     // digitalWrite(motorPinsRight[4],1);
//     // digitalWrite(motorPinsRight[3],0);
//     // analogWrite(motorPinsRight[5], abs(theSpeed));
//     // digitalWrite(motorPinsRight[2],0);                   // 2,  1, 0
//     // digitalWrite(motorPinsRight[1],1);
//     // analogWrite(motorPinsRight[0], abs(theSpeed));

//     digitalWrite(motorPinsLeft[4], 1);  //Pin 6, int1
//     digitalWrite(motorPinsLeft[3], 0);  //Pin 5, int2
//     analogWrite(motorPinsLeft[5], abs(theSpeed));
//     digitalWrite(motorPinsLeft[2], 1);  //Pin 6, int1
//     digitalWrite(motorPinsLeft[1], 0);  //Pin 5, int2
//     analogWrite(motorPinsLeft[0], abs(theSpeed));
//     delay(2000);
//   }


//     // digitalWrite(motorPinsLeft[4],1);
//     // digitalWrite(motorPinsLeft[3],0);
//     // analogWrite(motorPinsLeft[5], abs(theSpeed));
//     // digitalWrite(motorPinsLeft[2],1);
//     // digitalWrite(motorPinsLeft[1],0);
//     // analogWrite(motorPinsLeft[0], abs(theSpeed));
 

//  void loop() {
//     // put your main code here, to run repeatedly:
//     moveRobot(200);
//     delay(2000);
//     moveRobot(100);
//     delay(2000);
//     moveRobot(0);
//     delay(2000);
//     moveRobot(100);
//     delay(2000);
// }
