###### tags: IoT Project
:::info
#  Smart Aquarium using PyCom
 
 ######  By Peter Daniel, pd222hu
:::





This IoT project is a simple smart aquarium system that uses Pycom's LoPy4 development board and MicroPython (i.e., Python for microcontrollers). It measures the temperature and pH of an aquarium, displays the value in an OLED screen, sends the data to the cloud and alerts based on real-time data.

This project could be done within a day or two by following this tutorial, once all the vital components are at hand. 



## Objective

I have an aquarium at home and as part of my desire to having a smart home, i decided to make it smarter. Since keeping your aquarium's pH and temperature level stable and in optimal range is critical for the health of the fish and the maintenance of the tank, i will be able to monitor the readings constantly and be alerted whenever a spike or a drop from the ideal range is detected. This project can give insight into the importance of IoT in our everyday life.

## Material

Here is the BOM (Bill of Material) you'll need for this project: 
(**Note:** The *LoPy4 and sensors bundle* can be bought from [Electrokit](https://www.electrokit.com/en/product/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/) for 949.00 SEK)


###### Table 1. BOM




| Component                                          | No. | Spec                                                                                                                                                        | Picture                              | Buy    |
| -------------------------------------------------- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | --- |
| LoPy4                                              | x1  | A Micropython-programmable quadruple bearer board that works with LoRa, Sigfox, WiFi and Bluetooth. | ![](https://i.imgur.com/r4UKF4B.png) |[PyCom](https://pycom.io/product/lopy4/)    |
| Expansion board v3.1                               | x1  | Compatible with Pycom's WiPy, LoPy, SiPy, FiPy, and GPy development boards. Needed to program and power the LoPy4 board.                                    | ![](https://i.imgur.com/Y7DIzfp.png) |[PyCom](https://pycom.io/product/expansion-board-3-0/)     |
| Antennae                                           | x1  | External WiFi, LoRa and Sigfox antenna.                                                                                                                     | ![](https://i.imgur.com/sYiFVXD.png) |[PyCom](https://pycom.io/product/lora-868mhz-915mhz-sigfox-antenna-kit/)      |
| Micro USB cable                                    | x1  | Allows you to connect to your personal computer for programming.                                                                                                                 | ![](https://i.imgur.com/SjXGBHo.png) |[Electrokit](https://www.electrokit.com/en/product/usb-kabel-a-hane-micro-b-hane-15cm/)     |
| Jumper wires                                       | x20 | Used for making connections between components on your breadboard and your LoPy4's header pins.                                                                  | ![](https://i.imgur.com/B63H8Fl.png) |[Electrokit](https://www.electrokit.com/en/product/jumper-wires-20-pin-30cm-female-male/)     |
| Breadboard                                         | x1  | A board on which you can build electronic circuits without soldering.                                                                              | ![](https://i.imgur.com/C7rYMwp.png) |[Electrokit](https://www.electrokit.com/en/product/solderless-breadboard-400-tie-points/)     |
| Battery holder 3xAAA with switch and JST-connector | x1  | Connects 3 AAA batteries together in series for powering a 3.3V project                                                                                     | ![](https://i.imgur.com/BUjHlfE.png) |[Electrokit](https://www.electrokit.com/en/product/battery-holder-3xaaa-with-switch-and-jst-connector/)     |
| Rechargeable AAA NiMH Batteries                    | x3  | The output voltage will range from about 3.7V with charged batteries to 2.7V at the end of life with a nominal voltage of 3.6V.                             | ![](https://i.imgur.com/4G5iHSd.png) |[Electrokit](https://www.biltema.se/en-se/office---technology/batteries/rechargeable-batteries/aaa-rechargeable-batteries-4-pack-2000041810)     |
| Digital waterproof temperature sensor (DS18B20)    | x1  | Measures temperature from -55°C to +125°C with ±0.5°C Accuracy. The resolution of the temperature sensor is user-configurable to 9, 10, 11, or 12 bits.     | ![](https://i.imgur.com/SdSD3wf.png) |[Kjell](https://www.kjell.com/se/produkter/el-verktyg/arduino/moduler/temperatursensor-med-kabel-for-arduino-p87081)     |
| Analog pH sensor (SEN0161)                         | x1  | Measures pH with a ± 0.1pH accuracy at 25 ℃.                                                                                                                | ![](https://i.imgur.com/gCRQpNT.png) |[Arduino](https://store.arduino.cc/gravity-analog-ph-sensor-meter-kit-for-arduino?queryID=undefined)     |
| 1.12" OLED display (SSD1327)                       | x1  | A small display with 16 grayscales, very high contrast and no backlight. Uses the SSD1327 driver chip.                                                      | ![](https://i.imgur.com/UsD2d4o.png) |[Arduino](https://store.arduino.cc/grove-oled-display-1-12)     |
| Piezo Buzzer                                       | x1  | An electrical component that can be used to detect vibrations and create a tone, alarm or sound.                                                                                                                     | ![](https://i.imgur.com/ctYUia5.png) |[Electrokit](https://www.electrokit.com/en/product/buzzer-3-8-khz/)     |
| Resistor (4.7kΩ)                                   | x1  | Used to reduce current flow, adjust signal levels, to divide voltages, bias active elements, and terminate transmission lines.                              | ![](https://i.imgur.com/wC7uXLJ.png) |[Electrokit](https://www.electrokit.com/en/product/resistor-carbon-film-0-25w-4-7kohm-4k7/)     |
| Aquarium (Aquael Leddy 60)                         | x1  | A complete aquarium package of 54 liters with energy-efficient LED lighting of 7 w, pump, filter and 50w immersion heater.                                  | ![](https://i.imgur.com/IQTVLtU.png) |[CyberZoo](https://www.cyberzoo.se/sv/articles/2.199.846/aquael-leddy-60-akvariepaket-54-liter-fraktfritt)     |



## Computer setup

To follow this tutorial, you'll need firmware installed in your development board. You will also need an IDE to write and upload the code to your board. 

### Steps:
1. **Update expansion board firmware:**
    You won’t need to flash the expansion board firmware if you’ve ordered a latest board (v3.0 or v3.1). But if your board is     older, you could update the firmware by following this [documentation](https://docs.pycom.io/updatefirmware/expansionboard/).
2. **Update device firmware:**
    Updating your development board's firmware to the latest version is crucial for being able to connect your device to           PyBytes, which is an IoT platform. The basic firmware upgrade procedure can be found [here](https://docs.pycom.io/updatefirmware/device/).
3. **Install an IDE (Integrated Development Environment):**
   The next step is intalling an IDE that supports a PyMaker plugin. As of this moment, there are only two editors one could    choose from, [Atom](https://flight-manual.atom.io/getting-started/sections/installing-atom/) or [VS Code](https://code.visualstudio.com/docs/setup/setup-overview). I already had Atom in my machine and i'm familiar with it, so i        chose to stick with it. But if you decide to work with VS Code, you will also need to install [Node.js](https://nodejs.org/en/download/) on your computer.
4. **Install Pymakr (plugin):**
   Once you downloaded the text editor, you can now install the [Pymakr](https://docs.pycom.io/gettingstarted/software/atom/)          Plugin by navigating to:
   file > settings > Install (or just press Install a Package on the welcome guide) and then search for ***PyMakr***.
5. **Creating a project in Pymakr:**
   Now that you have installed Pymakr and connected your device, it is time to begin programming your device by creating your      first project, [Controlling the on-board RGB LED](https://docs.pycom.io/gettingstarted/). As seen in Figure 1, the pymakr      plugin adds REPL console to Atom. You can run a selected file by pressing the *play button* and upload your project to the device by the pressing the *upload button* beneath it.
   
   ![](https://i.imgur.com/GAUrkT2.png)
    ###### Figure 1. REPL console (in Atom)






## Putting everything together





![](https://i.imgur.com/n7N3phS.png)
###### Figure 2. Schematic diagram of the project


Now it's time to build the electronic circuit in the breadboard and connect it to [LoPy4’s header pins](https://docs.pycom.io/gitbook/assets/lopy4-pinout.pdf). **Caution:** avoid powering the device while connecting the components! Wire colour is an aid to help you keep track of what is connected to which. In this guide, we will use black for **GND** (ground), red for **3V3** (3.3V power supply), white for **SDA** (**S**erial **DA**ta) and yellow for **SCL** (**S**erial **CL**ock). Breadboards are usually divided into four sections, two outer sections and two inner sections.  Each row of five sockets in the inner sections are electrically connected to each other (see the green lines in figure 3).  The two outer sections of the breadboard are usually used exclusively for power.  On many breadboards these sockets will be labeled with colors denoting positive voltage (usually red) and ground (black or blue) with a **+** and **-** sign.  It is important to note that on many breadboards the power lines only run half the length of the board (as indicated in figure 3).  You will need to run a wire between these two sections to send power to from one end to the other. 



![](https://i.imgur.com/NmS4Kv7.png)
######  Figure 3. Breadboard




Start by connecting the **3V3** pin of your device to the power rail (+ sign) in the breadboard, and **GND** pin to ground (- sign). Next connect the OLED display by attaching **SDA** to **PIN 9** in the pycom device, **SCL** to **PIN 10**, **VCC** to **power** and **GND** to **ground** in the breadboard (see Figure 2). After that, connect the [piezo buzzer's](https://components101.com/misc/buzzer-pinout-working-datasheet) **longer terminal lead** to **PIN 8** of the device and the **shorter terminal lead** to **ground**. Then we'll connect the digital temperature sensor (DS18B20) that provides 9 to 12-bit (configurable) temperature readings and communicates over a [OneWire bus](https://docs.pycom.io/tutorials/hardware/owd/). Connect **VDD** to **power**, **GND** to **ground** and **DQ** (data line) to the digital **PIN 22**. Also connect a 4.7k ohm pull-up resistor to the data line on one side and power line (3.3V) on the other side as seen in figure 2. Finally, make a connection for the analogue pH sensor (SEN0161) by connecting the **DQ** to an analogue **PIN 16**, as well as **VDD** and **GND** to **power** and **ground** respectively. Although 3.3V more often works for a 5V logic (and it does in our case), the pH sensor is meant to use 5V. So alternatively, you can use the Vin (3.5-5.5V) instead. But since the output of 5v will burn the pycom device if more than 3.3 volts is used, you will need a [voltage divider](https://en.wikipedia.org/wiki/Voltage_divider) to the data port. This means you need to step down the voltage using resistors. You could use the [equation](https://www.allaboutcircuits.com/tools/voltage-divider-calculator/): **V***out* = **V***in* * (**R***2* / **R***1* + **R***2*), (where **V***out* and **V***in* are output and input voltage respectively, and **R***1* and **R***2* are the resistors) to calculate the resistor values you need to use. Using multimeter will be handy in this case. Or you can instead use any 3 resistors with the same value, connected in series to 5V and take voltage from 2 of them. So it will be 2/3 from 5V = 3.333V (very close to 3.3V). This combination of the available resistors will work. (**Note:** I'm mounting the breadboard and LoPy4 in a plastic base that comes with an Arduino Starter kit. Aletrnatively, you can make a customized base for your devices using 3D-printing).

![](https://i.imgur.com/7wlWRlt.jpg)

###### Figure 4. Implementation of the circuit 





## Platform

The first cloud platform that i tried was [Pybytes](https://docs.pycom.io/pybytes/gettingstarted/), which is PyCom's device managment platform designed to optimise your project when using Pycom boards. It offers data visualisation, notification (such as battery-level), geo-location and it is free to use. PyBytes only stores your data for a month, so if you want to persist your data, you have to integrate your project with external services or IoT platforms. **PyBytes** offers a way to integrate with [AWS IoT](https://docs.pycom.io/pybytes/integrations/amazon-iot/), [Microsoft Azure](https://docs.pycom.io/pybytes/integrations/azure/), [Google Cloud IoT](https://docs.pycom.io/pybytes/integrations/google/) and [Web Hooks](https://docs.pycom.io/pybytes/integrations/webhooks/). I integrated it with WebHooks.

Another low-code cloud platform that i used was [Ubidots](https://ubidots.com/), which offers both a free and paid subscription. The free Ubidots STEM platform is simple-to-use, has real-time dashboards with over 30 plus widgets for visualizing data and easy to create events that triggers and alerts the user with Email, SMS, Telegram, Voice call, Webhooks or Slack notifications. I chose to be alerted via sms and email. The paid subscription has many other features which could prove useful if i decided to scale this project.

Alternatively, one could use Big Data Platforms such as [Amazon Web Services IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html), [Google IoT](https://cloud.google.com/iot/docs/how-tos/getting-started) and [IBM IoT](https://developer.ibm.com/technologies/iot/learningpaths/iot-getting-started-iot-development/) instead.



## The code


Here you can find all the files and download the complete code from the [github repository](https://github.com/Peter-Daniel-hkr/smart-aquarium-using-microphython). The main libraries that i used were the [OneWire](https://github.com/pycom/pycom-libraries/tree/master/lib/onewire) for the DS18x20 temperature sensor, [Urequests](https://github.com/jotathebest/micropython-lib/blob/master/urequests/urequests.py) for Ubidots and [SSD1327](https://github.com/iot-lnu/applied-iot/blob/master/sensor-examples/Grove%20Oled%201%222%20display%20128x128/ssd1327.py) for the OLED display.

Once you've downloaded the code, organize the files in your IDE (text editor) as seen in Figure 5. Then upload the project to your device. If you did everything correctly, you will see data printed in the REPL console. Then head over to PyBytes and Ubidots to see if your signals are being transmitted.

![](https://i.imgur.com/TWMFW92.png)
###### Figure 5. File structure of the project in Atom IDE

### main.py

```
import machine
import time
import pycom
import keys
import urequests as requests
from machine import ADC, I2C, Pin, PWM
from onewire import OneWire, DS18X20
from network import WLAN
import ssd1327

#  =================== DECLARATION ================
pycom.heartbeat(False)

# Temperature sensor Declaration
ow = OneWire(Pin('P22'))                    # DS18B20 data line connected to pin P22
temp = DS18X20(ow)


pycom.pybytes_on_boot(True)

# OLED display Declaration
i2c = I2C(0)                                 # create on bus 0
#i2c = I2C(0, pins=('P9','P10'))             # PIN assignments (P9=SDA, P10=SCL)
#display = ssd1327.WS_OLED_128X128(i2c)      # Grove OLED Display
display = ssd1327.SH1107_I2C(128, 128, i2c)  # Width and height of the display
display.fill(0)                              # '0' for BLACK & '1' for WHITE
#display.invert(1)


# Buzzer Declaration

A6 = 1760                                  # define frequency for each tone
AS6 = 1865
B6 = 1976
E6 = 1319
G6 = 1568
A7 = 3520
C7 = 2093
D7 = 2349
E7 = 2637
F7 = 2794
G7 = 3136

buzzer_pin = Pin("P8")                       # set up pin PWM timer for output to buzzer
pwm = PWM(0, frequency=300)
pwm_channel = pwm.channel(2, duty_cycle = 0, pin=buzzer_pin)

TOKEN = keys.token                           # Put your ubidots TOKEN here
DELAY = 1                                    # Delay in seconds

# pH sensor Declaration
adc = machine.ADC(bits=10)                   # ADC (Analogue to Digital Conversion)
apin = adc.channel(pin='P16')                # create an analog pin on P16


# WiFi Declaration
wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)
#print(wlan.scan())

# Assign your own Wi-Fi credentials (SSID and Password) here
wlan.connect(keys.wifi_ssid, auth=(WLAN.WPA2, keys.wifi_password))

while not wlan.isconnected():
    machine.idle()
print("Connected to Wifi\n")



#  ===================IMPLEMENTATION================
# Plays the Super Mario melody
def play_tune():
    super_mario_tone = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0,
                        AS6, A6, 0, G6, E7, 0, G7, A7,0, F7, G7, 0, E7, 0, C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0,
                        A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0, C7, D7, B6, 0, 0]
    for i in super_mario_tone:
        if i == 0:
            pwm_channel.duty_cycle(0)
        else:
            pwm = PWM(0, frequency = i)        # changes frequency to change tone
            pwm_channel.duty_cycle(0.50)
        time.sleep(0.150)



# Sends data to PyBytes
def send_data_to_pybytes(pH, temperature):
    pybytes.send_signal(1, pH)
    pybytes.send_signal(2, temperature)
    time.sleep(DELAY)


# Builds the JSON-object to send the POST HTTP request
def build_json(variable1, value1, variable2, value2, variable3, value3):
    try:
        lat = 56.029394
        lng = 14.156678
        data = {variable1: {"value": value1},
                variable2: {"value": value2, "context": {"lat": lat, "lng": lng}},
                variable3: {"value": value3}}
        return data
    except:
        return None


# Sends the POST HTTP request. Please reference the REST API reference https://ubidots.com/docs/api/
def sending_data_to_ubidots(device, value1, value2, value3):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json("temperature", value1, "position", value2, "pH", value3)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass

# =================== MAIN ===================

while True:
    millivolts = apin.voltage()             # Reads the voltage in mV
    print(millivolts)
    # Data values
    pH = millivolts / 1024 * 5 * 1.45       # Calculates the pH
    print(pH)
    print("pH probe reading: {}".format(pH))
    time.sleep(5)
    temp.start_conversion()                 # Start the temp conversion on one DS18x20 device
    time.sleep(DELAY)
    temperature = temp.read_temp_async()    # Read the temperature of one DS18x20 device if the conversion is complete, otherwise return None.
    while temperature is None:
        temperature = temp.read_temp_async()
    print("Temperature probe reading: {}".format(temperature))

    display.text('pH: ' + str(pH), 0, 10, 255)
    display.show()                          # Displays pH value to the OLED Screen
    display.text('temp: ' + str(temperature) + ' C', 0, 30, 255)
    display.show()                          # Displays temp value to the OLED Screen

    # This will signal whether the aquarium is within the ideal range or not
    if (pH < 8 and pH > 6) and (temperature < 27 and temperature > 23):
        print("The aquarium is in ideal condition!")
        display.text("The aquarium ", 10, 70, 255)
        display.show()
        display.text("is in optimal ", 10, 80, 255)
        display.show()
        display.text("condition!!", 20, 90, 255)
        display.show()
        #display.invert(true)
        pycom.rgbled(0x00FF00)               # pycom's built-in LED device will emit GREEN light

    else:
        print("The aquarium is not within the optimal range!")
        display.text("The aquarium is ", 0, 70, 255)
        display.show()
        display.text("not within the ", 5, 80, 255)
        display.show()
        display.text("optimal range!", 5, 90, 255)
        display.show()
        pycom.rgbled(0xFF0000)               # pycom's built-in LED device will emit RED light
        play_tune()                          # plays the super mario melody to alert the user

    send_data_to_pybytes(pH, temperature)    # sends data to pybytes
    print("send_data_to_pybytes")
    sending_data_to_ubidots("pycom", temperature, 1, pH)   # sends data to ubidots
    print("sending_data_to_ubidots")
    time.sleep(600)                          # signal is send every 10 min

```
Here in the main file, we first start by importing the libraries, then we do our declarations, instantiations, pin assignments and network setup. After that we proceed with defining our functions (used for sending temperature and pH signal to PyBytes and Ubidots as well as for playing the 'Super Mario Bros.' theme song to alert as when a spike or drop in value happens). And finally, in the while loop we're getting the temperature and pH value, emit red or green light to indicate whether the values are within the optimal range or not, display it on our OLED Screen and make function calls to send the signals to the cloud. 

## Transmitting the data / connectivity

Since there is no LoRa gateway in my proximity and the aquarium is to be used indoors, the wireless protocol that i used for sending sensor data to the cloud is WiFi. Temperature and pH Data is transmitted every ten minutes to both platforms. When sending signal to *PyBytes*, the function **pybytes.sendsignal(signalnumber, value)** from the PyBytes API is used, while **webhook** (HTTP) is the transport protocol used to send data packaged in JSON-object format to [*Ubidots*](https://help.ubidots.com/en/articles/961994-connect-any-pycom-board-to-ubidots-using-wi-fi-over-http).

Although WiFi is not as battery hungry as LTE, it still consumes more battery power when compared with long-range low-consumption wiresless technologies like LoRa. In order to remedy that, i am using Battery holder with three rechargeable AAA NiMH Batteries to power my project. In addtion, device range is not an issue since the smart aquarium is used in a home environment.


## Presenting the data

Both PyBytes and Ubidots STEM use MongoDB for data storage and they retain your data for a month (**Note:** it's 24 months of data retention for **Ubidots**, the paid subscription). To persist the data, one could use integration to external services when using PyBytes (see Figure 10). You could create dasboards and alerts in both platforms (see figures 6-9). We'll be sending signal every 10 minutes and we will get notified regarding battery level and data storage in PyBytes and regarding pH and temperature spike/drop via sms and email in Ubidots STEM. 

For instructions on how to create dashboards, please follow this guide: [PyBytes](https://docs.pycom.io/pybytes/dashboard/), [Ubidots](https://help.ubidots.com/en/articles/2400308-create-dashboards-and-widgets).


![](https://i.imgur.com/YSJsJxl.png)
###### Figure 6. PyBytes Dashboard


![](https://i.imgur.com/3ImRGEv.png)
###### Figure 7. PyBytes Alerts


![](https://i.imgur.com/87NO3iT.png)
###### Figure 8. Ubidots Dashboard


![](https://i.imgur.com/T2azXHn.png)
###### Figure 9. Ubidots Alerts


![](https://i.imgur.com/9NzJqi1.jpg)

###### Figure 10. Ubidots email Notification



![](https://i.imgur.com/LSK4oUO.png)
###### Figure 11. Pybytes integration with WebHooks 


## Finalizing the design

As my first IoT project, i think it went pretty well. I would probably improve it by designing a 3D-model (for base and cover), replacing the 1.12" OLED screen with a 5″ TFT LCD for a wider display and by using LoRa.

[Video Demo:](https://www.youtube.com/watch?v=YS1NMDpvdA4
)

![](https://i.imgur.com/3GlihSj.jpg)
###### Figure 12. The electronic circuit

![](https://i.imgur.com/bF0eriT.jpg)
###### Figure 13. Data displayed on the OLED screen

![](https://i.imgur.com/X9qKO8Q.jpg)
###### Figure 14. The whole project


