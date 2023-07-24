# Feito 100% em Python
# Automatização das conversões

def conversor(x1, z1, y1):
    x2 = x1 / 8
    z2 = z1 / 8
    y2 = y1 / 8

    x3 = x1 * 8
    z3 = z1 * 8
    y3 = y1 * 8 

    return x2, z2, y2, x3, z3, y3

def coordenada():
    x1 = float(input("Digite a sua coordenada X: "))
    z1 = float(input("Digite a sua coordenada Z: "))
    y1 = float(input("Digite a sua coordenada Y: "))

    return x1, z1, y1

def tipo():
    while True:
        tipo = int(input("Pressione 1 para converter: Coordenada Overworld -> Nether \nPressione 2 para converter: Coordenada Nether -> Overworld: "))
        if tipo == 1 or tipo == 2:
            print("Forma válida.")
            return tipo
        else:
            print("Forma inválida. Por favor, escolha entre 1 ou 2.")
            break
       

def nova_coordenada(x2, z2, y2, x3, z3, y3, tipo):
    if tipo == 1:
        print(f"Suas novas coordenadas são: \nX: {x2}\nZ: {z2}\nY: {y2}")
    elif tipo == 2:
        print(f"Suas novas coordenadas são: \nX: {x3}\nZ: {z3}\nY: {y3}")


def main():
    while True:
        x1, z1, y1 = coordenada()
        x2, z2, y2, x3, z3, y3 = conversor(x1, z1, y1)
        tipo_escolhido = tipo()
        nova_coordenada(x2, z2, y2, x3, z3, y3, tipo_escolhido)

        continuar = input("Deseja continuar? s/n: ")
        if continuar.lower() != "s":
            break

main()