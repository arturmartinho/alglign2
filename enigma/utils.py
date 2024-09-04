import numpy as np

alfabeto = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def para_one_hot(msg):
    matriz = np.zeros((len(alfabeto), len(msg)))
    for i, c in enumerate(msg):
        idx = alfabeto.index(c)
        matriz[idx, i] = 1
    return matriz

def para_string(M):
    msg = ""
    for i in range(M.shape[1]):
        idx = np.argmax(M[:, i])
        msg += alfabeto[idx]
    return msg



