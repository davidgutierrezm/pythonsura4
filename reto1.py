#Entradas=variables=referencisa en memoria

nivelAgua=int(input("Digite el nivel el agua: "))

#Proceso
if(nivelAgua>=0 and nivelAgua<20):
    #Salida
    print(f'El nivel de agua es {nivelAgua} y este es bajo')
elif (nivelAgua>=20 and nivelAgua<400):
    #Salida
    print(f'El nivel de agua es {nivelAgua} operando normalmente')
elif (nivelAgua>=400):
    #Salida
    print(f'El nivel de agua es {nivelAgua} y el nivel de agua es alto')
else:
    #Salida
    print("El nivel de agua no es valido")



