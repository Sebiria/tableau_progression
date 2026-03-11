import locale
from datetime import datetime

from utilisateur import menu_principal, parametrage

if __name__ == '__main__':

    #region Gestion de temporalité
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    date_heure = datetime.now()  # Date et heure
    jour = datetime.now().strftime("%A")  # Jour de la semaine
    heure = datetime.now().strftime("%H:%M:%S") # Heure
    date = str(date_heure).replace("-", "").split(" ")[0]
    temporalite = {"jour_actuel": date,
                   "premier_jour": "",
                   "dernier_jour": "",
                   "jour_ferie": [],
                   "p1": [],
                   "p2": [],
                   "p3": [],
                   "p4": [],
                   "p5": []}
    #endregion

    #region Déclaration de variables
    profils = {}
    #endregion

    while True:
        choix = menu_principal(jour, date)

        if choix == "5":
            temporalite = parametrage(temporalite)