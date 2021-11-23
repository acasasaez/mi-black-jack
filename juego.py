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

lista1= "cartas{}".format(" ".join(cartas.keys()))
lista2 = "cartas{}".format(" ".join(str(cartas.values())))
print(lista1)
print(str(lista2))
