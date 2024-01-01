// #include <Servo.h>

// Servo servo;

void setup() {
  Serial.begin(9600);
  // servo.attach(9);  // Connect servo to pin 9
}
char signal = 0;
void loop() {
    if(Serial.available() > 0){
    signal = Serial.read();
    }

       if (signal == '1') {
     // Control the servo
     // Add code to turn the servo and print "Hello"
     Serial.println("Hello");
   }
    // Debug prints
   Serial.println("Receisegwrhd: ");
   // Serial.println(signal);
    delay(100);

    // Check the received signal

}
