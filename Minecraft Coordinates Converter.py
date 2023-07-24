# Made 100% with Python
# Automatization

def conversor(x1, z1, y1):
    x2 = x1 / 8
    z2 = z1 / 8
    y2 = y1 / 8

    x3 = x1 * 8
    z3 = z1 * 8
    y3 = y1 * 8 

    return x2, z2, y2, x3, z3, y3

def coordenada():
    x1 = float(input("Enter your coordinate X: "))
    z1 = float(input("Enter your coordinate Z: "))
    y1 = float(input("Enter your coordinate Y: "))

    return x1, z1, y1

def tipo():
    while True:
        tipo = int(input("Enter 1 to convert: Overworld -> Nether \nEnter 2 to convert: Nether -> Overworld: "))
        if tipo == 1 or tipo == 2:
            print("Valid number.")
            return tipo
        else:
            print("Invalid number. Please, choose between 1 and 2.")
            break
       

def nova_coordenada(x2, z2, y2, x3, z3, y3, tipo):
    if tipo == 1:
        print(f"Your new coordinates are: \nX: {x2}\nZ: {z2}\nY: {y2}")
    elif tipo == 2:
        print(f"Your new coordinates are: \nX: {x3}\nZ: {z3}\nY: {y3}")


def main():
    while True:
        x1, z1, y1 = coordenada()
        x2, z2, y2, x3, z3, y3 = conversor(x1, z1, y1)
        tipo_escolhido = tipo()
        nova_coordenada(x2, z2, y2, x3, z3, y3, tipo_escolhido)

        continuar = input("Do you wish to continue converting? y/n: ")
        if continuar.lower() != "y":
            break

main()