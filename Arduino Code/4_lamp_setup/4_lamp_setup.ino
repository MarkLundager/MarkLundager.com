int green = 12;
int blue = 11;
int yellow = 10;
int red = 9;

void setup() {
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(red, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    processCommand(data);
  }
}

void processCommand(String command) {
  command.trim();
  if (command.equals("red")) {
    togglePin(red);
  } else if (command.equals("green")) {
    togglePin(green);
  } else if (command.equals("blue")) {
    togglePin(blue);
  } else if (command.equals("yellow")) {
    togglePin(yellow);
  } else {
    Serial.println("failure, command received: " + command);
  }
}

void togglePin(int pin) {
  if (digitalRead(pin) == HIGH) {
    digitalWrite(pin, LOW);
    Serial.println("success");
  } else {
    digitalWrite(pin, HIGH);
    Serial.println("success");
  }
}