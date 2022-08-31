edad=int(input("Digite la edad: "))

#Proceso
if(edad>=0 and edad<14):
    #Salida
    print(f'La edad es {edad} y es un niño')
elif (edad>=14 and edad<28):
    #Salida
    print(f'La edad es {edad} y es un joven')
elif (edad>=28 and edad<60):
    #Salida
    print(f'La edad es {edad} y es un adulto')
elif (edad>=60 and edad<100):
    #Salida
    print(f'La edad es {edad} y es un adulto mayor')
else:
    #Salida
    print("la edad es invalida")