# O código da Lobotomy CinCorporation!
def malkuth (energianecessaria):
    # A Malkuth é a sefirá da organização, ela dará um teste para o aluno ter que receber um input com vários nomes e ter que ordenar pelo tamanho dos nomes.
    print ("Hoje é o dia da Malkuth!")
    print ("Malkuth: Ah, onde estão meus modos! Meu nome é Malkuth, e eu estou em cargo do time de controle!")
    print ("Malkuth: Estamos responsáveis hoje por organizar alfabeticamente nossa lista de funcionários do time de controle, vamos entregar com resultados perfeitos, gerente!")
    print ("")

    # Um exemplo de input: Roland Angela Netzach Yesod Hod
    listanomes = input().split()
    # Se caso nenhum funcionário estiver no time:
    if len(listanomes) == 0:
        print("Malkuth: Pessoal?! Onde está todo mundo?! Isso é inaceitável!")
        print ("")
        return 0

    # Bubblesort
    trocas = 0
    for i in range (len(listanomes)):
        for j in range (len(listanomes) - 1 - i):
            if (len(listanomes[j]) > len(listanomes[j + 1])):
                listanomes[j], listanomes[j + 1] = listanomes[j+1], listanomes[j]

                # Cada troca adicionará 1 na variável trocas para ser usado no manejo da energia.
                trocas += 1

    print(*listanomes)
    energia = max(0, 200 - trocas * 20)

    print(f"Energia Coletada: {energia} / {energianecessaria}")
    if energia >= energianecessaria:
        print ("Malkuth: O treino vespertino de hoje foi um sucesso! Estarei esperando vocês no período noturno, pessoal!")
        print ("")
        return 1
    else:
        print ("Malkuth: Ah não.. não conseguimos energia suficiente... amanhã eu dobrarei a carga horária para que a gente possa concluir o expediente com excelência!")
        print ("")
        return 0
    
def yesod(energianecessaria):
    return 0

def chesed(energianecessaria):
    return 0

def binah(energianecessaria):
    return 0

def dias(dia, energianecessaria):
    sefirot = input()

    if sefirot == 'Malkuth':
        diaconcluido = malkuth(energianecessaria)
        conclusaodias.append(diaconcluido)
    elif sefirot == "Yesod":
        diaconcluido = yesod(energianecessaria)
        conclusaodias.append(diaconcluido)
    elif sefirot == "Chesed":
        diaconcluido = chesed(energianecessaria)
        conclusaodias.append(diaconcluido)
    elif sefirot == "Binah":
        diaconcluido = binah(energianecessaria)
        conclusaodias.append(diaconcluido)
    else:
        print("Angela: Essa sefirot não está disponível hoje, gerente.")
        conclusaodias.append(0)

# Inicialização de Variáveis
dia = 1
conclusaodias = []
energianecessaria = 100
quantidade_de_dias = int(input())

print ("Hoje é o dia da Lobotomy CinCorporation!")
while (dia <= quantidade_de_dias):

    print (f"Angela: Hoje é o dia {dia} de {quantidade_de_dias}. Espero mais um expediente concluído com excelência, gerente.")
    dias(dia, energianecessaria)

    energianecessaria += 40
    dia += 1

print ("Angela O relatório dessa semana está pronto, gerente.")
for i in range(len(conclusaodias)):
    if conclusaodias[i]:
        print (f"Dia {i + 1} | Status: Energia necessária adquirida.")
    else:
        print (f"Dia {i + 1} | Status: Energia necessária não adquirida.")