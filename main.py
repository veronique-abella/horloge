import time
from datetime import datetime, timedelta

#Fonction pour afficher l'heure au format hh:mm:ss ou hh:mm:ss AM/PM
def afficher_heure(heure, format_24_heures=True):
    if format_24_heures:
        heure_formattee = heure.strftime("%H:%M:%S")
    else:
        heure_formattee = heure.strftime("%I:%M:%S %p")
    print(heure_formattee, end='\r')  # Utilisez '\r' pour mettre à jour la ligne actuelle dans la console

#Fonction pour effacer la ligne précédente
def effacer_ligne():
    print('\033[K', end='')

#Fonction pour régler l'heure affichée
def regler_heure(heures, minutes, secondes):
    return datetime.now().replace(hour=heures, minute=minutes, second=secondes)

#Fonction pour régler l'alarme
def regler_alarme(heures, minutes, secondes, message):
    alarme = datetime.now().replace(hour=heures, minute=minutes, second=secondes)
    return alarme, message

#Fonction pour choisir le mode d'affichage de l'heure
def choisir_mode_affichage():
    mode = input("Choisissez le mode d'affichage (12 ou 24 heures): ")
    return mode.lower() == "12"

#Initialisation de l'heure actuelle
heure_actuelle = regler_heure(heures=int(input("Veuillez entrer l'heure : ")), minutes=int(input("Veuillez entrer les minutes : ")), secondes=int(input("Veuillez entrer les secondes : ")))

#Initialisation de l'alarme
alarme, message_alarme = regler_alarme(heures=int(input("Veuillez entrer l'heure de l'alarme : ")), minutes=int(input("Veuillez entrer les minutes de l'alarme : ")), secondes=int(input("Veuillez entrer les secondes de l'alarme : ")), message=input("Entrez votre message : "))

#Choix du mode d'affichage
format_12_heures = choisir_mode_affichage()

#Boucle infinie pour actualiser l'heure chaque seconde
try:
    while True:
        # Vérifier si l'heure actuelle correspond à l'heure de l'alarme
        if heure_actuelle >= alarme and heure_actuelle < alarme + timedelta(seconds=1):
            effacer_ligne()  # Effacer la ligne précédente
            print(message_alarme)


        afficher_heure(heure_actuelle, format_24_heures=not format_12_heures)

        heure_actuelle += timedelta(seconds=1)  # Ajoute une seconde à l'heure actuelle
        time.sleep(1)  # Attendre une seconde

except KeyboardInterrupt:
    print("\nProgramme arrêté.")