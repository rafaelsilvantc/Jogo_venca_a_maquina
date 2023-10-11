#Antonio Rafael da Silva Ferreira
#2 TDS A         11/10/2023
#-------------------------------------------------------------------------------------------------------------------
#Refiz o código implementando a biblioteca "os" e usando ela para limpar o terminal entre cada interação           |                     
#Identei, comentei, otimizei e remodelei a ideia principal dentro de uma nova perspectiva, que seria a de um jogo. |                     
#Segue o conteudo  abaixo                                                                                          |                                          
#-------------------------------------------------------------------------------------------------------------------

#Importação das ferramentas e bilbliotecas
import os                                                     
from time import sleep                                        
from random import randint                                    

#Definição das variáveis usadas no programa
rodadas = 0                                         
acerto = 0                                          
erro = 0                                            
continua = 0  

#Menu principal e o Laço de repetição para realizar a transição do jogo para o Menu principal
while True:
    os.system("cls")
    continua = 0 
    print("*********************************************************")
    print("|                     Bem-vindo!                        |")
    print("|                                                       |")
    print("|                                                       |")
    print("|       Obrigado por adquirir o nosso jogo!             |")
    print('|                "Vença a máquina"                      |')
    print("|                                                       |")
    print("|    1- Iniciar jogo            2- Mostrar o placar     |")
    print("|                                                       |")
    print("|                     3- Sair                           |")
    print("|                                                       |")
    print("*********************************************************")

    iniciar = str(input("Resposta: "))
    #Condicional que Verifica se o jogo vai ser iniciado
    if iniciar == "1":
        while rodadas < 10:
           
            #Inicio do jogo
            os.system("cls")
            print('****************************************************************************************')
            print('|  Estou pensando em um número, será que você consegue adivinhar? Aguarde um momento!  |')
            print('****************************************************************************************')
            
            #Comando que cria um delay entre o "Pensamento da maquina" e a resposta do usuario
            sleep(3)
            
            #Comando que faz a maquina escolher um número aleatorio entre 0 e 5
            pc = randint(0, 5)

            os.system("cls")
            print('****************************************************************************************')
            print('|                            Pensei em um número, de 0 a 5                             |')
            print("|                         Qual número você acha que eu pensei?                         |")
            print('****************************************************************************************')
            
            jogador = int(input("Resposta: "))
            os.system("cls")

            #Condicionais que verificam se usuario acertou ou errou
            if jogador == pc:
                acerto = acerto+1
                rodadas = rodadas+1
                print("*******************************")
                print('|  Caramba! você acertou!     |')
                print("|     Eu pensei em", pc, "        |")
                print('|      Rodada nº', rodadas, "           |")
                print("| Aperte Enter para continuar!|")
                print("*******************************")
                input()
            else:
                erro += 1
                rodadas += 1
                print("*************************************")
                print('| Muahahaha! Você perdeu pra mim!   |')
                print('|        Eu pensei em', pc, "            |")
                print('|         Rodada nº', rodadas, '              |')
                print("*************************************")
                input()
            os.system("cls")
            
            #Escrita do placar
            print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print('[           PLACAR            ]')
            print("[                             ]")
            print("[    {} Acerto  x {} Erro       ]".format(acerto, erro))
            print("[                             ]")
            print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            input()
            
            
            #Painel de Interação entre cada rodada
            os.system("cls")
            print("*********************************************************")
            print("|                  VENÇA A MÁQUINA!                     |")
            print("|                                                       |")
            print("|               Você deseja Continuar?                  |")
            print("|                                                       |")
            print("|                                                       |")
            print("|    1- Continuar          2- Voltar ao menu principal  |")
            print("|                                                       |")
            print("|                                                       |")
            print("|                                                       |")
            print("*********************************************************")
            continua = input("Resposta: ")

            
            #Condicional que quebra o laço de repetição levando o usario de volta para o menu
            if continua == "2":
                os.system("cls")
                print("*******************************")
                print("|  Voltando ao menu inicial!  |")
                print("| Aperte Enter para continuar |")
                print("*******************************")
                input()
                break
    
    
    #Condicional  que verifica se o usuario vai fechar o jogo
    elif iniciar == "3":
        os.system("cls")
        print("*******************")
        print("|  Volte sempre!  |")
        print("*******************")
        input()
        break
   
   #Condicional que verifica se o usuario abriu o placar
    elif iniciar == "2":
        os.system("cls")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('[           PLACAR            ]')
        print("[                             ]")
        print("[     {} Acerto  x {} Erro      ]".format(acerto, erro))
        print("[                             ]")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input()
    
    #Else que nega as respostas inválidas e leva o usuario de volta para o menu
    else:
        os.system("cls")
        print("*************************")
        print("|   Resposta inválida!  |")
        print("*************************")
        input()

#----------------------------------------------------------------------------------- FIM DO PROGRAMA