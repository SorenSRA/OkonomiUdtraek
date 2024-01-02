def projekt(opgave: str, opgave_projekt) -> str:
    try:
        projekt_nr = int(opgave[:6])
    except:
        projekt_alias = "Fejl i opgaveNr"

    if projekt_nr in opgave_projekt:
        projekt_alias = opgave_projekt[projekt_nr]
    else:
        projekt_alias = "Fejl i opgaveNr"

    return projekt_alias
