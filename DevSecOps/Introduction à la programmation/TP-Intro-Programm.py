#Addition et Multiplication

a=int(input("donnez-moi un nombre"))
b=int(input("donnez-moi un second nombre"))

somme=a+b
print(f"la somme de {a} et {b} est {somme}")

produit=a*b
print(f"le produit de {a} et {b} est {produit}")


#Calculatrice d'IMC
taille = float(input("Entrez votre taille en mètres: "))
poids = float(input("Entrez votre poids en kilogrammes: "))
print(f"IMC : {poids/taille**2}")


#Vérification de nombre pair ou impair
c=int(input("donnez-moi un nombre"))

if c%2==0:
    print(f"Le nombre {c} est pair!")

else:
    print(f"Le nombre {c} est impair!")  


#Table de multiplication
d=int(input("donnez-moi un nombre"))

for i in range(1,11):
    table=d*i
    print(f"La multiplication de {d} par {i} est {table}")


#Vérification de l'éligbilité au vote
e=str(input("donnez-moi votre nom!"))
f=int(input("donnez-moi votre âge"))

if f>18:
    print(f"Vous pouvez aller voter {e}!")

else:
    print (f"Vous n'êtes pas éligible pour voter {e}")


#Calcul de la somme des entiers jusqu'à un nombre donné
while True:
    g=int(input("Saisissez un nombre."))
    if g > 0:
        break
    print("Vous ne pouvez pas renseigner de nombre négatif.")
    sum = 0
    for i in range(1, g+1):
        sum += i
    print(f"La somme des entiers de 1 à {g} vaut : {sum}")


#Jeu de devinette
from random import randint
h=randint(1, 100)
choix = int(input("Choisissez un nombre entre 1 et 100."))
while True :
    if h < choix:
        print("moins !")
        choix = int(input("Choisissez un nombre entre 1 et 100."))
    elif h > choix:
        print("plus !")
        choix = int(input("Choisissez un nombre entre 1 et 100."))
    else:
        print("Bien joué !")
        break

#Compte à rebours
j= int(input("Choisissez un nombre : "))
import time
for i in range(j+1):
    print(j)
    time.sleep(3)
    j -= 1

#Validation de mot de passe
k=str(input("Donnez-moi un mot de passe"))
while True:
        mdp_verif = input("Saisissez à nouveau le mot de passe.\n")
        if k == mdp_verif:
            print("Login successful.")
            break

#Conversion de température
l=int(input("Saisissez ue température en degrés Celsius (°C).\n"))
print(f"La température en degrés Fahrenheit est : {(9/5)*l+32}.")

#Conversion de secondes
m=int(input("Veuillez saisir une durée en secondes"))
heure = m//3600
m %= 3600
minute = m//60
m %= 60
seconde = m
print(f"{heure*3600+minute*60+seconde} seconde(s) correspond à : {heure} heure(s) {minute} minute(s) {seconde} seconde(s)")