#!/usr/bin/python3
from __future__ import print_function
import eel
import time
import os
import board
import busio
import sys
import multiprocessing
from digitalio import Direction
from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.SCL, board.SDA)
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
mcp = PCF8574_GPIO(0x27)
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)
mcp.output(3,1)
lcd.begin(20,4)
from rpi_lcd import LCD
@eel.expose
def initialize():
    lcd.setCursor(3,1)
    lcd.message('Initializing')
    lcd.setCursor(3,2)
    lcd.message('Raspi_Launcher')
    time.sleep(2.0)
    lcd.clear()

initialize()
try:
    from Bus0x20 import *
except ValueError:
    print("Relay Board 1 Not Connected")
try:
    from ConvertPin0x21 import *
except ValueError:
    print("Relay Board 2 Not Connected")
try:
    from ConvertPin0x22 import *
except ValueError:
    print("Relay Board 3 Not Connected")
try:
    from ConvertPin0x23 import *
except ValueError:
    print("Relay Board 4 Not Connected")
try:
    from ConvertPin0x24 import *
except ValueError:
    print("Relay Board 5 Not Connected")
try:
    from ConvertPin0x25 import *
except ValueError:
    print("Relay Board 6 Not Connected")
try:
    from ConvertPin0x26 import *
except ValueError:
    print("Relay Board 7 Not Connected")
try:
    from ConvertPin0x27 import *
except ValueError:
    print("Relay Board 8 Not Connected")

@eel.expose
def shutdown():
    lcd.setCursor(3,1)
    lcd.message('Shutting Down')
    lcd.setCursor(3,2)
    lcd.message('Raspi_Launcher')
    time.sleep(2.0)
    lcd.clear()

def confirmationMessage(pin, id, tst3):
    tst3.append(id)
    for string in tst3:
        print(tst3)
        while len(tst3) > 0:
            if len(tst3) >= 1:
                lcd.setCursor(0,0)
                lcd.message("Fired Cue #" + str(tst3[0]))
                time.sleep(1)
                tst3.pop(0)
                lcd.clear()
                lcd.clear()
                lcd.clear()
                lcd.clear()
                print(tst3)
            elif len(tst3) == 0:
                tst3.pop(0)
                lcd.clear()
                lcd.clear()
                lcd.clear()
                lcd.clear()

def fire(pin, id, tst3):
    prefiring = multiprocessing.Process(target = firing, args = (pin, id, tst3))
    prefiring.start()


def firing(pin, id, tst3):
    pin.value = False
    time.sleep(1.85)
    pin.value = True
    display = multiprocessing.Process(target=confirmationMessage, args = (pin, id, tst3))
    display.start()


