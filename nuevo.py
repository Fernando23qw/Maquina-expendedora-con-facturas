bebida = True

while bebida:
    
    def maquina_expendora():    
        print("¡Bienvenido a la máquina expendedora!")
    
    maquina_expendora()

    numero_de_bebida = int(input("Ingrese el número de la bebida que desea comprar: "))

    nombre = "COCA COLA, FANTA, PEPSI, SPRITE, NESTEA"
    precio = "10 euros"

    match numero_de_bebida:
        case 1:
            nombre = "COCA COLA"
        case 2:
            nombre = "FANTA"
        case 3:
            nombre = "PEPSI"
        case 4:
            nombre = "SPRITE"
        case 5:
            nombre = "NESTEA"
        case _:
            print("Opción no válida")
            continue

    print(f"Has elegido {nombre}")
    print(f"El precio es de {precio}")

    while True:
        dinero = input("Ingrese el dinero para comprar la bebida (10 euros): ")
        if dinero == "10 euros":
            print("¡Compra exitosa! Disfruta tu bebida.")

            with open("facturas.txt", "a") as archivo:
                archivo.write(f"Bebida: {nombre} - Precio: {precio}\n")

            break  
        else:
            print("Cantidad incorrecta.")

    respuesta = input("¿Deseas comprar otra bebida? (si/no): ")

    if respuesta == "no":
        print("¡Gracias por usar la máquina expendedora!")
        break
    