import machine
import json

# your device's i2c
i2c = machine.I2C(1, sda=machine.Pin(6), scl=machine.Pin(7), freq=400000)

# don't use '\n' in credentials as it is used to detect the end of json data
creds = {'ssid'                : 'YOUR_SSID',
         'password'            : 'your_password',
         'sender_email'        : 'sender_email@company.com',
         'sender_app_password' : 'email_password',
         'recipient_email'     : 'receive_email@other.com' }

json_str = json.dumps(creds)
# my eeprom has a 16bit address
i2c.writeto_mem(80,0x0000,bytearray(json_str + '\n','ascii'),addrsize=16)
