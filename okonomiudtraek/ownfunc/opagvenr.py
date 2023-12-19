# mapping af projektnumre til projektnavn
opgave_projekt = {
    "640449": "RigKilde",
    "640450": "RigKilde",
    "640489": "Hojmose",
    "640490": "Hojmose",
    "640599": "NatMan",
    "640600": "NatMan",
    "640649": "Better",
    "640650": "Better",
    "640674": "Coastal",
    "640675": "Coastal",
    "640699": "OpenWoods",
    "640700": "OpenWoods",
    "640729": "ForFit",
    "640730": "ForFit",
    "640749": "WadSea",
    "640750": "WadSea",
}


def projekt(opgave: str) -> str:
    projekt_nr = opgave[:6]
    if projekt_nr in opgave_projekt:
        projekt_alias = opgave_projekt[projekt_nr]
    else:
        projekt_alias = "Fejl i opgaveNr"

    return projekt_alias


if __name__ == "__main__":
    print(projekt("640700"))  # Openwoods
    print(projekt("640900"))  # Fejl i opgaveNr
