import requests
import wmi
import time

url = 'http://<ESP8266_IP_ADDRESS>/temperature/'

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
while(True):
    s = ""
    count1 = 0
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType == u'Temperature':
            count1 += 1
            s += sensor.Name+":\n     "+str(sensor.Value)+" [C]\n"
            if count1 == 2:
                x = requests.post(url, data=s)
                print(x.text)
                time.sleep(1)
            elif(count1>2):
                time.sleep(5)
                count1 = 0
                s = ""

            print("["+sensor.Name+"]")
            print(sensor.Value)
            print()
