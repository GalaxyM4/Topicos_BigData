print("Condicionales")

# Simple
score = 17

if score >= 10.51: print ("Aprobao")

# Doble
age = 17

if age >= 10: print("Puedes 🤌")
else: print("No puedes 🦣")

# Anidado
if score >= 17 & score <= 20: print("feli")
elif score >= 14 & score < 17: print("casi feli")

# Múltiple (previo a python 3.9.0 no existía multiple)
num = 4

match num: 
    case 1: print("a pez")
    case 2: print("e xd")
    case 3: print("i mnk")
    case 4: print("o sdasd")
    case 5: print("u pe")
    case _: print("numero no existe a vocal")