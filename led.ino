//define pins for the red, green and blue LEDs
#define RED_LED 6
#define BLUE_LED 5
#define GREEN_LED 9


//Green1,Red2,Blue3,custom4
 int precolor=4;


//overall brightness value
int brightness = 255;
//individual brightness values for the red, green and blue LEDs

int rBright;
int gBright; 
int bBright;

String redInput;
String greenInput;
String blueInput;

int fadeSpeed = 10;


void setup() {


  Serial.begin(9600);
  Serial.println("Arduino started.");
  
  //set up pins to output.
  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);

//Call the TurnOn method, wait, then call TurnOff 
//TurnOn();
//delay(5000);
//manualColor();
//TurnOff();
//incomingRGB();
//TurnOff();
}


/*
void TurnOn(){
   
    for (int i=0;i<256; i++){
      
      analogWrite(RED_LED, rBright);
      rBright +=1;
      delay(fadeSpeed);

    }
    
    for (int i=0;i<256; i++){
      
      analogWrite(BLUE_LED, bBright);
      bBright += 1;
delay(fadeSpeed);
    }  

    for (int i=0;i<256; i++){
      
      analogWrite(GREEN_LED, gBright);
      gBright +=1;
      delay(fadeSpeed);
    }  
}
   */
void TurnOff(){
    for (int i=0;i<256; i++){
          analogWrite(GREEN_LED, brightness);
          analogWrite(RED_LED, brightness);
          analogWrite(BLUE_LED, brightness);
    
      
      brightness -= 1;
 
      delay(fadeSpeed);

    }
}

/*
void  testrun(){
  if (precolor==2){
    analogWrite(RED_LED, 255);
    delay(5000);
  }else if  (precolor ==1){
    analogWrite(GREEN_LED,255);
    delay(5000);
   }else if(precolor==3){
     analogWrite(BLUE_LED,255);
     delay(5000);
     }else if(precolor==4){
     analogWrite(RED_LED,255);
     analogWrite(GREEN_LED,0);
     analogWrite(BLUE_LED,255);
     delay(5000);
     }     
   }
    */
  void rainbow(){
    delay(fadeSpeed);

  }

  void flashingLights(){


  }
   
  void customRun(){
    delay(fadeSpeed);  
    analogWrite(RED_LED,rBright);
    analogWrite(GREEN_LED,gBright);
    analogWrite(BLUE_LED,bBright);
  }

  void manualColor(){
    analogWrite(RED_LED,80);
    analogWrite(GREEN_LED,0);
    analogWrite(BLUE_LED,80);
  }


  
  void incomingRGB(){
    if (Serial.available()>0){
      redInput=Serial.readStringUntil('*');    // checks * , ; , . characters at the end of string
      greenInput=Serial.readStringUntil(';');  // and catches them 
      blueInput=Serial.readStringUntil('.');
      
      rBright=redInput.toInt();              // turns the strings values into integers
      gBright=greenInput.toInt();            // to get red, green, blue brightness values
      bBright=blueInput.toInt();  

      /*Serial.println("--------------- Incoming RGB Values -----------");
      Serial.print(" Red input is : ");
      Serial.println(redInput);
      Serial.print(" Green input is : ");      
      Serial.println(greenInput);
      Serial.print(" Blue input is : ");
      Serial.println(blueInput); */
      
    }
  }
  


void loop(){
    incomingRGB();
    customRun();
   /* Serial.print("--------------------------------------");
    Serial.print(" Red Brightness is: ");
    Serial.print(rBright);
    Serial.print(" Green Brightness is: ");
    Serial.print(gBright);
    Serial.print(" Blue Brightness is: ");
    Serial.print(bBright);
   // Serial.print(" Brightness is: ");
   // Serial.println(brightness);
    delay (5000);  */
}

