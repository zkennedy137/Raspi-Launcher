import time
import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, 0x27)

pin = "pin"
getPin = " = mcp.get_pin("
getPinEnd = ") "
pinName = ""
nameList=[]
for i in range(16):
    pin +=str(i)
    getPin+=str(i)
    pinName+=str(pin)
    pinName+=str(getPin)
    pinName+=str(getPinEnd)
    nameList.append((pinName))
    pin = ""
    getPin = ""
    getPinEnd = ""
    pin = "pin"
    getPin = " = mcp.get_pin("
    getPinEnd = ") "
    pinName = ""