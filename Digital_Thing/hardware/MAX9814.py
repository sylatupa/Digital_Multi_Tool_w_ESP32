import machine

adc = machine.ADC(7)

adc.read()

#uint8_t audioBuffer[AUDIO_BUFFER_MAX];
#uint8_t transmitBuffer[AUDIO_BUFFER_MAX];
#uint32_t bufferPointer = 0;

const char* ssid     = "spyprjct-219";
const char* password = "789sumrX";
const char* host     = "192.168.1.114";

bool transmitNow = false;

WiFiClient client;

hw_timer_t * timer = NULL; // our timer
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED; 

void IRAM_ATTR onTimer() {
  portENTER_CRITICAL_ISR(&timerMux); // says that we want to run critical code and don't want to be interrupted
//ADC1_CHANNEL_0
  int adcVal = adc1_get_voltage(ADC1_CHANNEL_7); // reads the ADC
  uint8_t value = map(adcVal, 0 , 4096, 0, 255);  // converts the value to 0..255 (8bit)
  audioBuffer[bufferPointer] = value; // stores the value
  bufferPointer++;
 
  if (bufferPointer == AUDIO_BUFFER_MAX) { // when the buffer is full
    bufferPointer = 0;
    memcpy(transmitBuffer, audioBuffer, AUDIO_BUFFER_MAX); // copy buffer into a second buffer
    transmitNow = true; // sets the value true so we know that we can transmit now
  }
  portEXIT_CRITICAL_ISR(&timerMux); // says that we have run our critical code
}


void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  adc1_config_width(ADC_WIDTH_12Bit); // configure the analogue to digital converter
  adc1_config_channel_atten(ADC1_CHANNEL_0, ADC_ATTEN_0db); // connects the ADC 1 with channel 0 (GPIO 36)

  const int port = 4444;
  while (!client.connect(host, port)) {
    Serial.println("connection failed");
    delay(1000);
  }


  timer = timerBegin(0, 80, true); // 80 Prescaler
  timerAttachInterrupt(timer, &onTimer, true); // binds the handling function to our timer 
  timerAlarmWrite(timer, 125, true);
  timerAlarmEnable(timer);
}

void loop() {
  if (transmitNow) { // checks if the buffer is full
    transmitNow = false;
    client.write((const uint8_t *)audioBuffer, sizeof(audioBuffer)); // sending the buffer to our server
  }
}












from machine import Pin, SPI, ADC
import time

OUT = 33  # Connect it to OUT on microphone

mic = ADC(Pin(OUT))
mic.atten(ADC.ATTN_11DB)

def read_mic():
    return min(max(int(round(mic.read()/15.0)) - 44, 0), 127)

while True:
    val = read_mic()
    print(val)
    time.sleep(0.1)
