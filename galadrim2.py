def sous_chaine_plus_frequente(texte, n =3):
    if len(texte) <= 2:
        return None
    if len(texte) == 3:
        return texte
    chaines = {texte[0:3]: 1}

    for i in range(3, len(texte)):
        new_chaine = texte[i-2:i+1]
        if new_chaine in chaines:
