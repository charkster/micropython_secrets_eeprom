import machine
import json

# your device's i2c
i2c = machine.I2C(1, sda=machine.Pin(6), scl=machine.Pin(7), freq=400000)

# read from attached i2c eeprom, my creds are smaller than 255 characters, '\n' is at the end of the json data
eeprom_str = i2c.readfrom_mem(0x50,0x0000,255,addrsize=16).decode('ascii').split('\n')[0]
json_str = json.loads(eeprom_str)
ssid                = json_str.get('ssid', '')
password            = json_str.get('password', '')
sender_email        = json_str.get('sender_email', '')
sender_app_password = json_str.get('sender_app_password', '')
recipient_email     = json_str.get('recipient_email', '')

# now the eeprom can be removed and wifi/email can be accessed with passwords in sram
