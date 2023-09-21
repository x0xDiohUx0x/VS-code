#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões
#- Funções

## Objetivo:

#Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
#depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

#Se vitórias for menor do que 10 = Ferro
#Se vitórias for entre 11 e 20 = Bronze
#Se vitórias for entre 21 e 50 = Prata
#Se vitórias for entre 51 e 80 = Ouro
#Se vitórias for entre 81 e 90 = Diamante
#Se vitórias for entre 91 e 100= Lendário
#Se vitórias for maior ou igual a 101 = Imortal

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

vitorias = int (102)
derrotas = int (46)

niveisDeHeroi = ["Ferro", "Bronze", "Prata", "Ouro", "Diamante", "Lendário", "Imortal"]

saldoRankeadas = vitorias - derrotas


if (saldoRankeadas <= 10):
    print ("O Herói tem saldo de ", saldoRankeadas, "vitórias, e está no níve de", niveisDeHeroi[0])

elif (11 <= saldoRankeadas <=20 ):
    print ("O Herói tem saldo de ", saldoRankeadas, "e está no nível de", niveisDeHeroi[1])

elif (21 <= saldoRankeadas <=50 ):
    print ("O Herói tem saldo de ", saldoRankeadas, "e está no nível de", niveisDeHeroi[2])

elif (51 <= saldoRankeadas <=80 ):
    print ("O Herói tem saldo de ", saldoRankeadas, "e está no nível de", niveisDeHeroi[3])

elif (81 <= saldoRankeadas <=90 ):
    print ("O Herói tem saldo de ", saldoRankeadas, "e está no nível de", niveisDeHeroi[4])

elif (91 <= saldoRankeadas <=100 ):
    print ("O Herói tem saldo de ", saldoRankeadas, "e está no nível de", niveisDeHeroi[5])

elif (saldoRankeadas >= 101):
    print ("O Herói tem saldo de ", saldoRankeadas, "e está no nível de ", niveisDeHeroi [6])




    