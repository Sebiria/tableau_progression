import locale
import time
from datetime import datetime



if __name__ == '__main__':

    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    date_heure = datetime.now()  # Date et heure
    jour = datetime.now().strftime("%A")  # Jour de la semaine
    heure = datetime.now().strftime("%H:%M:%S") # Heure
    date = str(date_heure).split(" ")[0]
    print(jour)
    print(date_heure)
    print(date)




    #region Déclarations
    # type profil = {'Prenom':
    profils = {}

    #endregion
