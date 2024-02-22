from parameters import *
from actions import *

def calcular_dano_inimigo(slot): #função que calcula o dano a levar de uma dada posição
    if tipo_inimigo[slot]==1:
        return vida_inimigo[slot]/vidainitanque*forcatanque
    if tipo_inimigo[slot]==2:
        return vida_inimigo[slot]/vidainiartilharia*forcaartilharia
    if tipo_inimigo[slot]==3:
        return vida_inimigo[slot]/vidainiinfanteria*forcainfanteria
    return 0

def calcular_dano_total(): #calcula o dano de todos os slots
    slota=0
    total=0
    for i in range(6):
        total=total+calcular_dano_inimigo(slota)
        print("O dano total:", total)
        slota=slota+1
    return total

def efici_dano(slot): #função que indica quais os ataques deve dar, em deprimento do oponente e a vida do oponente, numa determinada posição
    if tipo_inimigo[slot]==2:
        return ["som"]
    elif tipo_inimigo[slot]==3:
        print(vida_inimigo[slot])
        if vida_inimigo[slot]>50:
            return ["som","toque"]
        else:
            return ["som"]
    elif tipo_inimigo[slot]==1:
        print(vida_inimigo[slot])
        if vida_inimigo[slot]<200:
            if vida_inimigo[slot]<100:
                return ["som"]
            else:
                return ["som","toque"]
        else:
            return ["som","toque","grua"]
    else:
        return []

def procura_artilharia(): #função que procura na lista todas as artilharias
    posi_arti=[]
    for i in range (6):
        if tipo_inimigo[i]==2:
            posi_arti.append(i)
    print("A posição da artilharia", posi_arti)
    return posi_arti
            

def procura_tanque(): #função que procura na lista todos os tanques
    posi_ta=[]
    for i in range(6):
        if tipo_inimigo[i]==1:
            posi_ta.append(i)
    print("A posição do tanque:", posi_ta)
    return posi_ta

def procura_infataria(): #função que procura na lista todas as infantarias
    posi_in=[]
    for i in range(6):
        if tipo_inimigo[i]==3:
            posi_in.append(i)
    print("A posição da infataria:", posi_in)
    return posi_in

def calcular_dano_inimigo_next(slot,vida_inimigo_next): #função que calcula o dano a levar mas na ronda a seguinte, em uma determinada posição
    
    if tipo_inimigo[slot]==1:
        return vida_inimigo_next[slot]/vidainitanque*forcatanque
    if tipo_inimigo[slot]==2:
        return vida_inimigo_next[slot]/vidainiartilharia*forcaartilharia
    if tipo_inimigo[slot]==3:
        return vida_inimigo_next[slot]/vidainiinfanteria*forcainfanteria
    return 0

def calcular_dano_total_next(ataque_acumulado,vida_inimigo_next): #função que tira a "vida" (não retira da lista principal, apenas da lista usadas para as heurísticas) e calcula o dano total  a levar na ronda a seguir, de todas as posições
    slota=0
    total=0
    for i in range(6):
        if ataque_acumulado[i]=="som":
            vida_inimigo_next[i]=vida_inimigo_next[i]-ataquesom
            if vida_inimigo_next[i]<0:
                vida_inimigo_next[i]=0
        if ataque_acumulado[i]=="toque":
            vida_inimigo_next[i]=vida_inimigo_next[i]-ataquetoque
            if vida_inimigo_next[i]<0:
                vida_inimigo_next[i]=0
        if ataque_acumulado[i]=="grua":
            vida_inimigo_next[i]=vida_inimigo_next[i]-ataquegrua
            if vida_inimigo_next[i]<0:
                vida_inimigo_next[i]=0
        total=total+calcular_dano_inimigo_next(slota,vida_inimigo_next)
        slota=slota+1
    print("A vida dos inimigos",vida_inimigo)
    print("Dano no proximo inimigo",total)
    return total


