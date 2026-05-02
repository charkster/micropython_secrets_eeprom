# micropython_secrets_eeprom
Store passwords in json format inside eeprom. Remove eeprom after powering-up micropython device.

I have some wifi connected sensors in my yard and did not want to leave my wifi and email passwords on them. I connect an eeprom board with a Stemma cable and then remove it a couple seconds after it boots. Now all the sensitive information is stored in the MCU's volatile sram.

I use a [Sparkfun eeprom with Stemma connectors](https://www.sparkfun.com/sparkfun-qwiic-eeprom-breakout-512kbit.html) as my removable memory device. The write buffer is 128 bytes. Use the [CAT24C512.py](https://github.com/charkster/micropython_secrets_eeprom/blob/main/CAT24C512.py) write_data function if your secrets are larger than 128 bytes.

![picture](https://www.sparkfun.com/media/catalog/product/cache/f3020b7489dcfc4d1d147cf4dad07b7f/1/8/18355-SparkFun_Qwiic_EEPROM_Breakout_-_512Kbit-02.jpg)
