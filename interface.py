import os
from generator import gerar_senha_forte


def limpa_terminal():
    """
    Limpa o terminal, usando o comando adequado para o sistema operacional.

    Para sistemas Windows, utiliza o comando 'cls'.
    Para sistemas Unix-like (Linux, macOS), utiliza o comando 'clear'.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """
    Exibe o menu principal no terminal, instruindo o usuário a digitar a quantidade
    de caracteres desejada para a senha. Se nenhum valor ou um valor inválido for
    inserido, o comprimento padrão será 12.
    """
    limpa_terminal()
    print("#######################################")
    print("#                                     #")
    print("#        Crie uma senha forte         #")
    print("#                                     #")
    print("#######################################")
    print("\n")
    print("#######################################")
    print("#                                     #")
    print("#        Digite a quantidade          #")
    print("#      de caracteres que deseja       #")
    print("#         atribuir na senha:          #")
    print("#                                     #")
    print("#######################################")
    print("#                                     #")
    print("#    Caso não seja digitado nenhum    #")
    print("#    número, ou o número for menor    #")
    print("#    que 1, será automaticamente      #")
    print("#    atribuido o número padrão 12     #")
    print("#                                     #")
    print("#######################################")
    print("\n")


def new_senha():
    """
    Exibe a nova senha gerada e instrui o usuário a pressionar ENTER para gerar
    uma nova senha.
    """
    print("\n")
    print("#######################################")
    print("#                                     #")
    print("#        -------PARABÉNS-------       #")
    print("#    Essa é a sua nova senha forte    #")
    print("#                                     #")
    print("#######################################")
    print("#                                     #")
    print("#        Pressione ENTER para         #")
    print("#        gerar uma nova senha:        #")
    print("#                                     #")
    print("#######################################")
    print("\n")
    input('')
    limpa_terminal()


def erro():
    """
    Exibe uma mensagem de erro se o usuário digitar um valor não numérico para o
    comprimento da senha. Instrui o usuário a pressionar ENTER para continuar.
    """
    limpa_terminal()
    print("#######################################")
    print("#                                     #")
    print("#        Digite apenas números        #")
    print("#               0 - 9                 #")
    print("#                                     #")
    print("#######################################")
    print("#                                     #")
    print("#        Pressione ENTER para         #")
    print("#             continuar:              #")
    print("#                                     #")
    print("#######################################")
    print("\n")
    input('')
    limpa_terminal()


def main():
    """
    Função principal que controla o fluxo do programa. Exibe o menu principal,
    solicita a entrada do usuário para o comprimento da senha, gera uma nova senha
    forte, e lida com entradas inválidas.
    """
    while True:
        try:
            main_menu()
            length_input = input("Digite aqui: ")
            if length_input.strip() == '':
                length = 12
            else:
                length = int(length_input)
                if length < 1:
                    length = 12
            nova_senha = gerar_senha_forte(length)
            limpa_terminal()
            print('\n')
            print(nova_senha)
            new_senha()
        except ValueError:
            erro()


if __name__ == "__main__":
    # Se este script for executado diretamente, a função main() será chamada
    main()
