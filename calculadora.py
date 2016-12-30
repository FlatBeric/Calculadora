a = int(input("Introduzca el primer número: "))
b = int(input("Introduzca el segundo numero: "))
operando = int(input("Selecione una operación: \n 1.-Suma(+) \n 2.-Resta(-) \n 3.-Multiplicación(*) \n 4.-División(/) \n "))

if operando == 1:
    resultado = a + b
    
elif operando == 2:
    resultado = a - b
elif operando == 3:
    resultado = a * b
elif operando == 4:
    resultado = a / b
else:
    print("Meh, intentalo de nuevo.")

print("Su resultado es %d" %resultado)