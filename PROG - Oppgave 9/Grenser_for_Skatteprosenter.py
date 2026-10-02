# Grenser for skatteprosenten som brukes i skattekalkulatoren.

# Satsene hentes fra listen slik at de samme verdiene brukes i beregningen.
skatteprosenter = [0, 30, 35, 40]


def Grenser_for_Skatteprosenter(bruttolønn):
    if bruttolønn <= 110000:
        return skatteprosenter[0]
    elif bruttolønn <= 750000:
        return skatteprosenter[1]
    elif bruttolønn <= 1000000:
        return skatteprosenter[2]
    else:
        return skatteprosenter[3]