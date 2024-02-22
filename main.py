#!/usr/bin/env pybricks-micropython

from parameters import *
from actions import *
from movement import *
from thoughts import *



def rondadano(): # função que ele leva dano e se não estiver ninguém naquele slot na ronda anterior, ele irá reconhecer
    global slotatual
    global vida_robo
    for h in range(6):
        time.sleep(5)
        print("Slot atual:", slotatual)
        vida_robo = vida_robo - levardano(slotatual) #leva o dano
        if tipo_inimigo[slotatual]==0: #adiciona um inimigo novo
            criarinimigo(slotatual)  
        rodar()
        slotatual = ((slotatual + 1) % 6) #proximo slot

def rondaataque():# função que dá dano ao inimigo
    global slotatual
    global energia_robo
    global vida_robo
    a=0
    ataque=False
    decisao_final=decidir_o_ataque(vida_robo,energia_robo) # vai verificar se deve atacar ou se deve curar (caso seja atacar, irá mandar uma lista com os ataques; caso seja curar, irá mandar um número entre 1 e 3 que são o tipo de cura)
    print("o que vou fazer:",decisao_final)
    if type(decisao_final) is list: #caso seja uma lista, ele irá atacar
        ataque=True
    if ataque==True: #flag que permite um ataque
        print("Slot atual:", slotatual) 
        while ataque==True: #este while deixa o robo rodar ate atacar, mas nao poe ataque a false quando ataca.
            time.sleep(1)   #em vez disso, poe ataque a false quando chega a ultima posiçao, rodando uma ultima vez para deixar o robo no slot 0 (primeiro slot)
            if slotatual==5:
                ataque=False
            if decisao_final[slotatual]!="": #apenas irá atacar caso esteja alguma coisa naquela posição da lista
                energia_robo=atacar(decisao_final[slotatual],energia_robo,slotatual) #faz o ataque e atualiza a energia do robo
            rodar()
            slotatual = ((slotatual + 1) % 6) #atualiza o slot atual, com uma funçao resto

def mostrarecra(): #função para mostrar ronda, tipo de ronda, vida e energia
    ev3.screen.clear()
    ev3.screen.print("Ronda:",i)
    print("Ronda:",i)
    if i%2!=0:
        ev3.screen.print("Defender")
        print("Defender")
    else:
        ev3.screen.print("Atacar")
        print("Atacar")
    ev3.screen.print("Vida:",vida_robo)
    print("Vida:",vida_robo)
    ev3.screen.print("Energia:",energia_robo)
    print("Energia:",energia_robo)

# Codigo principal
#corre as rondas, verificando primeiro se o robo nao morreu na ronda anterior, atualiza a energia
for i in range (1,14): #corre comandos de ataque se a ronda é ímpar, e defesa para rondas pares
    if vida_robo > 0: #se o robo tiver vida, ele irá continuar rondas
        mostrarecra()
        print("Inimigo:",tipo_inimigo)
        print("Vida do inimigo:",vida_inimigo)
        energia_robo=min(500,energia_robo*1.5)
        if i%2!=0:
            rondadano()
        elif i%2==0:
            rondaataque()
        time.sleep(5)
    else: # se não tiver vida, ele morre 
        print("Morri :(")
        ev3.screen.clear()
        ev3.screen.print("Morri :(")