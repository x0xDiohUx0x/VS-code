# Crie uma variável para armazenar o nome e a quantidade de 
# experiencia (XP) de um herói, deopis utilize uma estrutura
# de decisão para apresentar alguma das mensagens abaixo

#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 6.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante

#Ao final deve se exibir uma mensagem:
#"O Herói de nome **{nome}** está no nível de **{nivel}**"

Heroi = str ("Pica das Galaxias")
Nivel = int (1)

if (Nivel <= 1000):
    print ("O herói de nome" , Heroi , "está no nível de Ferro")

elif (1001 <= Nivel <= 2000):
    print ("O herói de nome" , Heroi , "está no nível de Bronze")

elif (2001 <= Nivel <= 6000):
    print ("O herói de nome" , Heroi , "está no nível de Prata")

elif (6001 <= Nivel <= 7000):
    print ("O herói de nome" , Heroi , "está no nível de Ouro")

elif (7001 <= Nivel <= 8000):
    print ("O herói de nome" , Heroi , "está no nível de Platina")    

elif (8001 <= Nivel <= 9000):
    print ("O herói de nome" , Heroi , "está no nível de Ascendente")    

elif (9001 <= Nivel <= 10000):
    print ("O herói de nome" , Heroi , "está no nível de Imortal")   

elif (Nivel >= 10000):
    print ("O herói de nome" , Heroi , "está no nível de Radiante")