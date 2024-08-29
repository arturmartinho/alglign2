import numpy as np
from enigma.main import cifrar, de_cifrar, enigma, de_enigma

# Demonstração do funcionamento da biblioteca
mensagem = "abc"
P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])  
E = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])  

mensagem_cifrada = cifrar(mensagem, P)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_original = de_cifrar(mensagem_cifrada, P)
print("Mensagem recuperada:", mensagem_original)

mensagem_enigma = enigma(mensagem, P, E)
print("Mensagem cifrada com enigma:", mensagem_enigma)

mensagem_recuperada_enigma = de_enigma(mensagem_enigma, P, E)
print("Mensagem recuperada de enigma:", mensagem_recuperada_enigma)
