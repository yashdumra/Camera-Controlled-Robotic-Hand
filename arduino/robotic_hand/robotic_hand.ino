#include <Servo.h>

Servo myServo1;
Servo myServo2;
Servo myServo3;
Servo myServo4;
Servo myServo5;

void setup()
{
  Serial.begin(9600);

  myServo1.attach(3);
  myServo2.attach(5);
  myServo3.attach(6);
  myServo4.attach(9);
  myServo5.attach(10);
}

void loop()
{
  if (Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');

    int thumb, indexFinger, middleFinger, ringFinger, pinky;

    sscanf(data.c_str(), "%d,%d,%d,%d,%d",
           &thumb,
           &indexFinger,
           &middleFinger,
           &ringFinger,
           &pinky);

    myServo1.write(thumb * 180);
    myServo2.write(indexFinger * 180);
    myServo3.write(middleFinger * 180);
    myServo4.write(ringFinger * 180);
    myServo5.write(pinky * 180);
  }
}
