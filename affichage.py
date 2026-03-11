from colorama import Fore, Style

def separation_ancienne_info():
    print("\n🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽\n")

def afficher_erreurs(erreurs):
    print(Fore.RED + f"L'entrée est invalide pour {"la raison suivante :" if len(erreurs) == 1 else "les raisons suivantes"}" + Fore.RESET)
    for erreur in erreurs:
        print(Fore.MAGENTA + erreur + Fore.RESET)

def afficher_date_propre(jour, date):
    mois = {"01": "janvier", "02": "février", "03": "mars",
            "04": "avril", "05": "mai", "06": "juin",
            "07": "juillet", "08": "août", "09": "septembre",
            "10": "octobre", "11": "novembre", "12": "décembre"}
    print(Style.BRIGHT + Fore.CYAN + " "*9 + jour.title() + " " + date[6:9] + " " + mois[date[4:6]] +
          Style.RESET_ALL + Fore.RESET)

def afficher_titre(contexte):
    titres = {
        "menu_principal": "📋 MENU PRINCIPAL 📋",
        "ajout_participant": "➕ AJOUT D'UN PARTICIPANT ➕",
        "acces_profil": "👫 ACCÈS AU PROFIL D'UN PARTICIPANT 👫",
        "statistiques": "📈 STATISTIQUES 📉",
        "bonus_malus": "👍 Projet / Pénalité 👎",
        "parametrage": "⚙️ PARAMÉTRAGE ⚙️"}
    titre = titres[contexte]
    print(Style.BRIGHT + Fore.CYAN + "🔹🔹🔷" + titre + "🔷🔹🔹" + Style.RESET_ALL + Fore.RESET)

def afficher_options(contexte):
    options = {"menu_principal": "1 - Ajouter un participant"
                        "\n  2 - Accès au profil d'un participant"
                        "\n    3 - Statistiques"
                        "\n      4 - Projet / Pénalité"
                        "\n        5 - Paramétrage"
                        "\n🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹🔹"}
    print(Fore.YELLOW + options[contexte] + Fore.RESET)

def afficher_consigne_option():
    print(Fore.MAGENTA + "Choisissez une option du menu en entrant le numéro correspondant" + Fore.RESET)