print("Semana No.11: Ejercio 1")


N=0
while N<=0:
    N=int(input("Ingrese un nùmero mayor que 0: "))
    if N<=0:
        print("El nùmero ingresado debe ser mayor a 0")
        print()
A=0
B=1
C=0
I=2
resultado=""
resultado=str(A)
if N>1:
    resultado+=(", "+ str(B))
    while I<N:
        C=A+B
        resultado+=(", "+str(C))
        A=B
        B=C
        I=I+1
        print(resultado)
else:
    print(resultado)