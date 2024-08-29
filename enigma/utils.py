import numpy as np

ALFABETO = "abcdefghijklmnopqrstuvwxyz "

def para_one_hot(msg: str) -> np.array:
    n = len(ALFABETO)
    M = np.zeros((n, len(msg)), dtype=int)
    for i, char in enumerate(msg):
        if char in ALFABETO:
            idx = ALFABETO.index(char)
            M[idx, i] = 1
    return M

def para_string(M: np.array) -> str:
    msg = ""
    for i in range(M.shape[1]):
        idx = np.argmax(M[:, i])
        msg += ALFABETO[idx]
    return msg
