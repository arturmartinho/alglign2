import numpy as np
from enigma.utils import para_one_hot, para_string

def cifrar(msg, P):
    M = para_one_hot(msg)
    M_c = np.dot(P, M)
    return M_c

def de_cifrar(msg_cifrada, P):
    P_inv = np.linalg.inv(P)
    M = np.dot(P_inv, msg_cifrada)
    return M

def enigma(msg, P, E):
    M = para_one_hot(msg)
    P_current = P.copy() 
    for i in range(M.shape[1]):
        M[:, i] = np.dot(P_current, M[:, i])
        P_current = np.dot(E, P_current)
    return M

def de_enigma(msg_cifrada, P, E):
    M = msg_cifrada.copy()
    P_current = P.copy()
    P_inv_series = [P_current]
    for i in range(1, M.shape[1]):
        P_current = np.dot(E, P_current)
        P_inv_series.append(P_current)
        
    for i in range(M.shape[1] - 1, -1, -1):
        P_inv = np.linalg.inv(P_inv_series[i])
        M[:, i] = np.dot(P_inv, M[:, i])

    return M
