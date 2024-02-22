from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
import random

# Criação de objetos
ev3 = EV3Brick()
motorRODAB=Motor(Port.B)
motorGrua=Motor(Port.C)
colordetetor=ColorSensor(Port.S1)
gyrodetetor=GyroSensor(Port.S2)
#inicializações
slotatual = 0
tipo_inimigo=[0,0,0,0,0,0]
numero_ataques_restantes=[0,0,0,0,0,0]
vida_inimigo=[0,0,0,0,0,0]
vida_robo=750
energia_robo=500
i=1
# tabelas
# tabela de ataque
ataquegrua=200
ataquetoque=100
ataquesom=50
consumogrua=300
consumotoque=150
consumosom=50
# tabela de levar dano
forcatanque=200
forcaartilharia=500
forcainfanteria=100
nattanque=2
natartilharia=1
natinfanteria=3
vidainitanque=200
vidainiartilharia=50
vidainiinfanteria=100
# tabela de vida para a cura
vida1=100
vida2=200
vida3=400
consumo1=200
consumo2=300
consumo3=400