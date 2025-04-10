contraseña = "facuprado"
entrada = ""
intentos = 0
while entrada != contraseña and intentos < 3:
    entrada = input("Ingrese su contraseña: ")

    if entrada != contraseña:
        print("Contraseña incorrecta. Intenta de nuevo.")
        intentos += 1
if entrada == contraseña:
    print("¡Contraseña correcta!")
else:
    print("No hay más intentos.")
intentos=0

while entrada!=contraseña and intentos < 3:
    entrada=input("ingrese su contraseña: ")

if entrada != contraseña:
    print("Incorrecta-siga participando:")
    intentos +=1
if entrada == contraseña:
    print("Correcto!!!")
else:
    print("No hay mas intentos.")
    