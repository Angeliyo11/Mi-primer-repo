print("HOLA BIENVENIDOS A MI PRIMER JUEGO")
print("Creado por 'zlAngel'")
print(" ")
print("Espero que te diviertas!")
print(" ")
print("RECUERDA RESPETAR TU TURNO")
print(" ")

import random

choices = ["piedra", "papel", "tijera"]
attempts = 5

for _ in range(attempts):
    user_choice = input("Elige piedra, papel o tijera: ").lower()
    computer_choice = random.choice(choices)
    
    if user_choice not in choices:
        print("Eliga una opción valida ._.")
        continue
    
    print(f"Usted eligió: {user_choice}")
    print(f"La CPU eligió: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Oh no esto es un empata O.o")
    elif (user_choice == "piedra" and computer_choice == "tijera") or (user_choice == "papel" and computer_choice == "piedra") or (user_choice == "tijera" and computer_choice == "papel"):
        print("YEAH Ganaste que crack :3")
    else:
        print("OHHH Te gano la  :(")

print("End Game")



