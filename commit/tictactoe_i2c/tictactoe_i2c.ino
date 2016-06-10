#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *gripper = AFMS.getMotor(1);
Adafruit_DCMotor *elbow = AFMS.getMotor(2);
Adafruit_DCMotor *shoulder = AFMS.getMotor(3);
Adafruit_DCMotor *base = AFMS.getMotor(4);

#define SLAVE_ADDRESS 0x04
int pos = 0;

void setup() {
AFMS.begin();
pinMode(A0,INPUT); //M3
pinMode(A1,INPUT); //M4
pinMode(A2,INPUT); //M5
pinMode(A3,INPUT); //M1(gripper)
Serial.begin(9600);

Wire.begin(SLAVE_ADDRESS);
Wire.onReceive(receiveData);
Wire.onRequest(sendData);

gripper->setSpeed(100);
base->setSpeed(150);
shoulder->setSpeed(100);
elbow->setSpeed(100);
gripper->run(FORWARD);
base->run(FORWARD);
shoulder->run(FORWARD);
elbow->run(FORWARD);
  // turn on motor
gripper->run(RELEASE);
base->run(RELEASE);
shoulder->run(RELEASE);
elbow->run(RELEASE);
delay(5000);
Serial.println("Base movement start");
basemovement(279,354,403,820);
Serial.println("Base movement ends");
delay(1000);
}

/*
________________
 3  |  6  |  9
___ | ___ | ___
 2  |  5  |  8
___ | ___ | ___
 1  |  4  |  7
___ | ___ | ___
      ARM    
________________

*/

/* 
pin connections:
motor M1: orange--> gnd; red-->vcc
motor M3: orange-->gnd ; yellow-green--> vcc
motor M4: orange-->gnd; black-->vcc
motor M5: purple-->gnd; green-->vcc
*/

//Shield configuration
/*
 * Motor M1 - Gripper:> Backward(IN), Forward(OUT)  yellow-->blue ---driver(M1)
 * Motor M2 - Fixed
 * Motor M3 - Elbow:> Backward(UP), Forward(DOWN)  blue-->green ---driver(M2)
 * Motor M4 - Shoulder:> Backward(DOWN) Forward(UP) orange-->black  ---driver(M3)
 * Motor M5 - Base:> Backward(Left) Forward(Right)  orange-->blue ---driver(M4) 
 */
//pickup value: M1-->820    M3-->354    M4-->403    M5-->279
//gripper holding value: M1-->820,801,841
//gripper releasing value: M1-->850
//zero position: M3-->325; M4-->511

//mapping for each position:
//pos1:M3-->354    M4-->399    M5-->328(left)-388(right)
//pos2:M3-->511    M4-->271    M5-->369(left)-413(right)
//pos3:M3-->706    M4-->153    M5-->396(left)-454(right)
//pos4:M3-->354    M4-->399    M5-->388(left)-487(right)
//pos5:M3-->511    M4-->271    M5-->454(left)-482(right)
//pos6:M3-->706    M4-->153    M5-->454(left)-477(right)
//pos7:M3-->354    M4-->399    M5-->487(left)-581(right)
//pos8:M3-->511    M4-->271    M5-->492(left)-549(right)
//pos9:M3-->706    M4-->153    M5-->477(left)-525(right)

void movement(int a1,int a2, int b1, int b2, int c1, int c2, int d) {
//base,shoulder, elbow, gripper

while(analogRead(A0)<int((c1+c2)/2)) { // && analogRead(A0)<c2) {
  Serial.println("Inside movement elbow motor");
  elbow->run(BACKWARD);
  delay(50);
}
elbow->run(RELEASE);

while(analogRead(A1)>int((b1+b2)/2)) { // && analogRead(A1)<b2) {
  Serial.println("Inside movement shoulder motor");
  shoulder->run(BACKWARD);
  delay(50);
}
shoulder->run(RELEASE);

while(analogRead(A2)<int((a1+a2)/2)) { // && analogRead(A2)<a2) {
  Serial.println("Inside movement base motor");
  base->run(FORWARD);
  delay(50);
}
base->run(RELEASE);

while(analogRead(A3)<d) {
  Serial.println("Inside movement gripper motor");
  gripper->run(FORWARD);
  delay(50);
}
gripper->run(RELEASE);

}

void basemovement(int a, int b, int c, int d) {
  //base,elbow,shoulder,gripper

while(analogRead(A3)<850) {
  Serial.println("Inside movement gripper motor");
  gripper->run(FORWARD);
  delay(50);
}
gripper->run(RELEASE);

while(analogRead(A1)<c) {
  shoulder->run(FORWARD);
  delay(50);
}
shoulder->run(RELEASE);
  
while(analogRead(A0)>b) {
  elbow->run(FORWARD);
  delay(50);
}
elbow->run(RELEASE);

while(analogRead(A2)>a) {
  base->run(BACKWARD);
  delay(100);
}
base->run(RELEASE);

delay(10000);
while(analogRead(A3)>d) {
  int prev=analogRead(A3);
  gripper->run(BACKWARD);
  delay(50);
  int next=analogRead(A3);
  if (next == prev && next<840 && prev<840) { 
    Serial.println("prev= "+String(prev)+" next= "+String(next));
    break;
  }
}
gripper->run(RELEASE);
if (analogRead(A3)<825) {
basemovement(279,354,403,820);
}

}

void loop() {
  
Serial.print("M1-->" + String(analogRead(A3)));
/*
Serial.print("    M3-->" + String(analogRead(A0)));
Serial.print("    M4-->" + String(analogRead(A1)));
Serial.println("    M5-->" + String(analogRead(A2)));
*/
//int pos=random(1,10);
//int pos=9;
if (pos!=0) {
Serial.println(pos);
if (pos==1) {
  movement(328,388,390,410,340,370,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==2) {
  movement(369,413,250,290,500,550,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==3) {
  movement(396,439,160,180,670,710,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==4) {
  movement(388,487,390,410,340,370,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==5) {
  movement(454,482,250,290,500,550,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==6) {
  movement(444,467,160,180,670,710,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==7) {
  movement(487,581,390,410,340,370,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==8) {
  movement(492,549,250,290,500,550,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else if (pos==9) {
  movement(467,515,160,180,670,710,850);
  delay(3000);
  basemovement(279,354,403,820);
  delay(1000);
}
else {delay(500);}
pos=0;
delay(10000);
}
}

void receiveData(int byteCount){
while(Wire.available()) {
pos = Wire.read();
Serial.print("data received: ");

}
}

void sendData(){
Wire.write(pos);
}

