# mapping af artskontinumre til budgetopfølgningskontio
artskonti = {
    "118091": "DirOmk",
    "163092": "DirOmk",
    "221091": "DirOmk",
    "221092": "DirOmk",
    "222091": "DirOmk",
    "222092": "DirOmk",
    "222094": "DirOmk",
    "223092": "DirOmk",
    "225091": "DirOmk",
    "226592": "DirOmk",
    "227090": "DirOmk",
    "227091": "DirOmk",
    "227092": "DirOmk",
    "228091": "DirOmk",
    "228092": "DirOmk",
    "315501": "Overf",
    "331001": "STV",
    "431073": "Sko-Løn",
    "431074": "Mas",
    "431075": "Fun-Løn",
}

imf_nr = "2433"


def srakonto(artskt: str, formalskt: str) -> str:
    if artskt[:6].isdigit():
        art = artskt[:6]
    else:
        return "Ukendt art"

    if formalskt[:4].isdigit():
        formal = formalskt[:4]
    else:
        formal = "0"

    if formal == imf_nr:
        return "IMF"
    else:
        if art in artskonti:
            return artskonti[art]
        else:
            return "Ukendt art"


if __name__ == "__main__":
    artskt = "315501 asd AD d A"
    formalskt = "1234 jskd fsjkd "
    print(srakonto(artskt, formalskt))
    artskt = "315501 asd AD d A"
    formalskt = "2433 jskd fsjkd "
    print(srakonto(artskt, formalskt))
