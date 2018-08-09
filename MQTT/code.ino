
//Bibliotecas/////////////////////
#include <application.h>
#include <spark_wiring_i2c.h>
#include "MQTT.h"
#include <SdFat.h>


//////////////////////////////////


//Configurações Sistema Operacional
String ID = "D02";
SYSTEM_MODE(MANUAL); // Conexão com a nuvem de forma manual
STARTUP(RGB.control(true))
STARTUP(RGB.color(0, 0, 0))
STARTUP(pinMode(D3, OUTPUT))
//STARTUP (WiFi.selectAntenna (ANT_EXTERNAL))

// Tom de inicialização //////////
STARTUP(tone(D3, 1000, 250))
STARTUP(delay(100))
STARTUP(tone(D3, 2000, 250))
STARTUP(delay(100))
STARTUP(tone(D3, 4000, 250))
////////////////////////////////////


//Var. Global/////////////////////
SdFat sd;
File *myFile;
MQTT *client;
bool FLAG_REC = false;
unsigned long tempo_inicial;
uint8_t interador;
String saida;
char line[200];
const uint8_t chipSelect = SS; // SCK => A3, MISO => A4, MOSI => A5, SS => A2 (default)



//Ass. Funções////////////////////////////////////////////////////
void a_set_bw(uint8_t bw);
void a_set_scale(uint8_t scale);
void write(uint8_t device, uint8_t address, uint8_t data);
uint8_t* read(uint8_t device, uint8_t address, uint8_t length);
void ini_sensor();
void rec_date();
void switch_mqtt(char* topic, byte* payload, unsigned int length);

//////////////////////////////////////////////////////////////////

// ADXL345 I2C address is 0x53(83)
#define Addr_a 0x53
int xAccl = 0, yAccl =  0, zAccl = 0;
unsigned int data_a[6];


// L3G4200D I2C address is 0x68(104)
#define Addr_g 0x69
int xGyro = 0, yGyro = 0, zGyro = 0;
unsigned int data_g[6];


void setup() {

    Serial.begin(9600); while(!Serial);

    WiFi.on();
    if(!sd.begin(chipSelect, SPI_FULL_SPEED)) System.reset();
    while (!WiFi.ready()) WiFi.connect();
    if(!ini_mqtt()) System.reset();
    myFile = new File();
    //ini_sensor();
    sd.remove("amostras.csv");

    // Initialise I2C communication as MASTER
    Wire.begin();
    // Start I2C transmission
    Wire.beginTransmission(Addr_a);
    // Select bandwidth rate register
    Wire.write(0x2C);
    // Select output data rate = 100 Hz
    Wire.write(0x0A);
    // Stop I2C Transmission
    Wire.endTransmission();

    // Start I2C transmission
    Wire.beginTransmission(Addr_a);
    // Select power control register
    Wire.write(0x2D);
    // Select auto sleep disable
    Wire.write(0x08);
    // Stop I2C transmission
    Wire.endTransmission();

    // Start I2C transmission
    Wire.beginTransmission(Addr_a);
    // Select data format register
    Wire.write(0x31);
    // Select full resolution, +/-2g
    Wire.write(0x08);
    // End I2C transmission
    Wire.endTransmission();




       // CTRL_REG2
      Wire.beginTransmission(Addr_g);
      Wire.write(0x21);
      Wire.write(0x00);
      Wire.endTransmission();

      //CTRL_REG3
      Wire.beginTransmission(Addr_g);
      Wire.write(0x22);
      Wire.write(0x00);
      Wire.endTransmission();

      // CTRL_REG4
      Wire.beginTransmission(Addr_g);
      Wire.write(0x23);
      Wire.write(0x00);
      Wire.endTransmission();

      // CTRL_REG6
      Wire.beginTransmission(Addr_g);
      Wire.write(0x25);
      Wire.write(0x00);
      Wire.endTransmission();

      // CTRL_REG5
      Wire.beginTransmission(Addr_g);
      Wire.write(0x24);
      Wire.write(0x00);
      Wire.endTransmission();

      //CTRL_REG1
      Wire.beginTransmission(Addr_g);
      Wire.write(0x20);
      Wire.write(0x0F);
      Wire.endTransmission();

}

void loop() {
    client->loop();
}


//Func. MQTT/////////////////////////////////////////////////////////
bool ini_mqtt(){
	byte server[] = {192,168,1,200};
	client = new MQTT(server, 1883, switch_mqtt, 512); client->connect(ID);

    if (client->isConnected()) {
        client->publish("device/", "Device: " + ID);
        client->subscribe("device/" + ID + "/code");
        for(int i = 0; i < 5; i++){ tone(D3,5000,50); delay(100);}
        return true;
    }else{
    	return false;
    }
}

