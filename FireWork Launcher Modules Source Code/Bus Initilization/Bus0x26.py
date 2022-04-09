import time
import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c, 0x26)

pin = "pin"
getPin = " = mcp.get_pin("
getPinEnd = ") "
pinName = ""
pinList=[]
for i in range(16):
    pin+=str(i)
    getPin+=str(i)
    pinName+=str(pin)
    pinName+=str(getPin)
    pinName+=str(getPinEnd)
    pinList.append((pinName))
    pin = ""
    getPin = ""
    getPinEnd = ""
    pin = "pin"
    getPin = " = mcp.get_pin("
    getPinEnd = ") "
    pinName = ""
for i in range(16):
    exec(pinList[i])
pin = "pin"
DirectionIO = ".direction = Direction.OUTPUT"
pinName=""
pinList=[]
for i in range(16):
    pin+=str(i)
    pinName+=str(pin)
    pinName+=str(DirectionIO)
    pinList.append((pinName))
    pin = ""
    DirectionIO = ""
    pin = "pin"
    DirectionIO = ".direction = Direction.OUTPUT"
    pinName=""
for i in range(16):
    exec(pinList[i])
