#Juego del black jack:
cartas ={chr(0x1f0a): 11,
         chr(0x1fa2): 2,
         chr (0x1f03): 3,
         chr (0x1f0a4):4,
         chr(0x1f0a5): 5,
         chr(0x1f0a6): 6,
         chr(0x1f0a7): 7,
         chr(0x1f08): 8,
         chr (0x1f0a9): 9,
         chr(0x1f0aa):10,
         chr(0x1f0ab):10,
         chr(0x1f0ad):10,
         chr(0x1f0ae): 10 }

print ( "cartas{}".format(" ".join(cartas.keys())))
print ("cartas{}".format(" ".join(str(cartas.values()))))

for carta, valor in cartas.items():
    print("la carta{} vale {}".format(carta,valor))
print(" ")
for carta in sorted (cartas.keys()):
    print ("la carta{} vale {}".format(carta, cartas[carta]))
print (" ")
#Juego 
print("Juego del Black Jack")
import random
random.choice(list(str(cartas)))
print (carta)
print ("jugador 1:")
def jugador ():
    carta = random.choice(list(cartas))
    puntos = cartas[carta]
    carta = random.choice (list(cartas))
    puntosj = puntos + cartas[carta]
    print ("Tus puntos son:" + str(puntosj))
gg= jugador()
print (gg)
print("Banca")
def banca():
    carta = random.choice (list(cartas))
    puntos= cartas[carta]
    carta = random.choice (list(cartas))
    puntosb= puntos + cartas[carta]
    print ("Los puntos de la banca son:" + str(puntosb))
kk= banca()
print(kk)
