import random

def miniJuego():
    lista = [
        "claro",
        "me",
        "hola",
        "cual"
    ]

    palabra = random.choice(lista)

    palabra_contada = len(palabra)

    r_mal = 0
    r_bien = 0

    concatenado = ""

    print("La palabra que le tocó tiene", palabra_contada, "caracteres")
    for i in range(palabra_contada):
        r_usuario = input("Ingrese la letra que cree que va en la palabra: ").lower()

        if r_usuario in palabra:
            print(f"+------------------------------------------------------+")
            print(f"| Muy bien ✅ la letra {r_usuario} está en la palabra |")
            print(f"| Te quedan por adivinar {palabra_contada - i}              |")
            print(f"+------------------------------------------------------+")


            concatenado += r_usuario 
            print(f"+-------------------------+")
            print(f"| Progreso: {concatenado} |")
            print(f"+-------------------------+")

            r_bien += 1

        else:
            print(f"+-------------------------------------------+")
            print(f"| Lástima no adivinaste ❌                  |")
            print(f"| Te quedan {palabra_contada - i} intentos  |")
            print(f"+-------------------------------------------+")
            r_mal += 1

    if r_bien == palabra_contada:
        print(f"+----------------------------------+")
        print(f"| La palabra era {palabra}         |")
        print(f"| y tu acertaste {r_bien}          |")
        print(f"| Las cuales fueron {concatenado}  |")
        print(f"| 😁  |")
        print(f"+----------------------------------+")
    elif r_mal == palabra_contada:
        print(f"¡¡Manco te fue re mal!! 😭")

    else:
        print(f"¡Te fue regular! 😐")

        
miniJuego()
