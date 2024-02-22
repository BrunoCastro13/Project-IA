from parameters import *

def atacar(n,energia_robo,slotatual): #função para atacar um inimigo 
    print("Vou dar o ataque",n)
    if (n == "grua"):
        energia_robo=ataque_de_grua(energia_robo,consumogrua,vida_inimigo,slotatual)
    elif (n == "toque"):
        energia_robo=ataque_de_toque(energia_robo,consumotoque,vida_inimigo,slotatual)
    elif (n == "som"):
        energia_robo=ataque_de_som(energia_robo,consumosom,vida_inimigo,slotatual)
    return energia_robo

def curar(n): #função para ganhar a vida, verificando que tem energia suficiente
    global energia_robo
    global vida_robo
    if n == 0:
        if energia_robo>=consumo1:
            vida_robo+=vida1
    elif n == 1:
        if energia_robo>=consumo2:
            vida_robo+=vida2
    elif n == 2:
        if energia_robo>=consumo3:
            vida_robo+=vida3
    return vida_robo
# ------------------------------------------------------------------------
def ataque_de_grua(energia_robo,consumogrua,vida_inimigo,slotatual):
    # ---------------------------ATAQUE DE GRUA---------------------------
    if energia_robo>=consumogrua: #verifica se tem energia suficiente para o ataque
        # vida_inimigo[slotatual]=vida_inimigo[slotatual]-ataquegrua #retira vida ao inimigo
        # energia_robo=energia_robo-consumogrua #retira energia ao robo
        
        if vida_inimigo[slotatual]<=0: #verifica se o inimigo tem vida
            tipo_inimigo[slotatual]=0 #inimigo morreu
            vida_inimigo[slotatual]=0
        # print(tipo_inimigo[slotatual])
        # print(vida_inimigo[slotatual])
        #ataque
        #grua para a frente e para tras 90º
        motorGrua.run_angle(720,90, then=Stop.BRAKE, wait=True)
        motorGrua.run_angle(720,-90, then=Stop.BRAKE, wait=True)
    return energia_robo

def ataque_de_toque(energia_robo,consumotoque,vida_inimigo,slotatual):
    # ---------------------------ATAQUE DE TOQUE--------------------------
    if energia_robo>=consumotoque: #verifica se te energia suficiente para o ataque
        # vida_inimigo[slotatual]=vida_inimigo[slotatual]-ataquetoque #retira vida ao inimigo
        # energia_robo=energia_robo-consumotoque #retira energia ao robo
        if vida_inimigo[slotatual]<=0: #verifica se o inimigo tem vida
            tipo_inimigo[slotatual]=0 #inimigo morreu
            vida_inimigo[slotatual]=0
        # print(tipo_inimigo[slotatual])
        # print(vida_inimigo[slotatual])
        #ataque
        #grua para a frente e para tras 20º
        motorGrua.run_angle(720,20, then=Stop.BRAKE, wait=True)
        motorGrua.run_angle(720,-20, then=Stop.BRAKE, wait=True)
    return energia_robo

def ataque_de_som(energia_robo,consumosom,vida_inimigo,slotatual):
    # ---------------------------ATAQUE DE SOM--------------------------
    if energia_robo>=consumosom: #verifica se tem energia suficiente para o ataque
        # vida_inimigo[slotatual]=vida_inimigo[slotatual]-ataquesom #retira vida ao inimigo
        # energia_robo=energia_robo-consumosom #retira energia ao robo
        if vida_inimigo[slotatual]<=0: #verifica se o inimigo tem vida
            tipo_inimigo[slotatual]=0 # inimigo morreu
            vida_inimigo[slotatual]=0
        # print(tipo_inimigo[slotatual])
        # print(vida_inimigo[slotatual])
        #ataque
        #barulho irritante :)
        ev3.speaker.set_volume(50,'_all_')
        ev3.speaker.play_file("som.mp3")
    return energia_robo

def colortoenemie(color): #converte a cor lida para o valor do inimigo
    if color==Color.YELLOW or color==Color.BROWN: # tanque
        return 1
    elif color==Color.RED: # artilharia
        return 2
    elif color==Color.BLUE: # infantaria
        return 3
    else:
        return 0
def enemietoname(n): #converte o valor do inimigo para uma string do nome do mesmo
    if n==1:
        return "Tanque"
    elif n==2:
        return "Artilharia"
    elif n==3:
        return "Infanteria"
def criarinimigo(slotatual): #da a vida inicial ao inimigo na primeira vez que o detetar
    tipo_inimigo[slotatual]=colortoenemie(colordetetor.color())
    if tipo_inimigo[slotatual] == 1:
        print("Tanque criado")
        vida_inimigo[slotatual]=vidainitanque
        numero_ataques_restantes[slotatual]=nattanque
    elif tipo_inimigo[slotatual] == 2:
        print("Artilharia criado")
        vida_inimigo[slotatual]=vidainiartilharia
        numero_ataques_restantes[slotatual]=natartilharia
    elif tipo_inimigo[slotatual] == 3:
        print("Infantaria criada")
        vida_inimigo[slotatual]=vidainiinfanteria
        numero_ataques_restantes[slotatual]=natinfanteria

def levardano(slotatual): #leva dano do inimigo na posição atual
    dano_ao_robo = 0
    if numero_ataques_restantes[slotatual]!=0:
        if tipo_inimigo[slotatual] == 1:
            dano_ao_robo=vida_inimigo[slotatual]/vidainitanque*forcatanque
            numero_ataques_restantes[slotatual]=numero_ataques_restantes[slotatual]-1
        elif tipo_inimigo[slotatual] == 2:
            dano_ao_robo=vida_inimigo[slotatual]/vidainiartilharia*forcaartilharia
            numero_ataques_restantes[slotatual]=numero_ataques_restantes[slotatual]-1
        elif tipo_inimigo[slotatual] == 3:
            dano_ao_robo=vida_inimigo[slotatual]/vidainiinfanteria*forcainfanteria
            numero_ataques_restantes[slotatual]=numero_ataques_restantes[slotatual]-1
        print("Levou dano de", enemietoname(tipo_inimigo[slotatual]),"e perdeu ",dano_ao_robo,"de vida.")
    return dano_ao_robo

def verificarnataques(n): #verifica o número de ataques consoante o inimigo
    if n==1:
        return nattanque
    elif n==2:
        return natartilharia 
    elif n==3:
        return natinfanteria 
    else:
        return 0