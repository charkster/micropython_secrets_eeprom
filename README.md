# micropython_secrets_eeprom
Store passwords in json format inside eeprom. Remove eeprom after powering-up micropython device.

I have some wifi connected sensors in my yard and did not want to leave my wifi and email passwords on them. I connect an eeprom board with a Stemma cable and then remove it a couple seconds after it boots. Now all the sensitive information is stored in the MCU's volatile sram.

I use an [Adafruit eeprom with a Stemma connectors](https://www.adafruit.com/product/5146) as my removable memory device.

![picture](https://cdn-shop.adafruit.com/970x728/5146-01.jpg)
