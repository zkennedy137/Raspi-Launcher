from Bus0x26 import pin0
from Bus0x26 import pin1
from Bus0x26 import pin2
from Bus0x26 import pin3
from Bus0x26 import pin4
from Bus0x26 import pin5
from Bus0x26 import pin6
from Bus0x26 import pin7
from Bus0x26 import pin8
from Bus0x26 import pin9
from Bus0x26 import pin10
from Bus0x26 import pin11
from Bus0x26 import pin12
from Bus0x26 import pin13
from Bus0x26 import pin14
from Bus0x26 import pin15
from Bus0x26 import pin16
pin = "pin"
equal = " = "
pinName=""
pinn = "pin"
z = 0
pinList=[]
for i in range(96, 112):
    pin+=str(i)
    pinn+=str(z)
    pinName+=str(pin)
    pinName+=str(equal)
    pinName+=str(pinn)
    pinList.append((pinName))
    pin = "pin"
    pinn = "pin"
    equal= " = "
    pinName=""
    z+=1
for i in range(16):
    exec(pinList[i])
print(pinList)