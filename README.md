# Temperature reporting device based on ESP8266 Wi-Fi microchip and using Python 
### <**Only works on Windows**>

![Logos](https://github.com/ga-vo/esp8266-py-temp/blob/main/images/screen.png)
 
* Under [`/ESP8266 Temp/`](https://github.com/ga-vo/esp8266-py-temp/tree/main/ESP8266%20Temp):
  * [`/ESP8266Temp.ino`](https://github.com/ga-vo/esp8266-py-temp/blob/main/ESP8266%20Temp/ESP8266Temp.ino) C++ code for ESP8266 chip, as a webserver receiving data by POST method
  * [`/sendTemp.py`](https://github.com/ga-vo/esp8266-py-temp/blob/main/ESP8266%20Temp/sendTemp.py) Python code to obtain PC temperatures using [`WMI Library`](https://pypi.org/project/WMI/) and sending data via POST using [`Request Library`](https://pypi.org/project/requests/) 
