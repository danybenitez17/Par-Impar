# Programa para verificar si un numero es par o impar
# input

X=int(input("Digite el valor de X: "))

# Processing

R = (X % 2)

if R==0:
    rta= "PAR"

 else:
    rta= "IMPAR"
    print("HOLA")

    #Output
    print("El numero " + str(X) + " es " + rta )
  