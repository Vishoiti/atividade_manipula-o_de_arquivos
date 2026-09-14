import os 
os.system("cls")

while True:
    print("""
    0 - SAIR
    1 - Nome do arquivo
    2 - Gravar o arquivo
    3 - Ler o arquivo
    4 - Editar o arquivo
    5 - Gravar arquivo exclusivo
    """)
    try:
        opcao = int(input("Escolha um número: "))
    except ValueError:
        print("Digite apenas números!")
    except:
        print("ERRO!")
    match opcao:
        case 0:
            print("Fim do programa!")
            break