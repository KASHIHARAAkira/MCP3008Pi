#!/usr/bin/env python

#import necessary modules
import spidev

#MCP3008 module; arguments are bus and device.
class MCP3008:
  def __init__(self, bus, device):
    self.spi = spidev.SpiDev()	#create instance.
    self.spi.open(bus, device)	#bus is SPI port number, device is CS pin.

  def read(self, ch):				#An argument is used channel number
    var = self.spi.xfer2([0x01, (0x08+ch)<<4,0x00])	#first byte is start bit, second byte include control bit, third byte dummy byte.
    value = ((var[1]&0x03)<<8) + var[2]		#Decode byte to decimal
    voltage = (value * 3.3) / float(1024)	#Calculate voltage
    return voltage				#return voltage

  def close(self):				#MCP3008 close function
    self.spi.close()					#SPI close

