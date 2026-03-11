def validation_option(option, contexte):
    erreurs = []
    options = {"menu_principal": ["1", "2", "3", "4", "5"]}
    if not option in options[contexte]:
        erreurs.append("- Vous devez indiquez un chiffre compris dans le menu")
    return erreurs

def validation_oui_non(reponse):
    erreurs = []
    if not reponse in ("oui", "non"):
        erreurs.append("⚠️ Entrée invalide ⚠️")
    return erreurs