eel.init('web')
@eel.expose
def Fired(elementId, tst3):
    id = elementId.strip("button")
    if id == "1":
        print("Cue 1 Fired")
        pin = pin0
        fire(pin, id, tst3)
    elif id == "2":
        print("Cue 2 Fired")
        pin = pin1
        fire(pin, id, tst3)
    elif id == "3":
        print("Cue 3 Fired")
        pin = pin2
        fire(pin, id, tst3)
    elif id == "4":
        print("Cue 4 Fired")
        pin = pin3
        fire(pin, id, tst3)
    elif id == "5":
        print("Cue 5 Fired")
        pin = pin4
        fire(pin, id, tst3)
    elif id == "6":
        print("Cue 6 Fired")
        pin = pin5
        fire(pin, id, tst3)
    elif id == "7":
        print("Cue 7 Fired")
        pin = pin6
        fire(pin, id, tst3)
    elif id == "8":
        print("Cue 8 Fired")
        pin = pin7
        fire(pin, id, tst3)
    elif id == "9":
        print("Cue 9 Fired")
        pin = pin8
        fire(pin, id, tst3)
    elif id == "10":
        print("Cue 10 Fired")
        pin = pin9
        fire(pin, id, tst3)
    elif id == "11":
        print("Cue 11 Fired")
        pin = pin10
        fire(pin, id, tst3)
    elif id == "12":
        print("Cue 12 Fired")
        pin = pin11
        fire(pin, id, tst3)
    elif id == "13":
        print("Cue 13 Fired")
        pin = pin12
        fire(pin, id, tst3)
    elif id == "14":
        print("Cue 14 Fired")
        pin = pin13
        fire(pin, id, tst3)
    elif id == "15":
        print("Cue 15 Fired")
        pin = pin14
        fire(pin, id, tst3)
    elif id == "16":
        print("Cue 16 Fired")
        pin = pin15
        fire(pin, id, tst3)
    elif id == "17":
        print("Cue 17 Fired")
        pin = pin16
        fire(pin, id, tst3)
    elif id == "18":
        print("Cue 18 Fired")
        pin = pin17
        fire(pin, id, tst3)
    elif id == "19":
        print("Cue 19 Fired")
        pin = pin18
        fire(pin, id, tst3)
    elif id == "20":
        print("Cue 20 Fired")
        pin = pin19
        fire(pin, id, tst3)
    elif id == "21":
        print("Cue 21 Fired")
        pin = pin20
        fire(pin, id, tst3)
    elif id == "22":
        print("Cue 22 Fired")
        pin = pin21
        fire(pin, id, tst3)
    elif id == "23":
        print("Cue 23 Fired")
        pin = pin22
        fire(pin, id, tst3)
    elif id == "24":
        print("Cue 24 Fired")
        pin = pin23
        fire(pin, id, tst3)
    elif id == "25":
        print("Cue 25 Fired")
        pin = pin24
        fire(pin, id, tst3)
    elif id == "26":
        print("Cue 26 Fired")
        pin = pin25
        fire(pin, id, tst3)
    elif id == "27":
        print("Cue 27 Fired")
        pin = pin26
        fire(pin, id, tst3)
    elif id == "28":
        print("Cue 28 Fired")
        pin = pin27
        fire(pin, id, tst3)
    elif id == "29":
        print("Cue 29 Fired")
        pin = pin28
        fire(pin, id, tst3)
    elif id == "30":
        print("Cue 30 Fired")
        pin = pin29
        fire(pin, id, tst3)
    elif id == "31":
        print("Cue 31 Fired")
        pin = pin30
        fire(pin, id, tst3)
    elif id == "32":
        print("Cue 32 Fired")
        pin = pin31
        fire(pin, id, tst3)
    elif id == "33":
        print("Cue 33 Fired")
        pin = pin32
        fire(pin, id, tst3)
    elif id == "34":
        print("Cue 34 Fired")
        pin = pin33
        fire(pin, id, tst3)
    elif id == "35":
        print("Cue 35 Fired")
        pin = pin34
        fire(pin, id, tst3)
    elif id == "36":
        print("Cue 36 Fired")
        pin = pin35
        fire(pin, id, tst3)
    elif id == "37":
        print("Cue 37 Fired")
        pin = pin36
        fire(pin, id, tst3)
    elif id == "38":
        print("Cue 38 Fired")
        pin = pin37
        fire(pin, id, tst3)
    elif id == "39":
        print("Cue 39 Fired")
        pin = pin38
        fire(pin, id, tst3)
    elif id == "40":
        print("Cue 40 Fired")
        pin = pin39
        fire(pin, id, tst3)
    elif id == "41":
        print("Cue 41 Fired")
        pin = pin40
        fire(pin, id, tst3)
    elif id == "42":
        print("Cue 42 Fired")
        pin = pin41
        fire(pin, id, tst3)
    elif id == "43":
        print("Cue 43 Fired")
        pin = pin42
        fire(pin, id, tst3)
    elif id == "44":
        print("Cue 44 Fired")
        pin = pin43
        fire(pin, id, tst3)
    elif id == "45":
        print("Cue 45 Fired")
        pin = pin44
        fire(pin, id, tst3)
    elif id == "46":
        print("Cue 46 Fired")
        pin = pin45
        fire(pin, id, tst3)
    elif id == "47":
        print("Cue 47 Fired")
        pin = pin46
        fire(pin, id, tst3)
    elif id == "48":
        print("Cue 48 Fired")
        pin = pin47
        fire(pin, id, tst3)
    elif id == "49":
        print("Cue 49 Fired")
        pin = pin48
        fire(pin, id, tst3)
    elif id == "50":
        print("Cue 50 Fired")
        pin = pin49
        fire(pin, id, tst3)
    elif id == "51":
        print("Cue 51 Fired")
        pin = pin50
        fire(pin, id, tst3)
    elif id == "52":
        print("Cue 52 Fired")
        pin = pin51
        fire(pin, id, tst3)
    elif id == "53":
        print("Cue 53 Fired")
        pin = pin52
        fire(pin, id, tst3)
    elif id == "54":
        print("Cue 54 Fired")
        pin = pin53
        fire(pin, id, tst3)
    elif id == "55":
        print("Cue 55 Fired")
        pin = pin54
        fire(pin, id, tst3)
    elif id == "56":
        print("Cue 56 Fired")
        pin = pin55
        fire(pin, id, tst3)
    elif id == "57":
        print("Cue 57 Fired")
        pin = pin56
        fire(pin, id, tst3)
    elif id == "58":
        print("Cue 58 Fired")
        pin = pin57
        fire(pin, id, tst3)
    elif id == "59":
        print("Cue 59 Fired")
        pin = pin58
        fire(pin, id, tst3)
    elif id == "60":
        print("Cue 60 Fired")
        pin = pin59
        fire(pin, id, tst3)
    elif id == "61":
        print("Cue 61 Fired")
        pin = pin60
        fire(pin, id, tst3)
    elif id == "62":
        print("Cue 62 Fired")
        pin = pin61
        fire(pin, id, tst3)
    elif id == "63":
        print("Cue 63 Fired")
        pin = pin62
        fire(pin, id, tst3)
    elif id == "64":
        print("Cue 64 Fired")
        pin = pin63
        fire(pin, id, tst3)
    elif id == "65":
        print("Cue 65 Fired")
        pin = pin64
        fire(pin, id, tst3)
    elif id == "66":
        print("Cue 66 Fired")
        pin = pin65
        fire(pin, id, tst3)
    elif id == "67":
        print("Cue 67 Fired")
        pin = pin66
        fire(pin, id, tst3)
    elif id == "68":
        print("Cue 68 Fired")
        pin = pin67
        fire(pin, id, tst3)
    elif id == "69":
        print("Cue 69 Fired")
        pin = pin68
        fire(pin, id, tst3)
    elif id == "70":
        print("Cue 70 Fired")
        pin = pin69
        fire(pin, id, tst3)
    elif id == "71":
        print("Cue 71 Fired")
        pin = pin70
        fire(pin, id, tst3)
    elif id == "72":
        print("Cue 72 Fired")
        pin = pin71
        fire(pin, id, tst3)
    elif id == "73":
        print("Cue 73 Fired")
        pin = pin72
        fire(pin, id, tst3)
    elif id == "74":
        print("Cue 74 Fired")
        pin = pin73
        fire(pin, id, tst3)
    elif id == "75":
        print("Cue 75 Fired")
        pin = pin74
        fire(pin, id, tst3)
    elif id == "76":
        print("Cue 76 Fired")
        pin = pin75
        fire(pin, id, tst3)
    elif id == "77":
        print("Cue 77 Fired")
        pin = pin76
        fire(pin, id, tst3)
    elif id == "78":
        print("Cue 78 Fired")
        pin = pin77
        fire(pin, id, tst3)
    elif id == "79":
        print("Cue 79 Fired")
        pin = pin78
        fire(pin, id, tst3)
    elif id == "80":
        print("Cue 80 Fired")
        pin = pin79
        fire(pin, id, tst3)
    elif id == "81":
        print("Cue 81 Fired")
        pin = pin80
        fire(pin, id, tst3)
    elif id == "82":
        print("Cue 82 Fired")
        pin = pin81
        fire(pin, id, tst3)
    elif id == "83":
        print("Cue 83 Fired")
        pin = pin82
        fire(pin, id, tst3)
    elif id == "84":
        print("Cue 84 Fired")
        pin = pin83
        fire(pin, id, tst3)
    elif id == "85":
        print("Cue 85 Fired")
        pin = pin84
        fire(pin, id, tst3)
    elif id == "86":
        print("Cue 86 Fired")
        pin = pin85
        fire(pin, id, tst3)
    elif id == "87":
        print("Cue 87 Fired")
        pin = pin86
        fire(pin, id, tst3)
    elif id == "88":
        print("Cue 88 Fired")
        pin = pin87
        fire(pin, id, tst3)
    elif id == "89":
        print("Cue 89 Fired")
        pin = pin88
        fire(pin, id, tst3)
    elif id == "90":
        print("Cue 90 Fired")
        pin = pin89
        fire(pin, id, tst3)
    elif id == "91":
        print("Cue 91 Fired")
        pin = pin90
        fire(pin, id, tst3)
    elif id == "92":
        print("Cue 92 Fired")
        pin = pin91
        fire(pin, id, tst3)
    elif id == "93":
        print("Cue 93 Fired")
        pin = pin92
        fire(pin, id, tst3)
    elif id == "94":
        print("Cue 94 Fired")
        pin = pin93
        fire(pin, id, tst3)
    elif id == "95":
        print("Cue 95 Fired")
        pin = pin94
        fire(pin, id, tst3)
    elif id == "96":
        print("Cue 96 Fired")
        pin = pin95
        fire(pin, id, tst3)
    elif id == "97":
        print("Cue 97 Fired")
        pin = pin96
        fire(pin, id, tst3)
    elif id == "98":
        print("Cue 98 Fired")
        pin = pin97
        fire(pin, id, tst3)
    elif id == "99":
        print("Cue 99 Fired")
        pin = pin98
        fire(pin, id, tst3)
    elif id == "100":
        print("Cue 100 Fired")
        pin = pin99
        fire(pin, id, tst3)
    elif id == "101":
        print("Cue 101 Fired")
        pin = pin100
        fire(pin, id, tst3)
    elif id == "102":
        print("Cue 102 Fired")
        pin = pin101
        fire(pin, id, tst3)
    elif id == "103":
        print("Cue 103 Fired")
        pin = pin102
        fire(pin, id, tst3)
    elif id == "104":
        print("Cue 104 Fired")
        pin = pin103
        fire(pin, id, tst3)
    elif id == "105":
        print("Cue 105 Fired")
        pin = pin104
        fire(pin, id, tst3)
    elif id == "106":
        print("Cue 106 Fired")
        pin = pin105
        fire(pin, id, tst3)
    elif id == "107":
        print("Cue 107 Fired")
        pin = pin106
        fire(pin, id, tst3)
    elif id == "108":
        print("Cue 108 Fired")
        pin = pin107
        fire(pin, id, tst3)
    elif id == "109":
        print("Cue 109 Fired")
        pin = pin108
        fire(pin, id, tst3)
    elif id == "110":
        print("Cue 110 Fired")
        pin = pin109
        fire(pin, id, tst3)
    elif id == "111":
        print("Cue 111 Fired")
        pin = pin110
        fire(pin, id, tst3)
    elif id == "112":
        print("Cue 112 Fired")
        pin = pin111
        fire(pin, id, tst3)
    elif id == "113":
        print("Cue 113 Fired")
        pin = pin112
        fire(pin, id, tst3)
    elif id == "114":
        print("Cue 114 Fired")
        pin = pin113
        fire(pin, id, tst3)
    elif id == "115":
        print("Cue 115 Fired")
        pin = pin114
        fire(pin, id, tst3)
    elif id == "116":
        print("Cue 116 Fired")
        pin = pin115
        fire(pin, id, tst3)
    elif id == "117":
        print("Cue 117 Fired")
        pin = pin116
        fire(pin, id, tst3)
    elif id == "118":
        print("Cue 118 Fired")
        pin = pin117
        fire(pin, id, tst3)
    elif id == "119":
        print("Cue 119 Fired")
        pin = pin118
        fire(pin, id, tst3)
    elif id == "120":
        print("Cue 120 Fired")
        pin = pin119
        fire(pin, id, tst3)
    elif id == "121":
        print("Cue 121 Fired")
        pin = pin120
        fire(pin, id, tst3)
    elif id == "122":
        print("Cue 122 Fired")
        pin = pin121
        fire(pin, id, tst3)
    elif id == "123":
        print("Cue 123 Fired")
        pin = pin122
        fire(pin, id, tst3)
    elif id == "124":
        print("Cue 124 Fired")
        pin = pin123
        fire(pin, id, tst3)
    elif id == "125":
        print("Cue 125 Fired")
        pin = pin124
        fire(pin, id, tst3)
    elif id == "126":
        print("Cue 126 Fired")
        pin = pin125
        fire(pin, id, tst3)
    elif id == "127":
        print("Cue 127 Fired")
        pin = pin126
        fire(pin, id, tst3)
    elif id == "128":
        print("Cue 128 Fired")
        pin = pin127
        fire(pin, id, tst3)

    else:
        print("Error Invalid Input")
@eel.expose
def ResetScreen():
    lcd.home()
    lcd.noCursor()
    lcd.clear()
    lcd.clear()
    lcd.clear()
@eel.expose
def ExitScript():
    exit()
eel.start('index.html', host='192.168.0.2', port=80)
