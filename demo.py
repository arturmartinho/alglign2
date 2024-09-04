import numpy as np
from enigma import enigma, de_enigma, cifrar, de_cifrar
from enigma import para_one_hot, para_string

mensagem = "o bolo de chocolate fica pronto quatro horas da tarde"

P = np.eye(27) 
E = np.roll(np.eye(27), 1, axis=0) 

one_hot_msg = para_one_hot(mensagem)

msg_cifrada_simples = cifrar(mensagem, P)
print("Mensagem Cifrada Simples:", para_string(msg_cifrada_simples))

msg_decifrada_simples = de_cifrar(msg_cifrada_simples, P)
print("Mensagem Decifrada Simples:", para_string(msg_decifrada_simples))

msg_cifrada_enigma = enigma(mensagem, P, E)
print("Mensagem Cifrada Enigma:", para_string(msg_cifrada_enigma))

msg_decifrada_enigma = de_enigma(msg_cifrada_enigma, P, E)
print("Mensagem Decifrada Enigma:", para_string(msg_decifrada_enigma))

