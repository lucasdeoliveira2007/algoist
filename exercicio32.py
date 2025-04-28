base = int(input("adicione a base da tabuada que deseja realizar: "))
inicio = int(input("adicione inicio da tabuada que deseja realizar: "))
fim = int(input("adicione o fim da tabuada que deseja realizar: "))

def tabuada_personalizada (base, inicio, fim):
    print(f"tabuada do {base} de {inicio} e {fim}: ")
    for j in range (inicio, fim +1):
        print(f'{base} x {j} = {base * j }')

tabuada_personalizada(base, inicio, fim)