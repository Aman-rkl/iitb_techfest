String InBytes;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (Serial.available() > 0) {
    InBytes = Serial.readStringUntil('\n');
    if (InBytes == "off") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write("LED ON");
    }
    if (InBytes == "on") {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.write("LED OFF");
    }
    else {
      Serial.write("invalid information");
    }
  }
}