def decidir_o_ataque(vida_robo,energia_robo): #função que irá verificar se deve de atacar ou não
    ataque_acumulado=["","","","","",""]
    tipo_inimigo_next=tipo_inimigo #copia das listas para usar apenas nas heurísticas, bem como a sua energia
    vida_inimigo_next=vida_inimigo
    ene=energia_robo
    posicao_artilharia=procura_artilharia() #posições das artilharias
    posicao_tanque=procura_tanque() #posições dos tanques
    posicao_infataria=procura_infataria() #posições da infataria
    if posicao_artilharia!=[]: #primeiro será escolhido todos os ataques para todas as artilharias
        print("Vida do inimigo:",vida_inimigo)
        for a in posicao_artilharia:
            print("Energia:",ene)
            tipo_de_dano_ava_ava=efici_dano(a)
            ene=ene-consumosom
            if ene>=200: #garante que a eneriga nunca baixa de 200
                ataque_acumulado[a]="som"
            else:
                ene=ene+consumosom  
    elif posicao_tanque!=[]: #depois de todos os ataques escolhidos para as artilharias, será a vez dos tanques para ser selecionado os ataques
        print("Vida do inimigo:",vida_inimigo)
        for a in posicao_tanque:
            print("Energia:",ene)
            tipo_de_dano_ava=efici_dano(a)
            if tipo_de_dano_ava==["som"]:
                ene=ene-consumosom
                if ene>=200:#garante que a eneriga nunca baixa de 200
                    ataque_acumulado[a]="som"
                else:
                    ene=ene+consumosom
            elif tipo_de_dano_ava==["som","toque"]:
                ene=ene-consumotoque
                if ene>=200:#garante que a eneriga nunca baixa de 200
                    ataque_acumulado[a]="toque"
                else:
                    ene=ene+consumotoque
                    ene=ene-consumosom
                    if ene>=200:#garante que a eneriga nunca baixa de 200
                        ataque_acumulado[a]="som"
                    else:
                        ene=ene+consumosom
            elif tipo_de_dano_ava==["som","toque","grua"]:
                ene=ene-consumogrua
                if ene>=200:#garante que a eneriga nunca baixa de 200
                    ataque_acumulado[a]="grua"
                else:
                    ene=ene+consumogrua
                    ene=ene-consumotoque
                    if ene>=200:#garante que a eneriga nunca baixa de 200
                        ataque_acumulado[a]="toque"
                    else:
                        ene=ene+consumotoque
                        ene=ene-consumosom
                        if ene>=200:#garante que a eneriga nunca baixa de 200
                            ataque_acumulado[a]="som"
                        else:
                            ene=ene+consumosom
    elif posicao_infataria!=[]: #finalmente será escolhido os ataques para todas as infatarias
        print("Vida do inimigo:",vida_inimigo)
        for a in posicao_infataria:
            print("Energia:",ene)
            tipo_de_dano_ava=efici_dano(a)
            print("Efeciencia:",tipo_de_dano_ava)
            if tipo_de_dano_ava==["som"]:
                ene=ene-consumosom
                if ene>=200:#garante que a eneriga nunca baixa de 200
                    ataque_acumulado[a]="som"
                else:
                    ene=ene+consumosom
            elif tipo_de_dano_ava==["som","toque"]:
                ene=ene-consumotoque
                if ene>=200:#garante que a eneriga nunca baixa de 200
                    ataque_acumulado[a]="toque"
                else:
                    ene=ene+consumotoque
                    ene=ene-consumosom
                    if ene>=200:#garante que a eneriga nunca baixa de 200
                        ataque_acumulado[a]="som"
                    else:
                        ene=ene+consumosom
    print("Vida do inimigo:",vida_inimigo)
    dano_total=calcular_dano_total_next(ataque_acumulado,vida_inimigo_next) # irá calcular o dano total a levar na ronda seguinte
    print("Vida do inimigo:",vida_inimigo)
    print("Novo dano:",dano_total)
    if dano_total>=vida_robo: #caso o dano a levar na ronda a seguir for maior do que a vida atual do robo, ele irá tentar curar-se
        dano_total=calcular_dano_total() #atualiza o valor do dano total, sem dar tira vida aos inimigos
        decisao_curar=decidir_curar(dano_total,vida_robo,energia_robo) #irá retornar um valor entre 0 e 3, em que 0 não irá curar-se, simplesmente morre
        if decisao_curar!=0:
            curar(decisao_curar) #cura-se, dependendo da cura selecionado
            return decisao_curar # neste momento, o robo já se curou
        else:
            return 0
    else:
        print(ataque_acumulado)
        return ataque_acumulado #retorna a lista de ataques a dar

def decidir_curar(dano_total,vida_robo2,energia_robo):
    if vida_robo2<vida_robo: #verifica se a vida que o robo tem é menor da inicial
        if vida_robo2+vida1<dano_total: #verifica se a vida atual+vida a recuperar será menor que o dano que irá levar
            if energia_robo+200>consumo1: #verifica se ao curar irá ter mais de 200 de energia
                print("Usou a 1º Cura")
                return 1
        elif vida_robo2+vida2<dano_total:#verifica se a vida atual+vida a recuperar será menor que o dano que irá levar
            if energia_robo+200>consumo2:#verifica se ao curar irá ter mais de 200 de energia
                print("Usou a 2º Cura")
                return 2
        elif vida_robo2+vida3<dano_total:#verifica se a vida atual+vida a recuperar será menor que o dano que irá levar
            if energia_robo+200>consumo3:#verifica se ao curar irá ter mais de 200 de energia
                print("Usou a 3º Cura")
                return 3
        else: #senão ele irá morrer
            return 0
    else:#senão ele irá morrer
        return 0