void switch_mqtt(char* topic, byte* payload, unsigned int length){
    char p[length + 1];
    memcpy(p, payload, length);
    p[length] = NULL;
    String message(p);

    String code = message.substring(0,2);
    String user = message.substring(2,5);
    String msg  = message.substring(5);

    Serial.println(code);
    Serial.println(user);
    Serial.println(msg);


    if (code.equals("L1")){
        RGB.color(255, 0, 0);
        client->publish("device/"  + user + "/code", msg);
        tone(D3, 4000, 100);
    }
    else if (code.equals("L2")){
        RGB.color(0, 255, 0);
        client->publish("device/"  + user + "/code", msg);
        tone(D3, 4000, 100);
    }
    else if (code.equals("L3")){
        RGB.color(0, 0, 255);
        client->publish("device/"  + user + "/code", msg);
        tone(D3, 4000, 100);
    }
    else if (code.equals("C1")){ //RSSI
        client->publish("device/"  + user + "/code", String(WiFi.RSSI()));
        tone(D3, 4000, 100);
    }
    else if (code.equals("C2")){
        client->publish("device/"  + user + "/code", msg + "C2T");
        FLAG_REC = true;
        rec_date();
        client->publish("device/"  + user + "/code", msg + "C2T");

        tone(D3, 4000, 100);
    }
    else if (code.equals("C3")){
        client->publish("device/"  + user + "/code", msg);
        tone(D3, 4000, 100);
        if(!myFile->open("amostras.csv", O_READ)) System.reset();
        while ((myFile->fgets(line, sizeof(line))) > 0){
            client->loop();
            client->publish("device/"  + user + "/code", line);
            client->loop();
            delay(5);
            client->loop();

        }
        myFile->close();
        client->publish("device/"  + user + "/code", msg + "C3T");
        tone(D3, 4000, 100);
    }
    else if (code.equals("C4")){
        client->publish("device/"  + user + "/code", msg);
        tone(D3, 4000, 100);
        if(sd.remove("amostras.csv")) client->publish("device/"  + user + "/code", msg + "C4T");
        tone(D3, 4000, 100);
    }
    else if (code.equals("C5")){
        tone(D3, 4000, 100);
        client->publish("device/"  + user + "/code", msg + "C5T");
        tone(D3, 4000, 100);
        FLAG_REC = false;
    }
    else{
        RGB.color(255, 255, 255);
        tone(D3, 1000, 500);
    }

}
//////////////////////////////////////////////////////////////////////


void rec_date(){

    if(!myFile->open("amostras.csv", O_RDWR | O_CREAT)) System.reset();

	tone(D3,2000,100);
	delay(900);
	tone(D3,2000,100);
	delay(900);
	tone(D3,2000,1000);


	while(FLAG_REC){

    	tempo_inicial = micros();

        for(interador = 0; interador < 6; interador++){
            // Start I2C transmission
            Wire.beginTransmission(Addr_a);
            // Select data register
            Wire.write((50+interador));
            // Stop I2C transmission
            Wire.endTransmission();
            // Request 1 byte of data from the device
            Wire.requestFrom(Addr_a,1);
            // Read 6 bytes of data
            // xAccl lsb, xAccl msb, yAccl lsb, yAccl msb, zAccl lsb, zAccl msb
            if(Wire.available()==1) data_a[interador] = Wire.read();
        }

        for(interador = 0; interador < 6; interador++){
            // Start I2C Transmission
            Wire.beginTransmission(Addr_g);
            // Select data register
            Wire.write((40 + interador));
            // Stop I2C transmission
            Wire.endTransmission();
            // Request 1 byte of data
            Wire.requestFrom(Addr_g, 1);
            // Read 6 bytes of data
            // xGyro lsb, xGyro msb, yGyro lsb, yGyro msb, zGyro lsb, zGyro msb
            //while(!Wire.available());
            if(Wire.available() == 1) data_g[interador] = Wire.read();
        }

        // Convert the data to 10-bits
        xAccl = (((data_a[1] & 0x03) * 256) + data_a[0]);
        if(xAccl > 511) xAccl -= 1024;

        yAccl = (((data_a[3] & 0x03) * 256) + data_a[2]);
        if(yAccl > 511) yAccl -= 1024;

        zAccl = (((data_a[5] & 0x03) * 256) + data_a[4]);
        if(zAccl > 511) zAccl -= 1024;

         // Convert the data
        xGyro = ((data_g[1] * 256) + data_g[0]);
        if (xGyro > 32767) xGyro -= 65536;

        yGyro = ((data_g[3] * 256) + data_g[2]);
        if (yGyro > 32767) yGyro -= 65536;

        zGyro = ((data_g[5] * 256) + data_g[4]);
        if (zGyro > 32767) zGyro -= 65536;


        saida = "";
        saida.concat(tempo_inicial);
        saida.concat("\t");
        saida.concat(xAccl);
        saida.concat("\t");
        saida.concat(yAccl);
        saida.concat("\t");
        saida.concat(zAccl);

        saida.concat("\t");
        saida.concat(xGyro);
        saida.concat("\t");
        saida.concat(yGyro);
        saida.concat("\t");
        saida.concat(zGyro);

        myFile->println(saida);
        myFile->flush();
        client->loop();
        while((micros() - tempo_inicial) < 15600);
	}

    myFile->close();
	tone(D3,500,2000);
	delay(900);
	tone(D3,2000,100);

}
