
## Overview
I love RISC-V. Maybe cuz I worked on it for a long time during my internship at Huawei and I sort of know the instruction set inside out. I want to make a board using the ESP32-C3, cuz its cheap.

## Documents
- [Hardware Design Guidelines](https://www.espressif.com/sites/default/files/documentation/esp32-c3_hardware_design_guidelines_en.pdf): must-have components on the PCB and recommended specs
- [Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf): not much use for an MCU, mostly refer to the pin configurations and numbers
- [Technical Reference Manual](file:///C:/Users/peter/Downloads/esp32-c3_technical_reference_manual_cn.pdf): internal workings of the chip, not too important until you need to fiddle with the registers

## Minimal Board Setup
### Digital Power
- Use recommended cap values

### Analog Power Supply
- Use recommended LC filter and caps

### Power-on sequence
- Use RC delay / latch circuit to delay power-on after 3.3V has stabilised

### Clock Crystal
- 10ppm and 40MHz
- Capacitor values: https://blog.adafruit.com/2012/01/24/choosing-the-right-crystal-and-caps-for-your-design/

### RF Circuit
- pi-matching is ideal but not compulsory, its just a lower gain mate

### Strapping Bins (i.e. boot config)
- GPIO 2, 8, 9
- just do pull-up or pull-down resistors and jumper wire

## Use CDC USB
Using CDC USB for serial console and programming means you can save the space of a CH340g. Just set your serial console output in ESP-IDF to CDC USB