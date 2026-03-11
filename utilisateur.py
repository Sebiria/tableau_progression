from colorama import Fore, Style
from affichage import (afficher_titre, afficher_date_propre, afficher_options,
                       afficher_consigne_option, separation_ancienne_info,
                       afficher_erreurs)
from validation import validation_option, validation_oui_non

def menu_principal(jour, date):
    afficher_date_propre(jour, date)
    afficher_titre("menu_principal")
    while True:
        afficher_options("menu_principal")
        afficher_consigne_option()
        option = input("Option ➡️ ").strip()
        separation_ancienne_info()
        erreurs = validation_option(option, "menu_principal")
        if erreurs:
            afficher_erreurs(erreurs)
        else:
            return option

def parametrage(temporalite):
    while True:
        print(Fore.MAGENTA + "Souhaitez_vous paramétrer toutes les dates et période de l'année" + Fore.RESET)
        reponse = input("oui / non ➡️ ").lower().strip()
        erreurs = validation_oui_non(reponse)
        if erreurs:
            afficher_erreurs(erreurs)