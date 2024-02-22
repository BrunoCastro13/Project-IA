from parameters import *

def rodar(): # rodar 60º para o slot seguinte
    global slotatual
    rotate=True
    gyrodetetor.reset_angle(0) #reset ao giroscopio para contar de 0 a 55
    while rotate==True:
        if gyrodetetor.angle()>=55:
            motorRODAB.stop()
            rotate=False
        else:
            motorRODAB.run(180)