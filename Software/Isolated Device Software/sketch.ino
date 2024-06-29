//Program for acceleration rate control for Stepper Motor with L298N & Arduino
//Source: https://www.ee-diary.com/2021/08/stepper-motor-acceleration-speed.html


#include <AccelStepper.h>
#include <LiquidCrystal_I2C.h>
#include <Keypad.h>

const uint8_t ROWS = 4;
const uint8_t COLS = 4;
char keys[ROWS][COLS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};

uint8_t colPins[COLS] = { 5, 4, 10, 12 }; // Pins connected to C1, C2, C3, C4
uint8_t rowPins[ROWS] = { 9, 8, 7, 6 }; // Pins connected to R1, R2, R3, R4

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);



#define I2C_ADDR    0x27
#define LCD_COLUMNS 16
#define LCD_LINES   2

LiquidCrystal_I2C lcd(I2C_ADDR, LCD_COLUMNS, LCD_LINES);

//define pins for stepper motor
int en = 10;
int in1 = 9;
int in2 = 8;
int in3 = 7;
int in4 = 6;
int buzz = 11;
int speed = 1;
int adjst = 0;

int fullstep = 4; //number of stages in full drive
int halfstep = 8; //number of stages in half drive
int stepdrive = fullstep; //select step drive mode

//define stepper motor with step mode and inputs
AccelStepper stepper1(1, 3, 2);

int steps = 20; //number of steps per revolution
long last = 0;
int lag = 500; //time (ms) interval for display
int dir = 1; //direction of rotation
float rpm, v, oldspeed, a;
int nsteps;

void setup() {
  Serial.begin(9600); // define Serial output baud rate
  pinMode(en, OUTPUT);
  digitalWrite(en, HIGH);
  stepper1.setMaxSpeed(3); //max speed 2000 steps/s
  stepper1.setAcceleration(0); //acceleration rate(steps/s^2)
  stepper1.moveTo(20000);


  lcd.init();
  lcd.backlight();

  // Print something
  lcd.setCursor(0, 0);
  lcd.print("Hello !");
  lcd.setCursor(0, 1);
  lcd.print("# For Settings ");

}

void loop() {
  delay(100);
  stepper1.moveTo(110000); //move to position ±100 or ±200
  if(stepper1.distanceToGo()==0)
  stepper1.setSpeed(2000);
  stepper1.moveTo(20000);
  if (millis() > last + lag) //lag time elapsed since last print
  {
    v = stepper1.speed(); //get motor speed (steps/s)
    nsteps = v * lag / pow(10, 3); //No. of steps taken during lag time
    rpm = 60.0 * v / steps; //RPM
    a = (v - oldspeed) * 1000.0 / lag; //Acceleration
    oldspeed = v; //update speed value
    last = millis(); //update last print time

  }
  stepper1.run(); //move to new position

  char key = keypad.getKey();

  String msg;

  if (key != NO_KEY || adjst==1) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Press # for ");
    lcd.setCursor(0, 1);
    lcd.print("Settings ");

    if (key=='#' || adjst==1){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Speed Settings");
      lcd.setCursor(0, 1);
      lcd.print("Yes(A) or No(B)");
      key = keypad.waitForKey();

      if (key == 'A') {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Enter Flow Rate:");
        lcd.setCursor(5, 1);
        lcd.print("B - Enter");
        while (true) {
          char speedKey = keypad.waitForKey();
          if (speedKey == 'B') {
            int speed = msg.toInt();
            Serial.println(speed);
            stepper1.setMaxSpeed(speed);
            break;
          }
          if (speedKey == 'C') {
            msg.remove(msg.length() - 2);
          }
          lcd.setCursor(msg.length(), 1);
          lcd.print(speedKey);
          msg += speedKey;
        }
      // Convert the entered speed to an integer
 
        
        

     
        
      }
    }
  }
}



// if(key == 'A' || adjst==1){
//           speed = speed +1;
//           lcd.setCursor(9, 0);
//           lcd.print(speed);
//           lcd.setCursor(0, 1);
//           lcd.print("press * to ok");
//           adjst=1;
//           key = keypad.waitForKey();
//           if (key=='*'){
//           adjst=0;
//           }
//         }

//         if(key == 'B' || adjst==2){
//           speed = speed -1;
//           lcd.setCursor(9, 0);
//           lcd.print(speed);
//           lcd.setCursor(0, 1);
//           lcd.print("press * to ok");
//           adjst=2;
//           key = keypad.waitForKey();
//           if (key=='*'){
//           adjst=0;
//           }
//         }