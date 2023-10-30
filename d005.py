print (".____       _____    __________.____________________________________________.___________ __________    _____    ________ ")
print ("|    |     /  _  \   \______   \   \____    /\____    /\_   _____/\______   \   \______  \\______   \  /  _  \  /  ______/ ")
print ("|    |    /  /_\  \   |     ___/   | /     /   /     /  |    __)_  |       _/   ||    |  \|       _/ /  /_\  \/   \  ___ ")
print ("|    |___/    |    \  |    |   |   |/     /_  /     /_  |        \ |    |   \   ||    `   \    |   \/    |    \    \_\  \ ")
print ("|_______ \____|__  /  |____|   |___/_______ \/_______ \/_______  / |____|_  /___/_______  /____|_  /\____|__  /\______  / ")
print ("        \/       \/                        \/        \/        \/         \/            \/       \/         \/        \/ ")

#declaración inicial de variables
dinero_usuario = float(input("\nLo primero, el dinero, querida... ¿Cuánto tienes?: "))
dinero_inicial = dinero_usuario
total = 0
lista_pedido = []

#lista pizzas
laBasica = 5.50
laHierbas = 7.00
laBestia = 6.66
laChunga = 8.80
laChoni = 6.40

#lista extras
extraQueso = 1.50
bacon = 2.00
heura = 1.80
peperoni = 1.90
sabo = 2.50

while True:

    print ("\n¿Qué pizza quieres, Reina?:\n")
    
    print (f"1 - La Básica - {laBasica} €")
    print (f"2 - La Hierbas - {laHierbas} €")
    print (f"3 - La Bestia - {laBestia} €")
    print (f"4 - La Chunga - {laChunga} €")
    print (f"5 - La Choni - {laChoni} €")

    elección = int(input("\nElige un número: "))

    match elección:
        case 1:
            total = laBasica
            dinero_usuario -= total
            print(f"\nHas elegido La Básica, son {laBasica} €")
            lista_pedido.append (f"La Básica - {laBasica} €")
            break
        case 2:
            total = laHierbas
            dinero_usuario -= total
            print(f"\nHas elegido La Hierbas, son {laHierbas} €")
            lista_pedido.append (f"La Hierbas -  {laHierbas} €")
            break
        case 3:
            total = laBestia
            dinero_usuario -= total
            print(f"\nHas elegido La Bestia, son {laBestia} €")
            lista_pedido.append (f"La Bestia - {laBestia} €")
            break
        case 4:
            total = laChunga
            dinero_usuario -= total
            print(f"\nHas elegido La Chunga, son {laChunga} €")
            lista_pedido.append (f"La Chunga -  {laChunga} €")
            break
        case 5:
            total = laChoni
            dinero_usuario -= total
            print(f"\nHas elegido La Choni, son {laChoni} €")
            lista_pedido.append (f"La Choni -  {laChoni} €")
            break
        case _:
            print("No te columpies, guapa... vuelve a elegir, anda...")

print (f"\nLlevas un total de {round(total,2)} €")
print (f"Te quedarían {round(dinero_usuario,2)} €")
        
while True:

    print("\n¿Quieres algún ingrediente extra más?\n")

    print (f"1 - Yas")
    print (f"2 - Nah")

    extraQuiere = int(input("\nDime: "))

    match extraQuiere:
        case 1:
            print (f"\nEsto es lo que puedes añadir:\n")

            print (f"1 - Extra de queso - {extraQueso} €")
            print (f"2 - Bacon - {bacon} €")
            print (f"3 - Heura - {heura} €")
            print (f"4 - Peperoni - {peperoni} €")
            print (f"5 - Sabo - {sabo} €")
            print (f"6 - Lo he pensado mejor, no quiero nada más, quiero pagar")

            extraCual = int(input("\nElige un número:\n"))

            match extraCual:
                case 1:
                    total += extraQueso
                    dinero_usuario -= total
                    lista_pedido.append (f"Extra de Queso - {extraQueso} €")
                    print (f"Has elegido Extra de Queso, son {extraQueso} €")
                    print (f"\nLlevas un total de {round(total,2)} €")
                    print (f"Te quedarían {round(dinero_usuario,2)} €")
                
                case 2:
                    total += bacon
                    dinero_usuario -= total
                    lista_pedido.append (f"Bacon - {bacon} €")
                    print (f"Has elegido Bacon, son {bacon} €")
                    print (f"\nLlevas un total de {round(total,2)} €")
                    print (f"Te quedarían {round(dinero_usuario,2)} €")

                case 3:
                    total += heura
                    dinero_usuario -= total
                    lista_pedido.append (f"Heura - {heura} €")
                    print (f"Has elegido Heura, son {heura} €")
                    print (f"\nLlevas un total de {round(total,2)} €")
                    print (f"Te quedarían {round(dinero_usuario,2)} €")

                case 4:
                    total += peperoni
                    dinero_usuario -= total
                    lista_pedido.append (f"Peperoni - {peperoni} €")
                    print (f"Has elegido Peperoni, son {peperoni} €")
                    print (f"\nLlevas un total de {round(total,2)} €")
                    print (f"Te quedarían {round(dinero_usuario,2)} €")

                case 5:
                    total += sabo
                    dinero_usuario -= total
                    lista_pedido.append (f"Sabo - {sabo} €")
                    print (f"Has elegido Sabo, son {sabo} €")
                    print (f"\nLlevas un total de {round(total,2)} €")
                    print (f"Te quedarían {round(dinero_usuario,2)} €")

                case 6:
                    print (f"Claro, como quieras...")
                    break

                case _:
                    print (f"A vacilar a tu puta madre, guapa")
 

        case 2:
            print ("Pues ya estaría...")
            break

        case _:
            print (f"Que si quiere extra...")

print (f"En total serían {round(total,2)} €")

if total > dinero_inicial:
    print (f"Un momento... no tienes dinero suficiente, perra... vuelve cuando tengas pasta, aquí no se come de gratis!!")

else:
    print ("Toma el ticket\n\n\n")
    print (">-------------------------------------<")
    print ("<------------- SU PEDIDO ------------->")
    print (">-------------------------------------<")
    
    for i in lista_pedido:
        print(f"{i}")


    print (">-------------------------------------<")
    print (f"Total:\n{round(total,2)} €\nSu cambio\n{round(dinero_usuario,2)} €")
    print (">-------------------------------------<")
    print ("-Que aproveche y por el culo lo eches!!")

    


