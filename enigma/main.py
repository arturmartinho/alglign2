import numpy as np
from enigma.utils import para_one_hot, para_string


def cifrar(msg: str, P: np.array) -> str:
    M = para_one_hot(msg)
    M_cifrada = P @ M
    return para_string(M_cifrada)

def de_cifrar(msg: str, P: np.array) -> str:
    M_cifrada = para_one_hot(msg)
    M_original = np.linalg.inv(P).astype(int) @ M_cifrada
    return para_string(M_original)

def enigma(msg: str, P: np.array, E: np.array) -> str:
    mensagem_cifrada = ""
    for char in msg:
        mensagem_cifrada += cifrar(char, P)
        P = P @ E  
    return mensagem_cifrada

def de_enigma(msg: str, P: np.array, E: np.array) -> str:
    mensagem_original = ""
    for char in msg:
        mensagem_original += de_cifrar(char, P)
        P = P @ E  
    return mensagem_original
