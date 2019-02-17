// Adaptations for DC Multi-Tool, by Shaun
// From
// ArduinoJson - arduinojson.org
// Copyright Benoit Blanchon 2014-2018
// MIT License

##include <ArduinoJson.h>
##include <SD.h>
##include <SPI.h>
#include "Config_init.h"

//void Config_init::Config_init() {}

void Config_init::Hello()
{

    Serial.print("world");
}

const char *filename = "/Digital_Thing_Config.json";  

struct Config {
    char hostname[64];
    int port;
};
Config config;                         

void loadConfiguration(const char *filename, Config &config) {
    // Open file for reading
    File file = SD.open(filename);
    // Allocate the memory pool on the stack. Don't forget to change the capacity to match your JSON document. Use arduinojson.org/assistant to compute the capacity.
    StaticJsonBuffer<512> jsonBuffer;
    JsonObject &root = jsonBuffer.parseObject(file);

    if (!root.success())
	Serial.println(F("Failed to read file, using default configuration"));
    config.port = root["port"] | 2731;
    strlcpy(config.hostname, root["hostname"] | "example.com",sizeof(config.hostname));          
    file.close();
}

// Saves the configuration to a file
void saveConfiguration(const char *filename, const Config &config) {
    SD.remove(filename);
    File file = SD.open(filename, FILE_WRITE);
    if (!file) {
	Serial.println(F("Failed to create file"));
	return;
    }

    StaticJsonBuffer<256> jsonBuffer;
    // Allocate the memory pool on the stack Don't forget to change the capacity to match your JSON document. Use https://arduinojson.org/assistant/ to compute the capacity.
    JsonObject &root = jsonBuffer.createObject(); // Parse the root object
    root["hostname"] = config.hostname;
    root["port"] = config.port;

    // Serialize JSON to file
    if (root.printTo(file) == 0) {
	Serial.println(F("Failed to write to file"));
    }

    // Close the file (File's destructor doesn't close the file)
    file.close();
}

// Prints the content of a file to the Serial
void printFile(const char *filename) {
    File file = SD.open(filename);
    if (!file) {
	Serial.println(F("Failed to read file"));
	return;
    }
    while (file.available()) {
	Serial.print((char)file.read());
    }
    Serial.println();
    file.close();
}
