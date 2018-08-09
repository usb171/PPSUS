SYSTEM_MODE(MANUAL); // Conexão com a nuvem de forma manual

#define GY80_dev_a 0x53
#define GY80_a_reg_bw 0x2C
#define GY80_a_scale_16 0x03
#define GY80_a_reg_data 0x32
#define GY80_a_bw_3200 0b1111
#define GY80_a_reg_format 0x31
#define GY80_a_reg_pwrctrl 0x2D


void a_set_bw(uint8_t bw);
void a_set_scale(uint8_t scale);
void write(uint8_t device, uint8_t address, uint8_t data);
uint8_t* read(uint8_t device, uint8_t address, uint8_t length);


uint8_t * a_buf;


void setup()
{
  Serial.begin(9600);
  while(!Serial);

  Wire.begin(); // Barramento i2c
  write(GY80_dev_a, GY80_a_reg_pwrctrl, 0x08);
  a_set_scale(GY80_a_scale_16);
  a_set_bw(GY80_a_bw_3200);

}

void loop()
{
  // Ler acelereômetro ****************************************************
  a_buf = read(GY80_dev_a, GY80_a_reg_data, 6); //read the acceleration data from the ADXL345
  Serial.print( ((int16_t)((((int16_t)a_buf[1]) << 8) | a_buf[0])) * 0x03 );
  Serial.print("\t");
  Serial.print( ((int16_t)((((int16_t)a_buf[3]) << 8) | a_buf[2])) * 0x03 );
  Serial.print("\t");
  Serial.print( ((int16_t)((((int16_t)a_buf[5]) << 8) | a_buf[4])) * 0x03 );
  Serial.println("\t");
}

void write(uint8_t device, uint8_t address, uint8_t data)
{
    Wire.beginTransmission(device);
    Wire.write(address);
    Wire.write(data);
    Wire.endTransmission();
}

uint8_t* read(uint8_t device, uint8_t address, uint8_t length)
{
    Wire.beginTransmission(device);
    Wire.write(address);
    Wire.endTransmission();

    //Wire.beginTransmission(device);
    Wire.requestFrom(device, length);
    uint8_t buffer[length];
    while(Wire.available()<length);
    if(Wire.available() == length)
    {
        for(uint8_t i = 0; i < length; i++)
        {
            buffer[i] = Wire.read();
        }
    }
    Wire.endTransmission();

    return buffer;
}

void a_set_scale(uint8_t scale)
{
    uint8_t format = *read(GY80_dev_a, GY80_a_reg_format,1);

    scale &= 0x03;
    format &= ~0x0F;
    format |= scale;
    format |= 0x08;

    write(GY80_dev_a,GY80_a_reg_format, format);
}

void a_set_bw(uint8_t bw)
{
    bw &= 0x0F;
    write(GY80_dev_a,GY80_a_reg_bw,bw);
}
