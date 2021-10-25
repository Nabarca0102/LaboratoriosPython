#Programacion bajo plataformas abiertas-IE0117
#Laboratorio 1
#Programa que imprime una piramide

print("Necesitamos su número de carnet para realizar una pirámide.")
print("Si el último número del carnet universitario  es par, la pirámide será invertida.")
print("Si el último número del carnet unversitario es impar, la pirámide será NO invertida.")

#Se crea una variable carnet que decide que tipo de piramide se contruira
#Se utiliza una lista para almacenar los datos del carnet, ingresados.
#Con el bucle FOR se crea una variable digito que almacena cada entrada de la lista.
#Con el argumento dentro del bucle para cada digito ingresado en carnet se añade una entrada en lista.
carnet = input("Digite su número de carnet para definir el tipo de pirámide a contruir: ")
lista = []
for digito in carnet:
    lista.append(digito)

#Los datos almacenados en lista son tipo string, debemos convertir la entrada de interés en entero
#Se declara una variable nueva para convertir la entrada lista[5] en tipo entero.
lista_int = int(lista[5])

#Se utilizan los condicionales para indicar en consola que tipo de pirámide se creará.
#Una vez se define, se leerá el código respectivo dentro de cada condicional.
#En este caso, si el resultado es cero o no es cero determina a cual de los dos condicionales entra.
if (lista_int%2 == 0):
    print("Su número de su carnet es par, la pirámide será invertida.") 
    print("\n")
    
    #Se introducen los datos para crear la pirámide con las variables declaradas
    bloque = input("Digite un caracter para crear la pirámide: ")
    altura = int(input("Digite un número para determinar los pisos de la pirámide: "))
    print("\n")
    print("El caracter elegido para contruir la pirámide invertida es: ", bloque)
    print("La altura de la pirámide es: ", altura)
    print("\n")

    #Se utiliza un bucle FOR dentro de otro para iterar las variables ingresadas por el usuario.
    for contador1 in range(altura, 0, -1):
        for contador2 in range(0, contador1, 1):
            print(bloque, end=" ")
        print(" ")
    print("\n")
    print("Usted ha construido una pirámide!!!")
    print("\n")

elif (lista_int != 0):
    print("Su número de su carnet es impar, la pirámide será invertida.")
    print("\n")

    #Introducimos las funciones para que el usuario ingrese los datos para la pirámide
    bloque = input("Digite un caracter para crear la pirámide: ")
    altura = int(input("Digite un número para determinar la altura de la pirámide: "))
    print("\n")
    print("El caracter elegido para contruir la pirámide invertida es: ", bloque)
    print("La altura de la pirámide es: ", altura)
    print("\n")

    #Se utiliza una estructura de un buble For anidado dentro de otro para iterar la función de las variables
    for contador1 in range(0, altura, 1):
        for contador2 in range(0,contador1 +1, 1):
            print(bloque, end=" ")
        print(" ")
    print("\n")
    print("Usted ha contruido una pirámide, felicidades!!")
    print("\n")

print("Finaliza el programa.")
