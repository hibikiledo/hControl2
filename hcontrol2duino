#include <aJSON.h>
#include <SPI.h>
#include <Ethernet.h>

#define SL1_PIN 8
#define RT_DALAY 10000
#define TIMEOUT 2000
#define REFRESH_RATE 2000

unsigned int aBytes;
unsigned int pcount;
unsigned long time;
unsigned int i,j;
unsigned char ch;
boolean err = false;
boolean data_flag = false;
char buf[256];

// Ethernet
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
byte server[] = {128, 199, 184, 144};
EthernetClient client;

void setup()
{
    // enable serial for debugging
    Serial.begin(9600);

    // ask dhcp server for ip address
    while( !Ethernet.begin(mac) ) {
        Serial.println("Fail to get IP Address");
        Serial.print("Try again in "); Serial.print(RT_DALAY); Serial.println(" seconds.");
    }

    Serial.println("Successfully get IP Address");

    // Setup pin
	pinMode(SL1_PIN, OUTPUT);
	// Init pin
	digitalWrite(SL1_PIN, HIGH);
}

void loop()
{
    // reset flags
    err = false;

	// connect to server
	if( client.connect(server, 5000) ) {
		Serial.println("Connected");
		client.println("GET /api/{AUTH_TOKEN}/get/OUTDOOR/spotlight-1 HTTP/1.1");
		client.println();
	}
	else {
		Serial.println("Fail to connect");
		err = true;
	}

    /*
        Process response from server
    */

    i = 0;                          // buffer index pointer
    pcount = 0;                     // counting # of braces
    data_flag = false;              // when true, the ch read is data or waste otherwise
    memset(buf, 0, sizeof(buf));    // clear all data in buffer
    time = millis();                // save current time for checking TIMEOUT

    // Process data only if connection doesn't result in error
    if( !err ) {
        while( true ) {
             if( client.available() ) {
                  ch = client.read();
                  // start of json data
                  if( ch == '{' ) {
                       data_flag = true;
                       pcount++;
                  }
                  if( ch == '}' ) {
                       pcount--;
                       // end of json data
                       if( pcount == 0 ) {
                            data_flag = false;
                            buf[i] = ch;
                            i++;
                            // done! stop the loop
                            break;
                       }
                  }
                  // keep data in buf when data_flag is raised
                  if( data_flag ) {
                      buf[i] = ch;
                      i++;
                  }
             } else {
                 // no data received from server .. check for timeout
                 // timeout excees TIMEOUT, break out the loop
                 if( millis() - time > TIMEOUT ) {
                      Serial.println("Timeout. No data received from server");
                      break;
                 }
             }
        }
    }

    // HARDCODED : handling relay for spotlight-1
    aJsonObject* root = aJson.parse(buf);
    aJsonObject* data = aJson.getObjectItem(root, "value");
    if( strcmp(data->valuestring,"on") == 0 ) {
         digitalWrite(SL1_PIN, LOW);
    }
    if( strcmp(data->valuestring,"off") == 0 ) {
         digitalWrite(SL1_PIN, HIGH);
    }

    // Verbose
    Serial.println(buf);

	// Clean up
    aJson.deleteItem(root);
    client.flush();
	client.stop();

	delay(REFRESH_RATE);
}
