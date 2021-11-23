# mi-black-jack
En esta tarea se nos ha propuesto programar un juego que simule al blackjack en su versión ,ás sencilla.

En la idea el jugador juega contra la banca.

Para comenazar, se le asignan dos cartas al jugador y dos a la banca. Los puntos de cada uno será igual al valor que sumen sus respectivas cartas y gana el que vayor número de puntos tenga.

Finalmente, la máquina imprime un mensaje felicitando o apoyando al jugador según los resultados del juego.

Para compartir este juego se ha creado un repositorio de GitHub cuyo enlace le adjunto: https://github.com/acasasaez/mi-black-jack.git

Por otro lado, dejo a continuación el diagrama de flujo que refleja el mecanismo del juego:
![MI BLACK CON J](https://user-images.githubusercontent.com/91721826/143073262-711425c4-ef70-432d-b398-e62691ca7e42.jpg)

Por último, adjunto copia del código del juego:

´´´#Juego del black jack:
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
print ("Jugador 1:")
def jugador ():
    carta = random.choice(list(cartas))
    puntos = cartas[carta]
    carta = random.choice (list(cartas))
    puntosj = puntos + cartas[carta]
    return puntosj
    print ("Tus puntos son:" + str(puntosj))
gg= jugador()
print (gg)
print("Banca")
def banca():
    carta = random.choice (list(cartas))
    puntos= cartas[carta]
    carta = random.choice (list(cartas))
    puntosb= puntos + cartas[carta]
    return puntosb
    print ("Los puntos de la banca son:" + str(puntosb))
kk= banca()
print(kk)
if gg > kk:
    print ("Enhorabuena jugador, ha ganado la partida")
if gg< kk:
    print ("La banca ha ganado, vuelva a intentarlo")
else:
    print("Empate")
