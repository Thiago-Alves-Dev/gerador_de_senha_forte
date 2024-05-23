from random import choice
from string import ascii_letters, digits, punctuation


def gerar_senha_forte(length=12):
    """
    Gera uma senha forte composta por letras, dígitos e caracteres de pontuação.

    Parâmetros:
    -----------
    length : int, opcional
        O comprimento da senha a ser gerada. O valor padrão é 12.

    Retorna:
    --------
    str
        A senha gerada como uma string.
    """
    caracteres = ascii_letters + digits + punctuation
    senha = ''.join(choice(caracteres) for _ in range(length))
    return senha


def _test():
    """
    Função de teste que gera e imprime uma nova senha forte.
    """
    nova_senha = gerar_senha_forte()
    print(nova_senha)


if __name__ == "__main__":
    # Caso este script seja executado diretamente, a função _test() será chamada
    _test()
