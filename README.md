# MCP3008 with Raspberry Pi
## Introduction
  This module provide some method using MCP3008. If you want to use this module, you have to enable SPI on your Raspberry Pi and install spi-dev. This README tell you how to do them.
  I assume that you use Raspbian on your Raspberry Pi.

## Usage
### Sample Code
```
#!/usr/bin/env python

from MCP3008Pi import mcp3008

mcp = mcp3008.MCP3008(1,2)

print(mcp.read(0))

mcp.close()
```

### Enable SPI on Your Raspberry Pi
  You run the following script on terminal. This process need about  20-30 minitus.
```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
```

  You choose Menu=>Preference=>Raspberry Pi Configuration=>Interface=>SPI and select enable.
  Then you reboot your raspberry Pi

### Install spidev
  You run the following script on your terminal.
```
cd ~
git clone git://github.com/doceme/py-spidev
cd py-spidev
sudo python setup.py install
```

##Confirm spi

```
python
import spidev
```
If you not get some error, sucess install spidev.


