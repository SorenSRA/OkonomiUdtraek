# mapping af danske månednavne til kvartal
danish_month_names = {
    "januar": 1,
    "februar": 1,
    "marts": 1,
    "april": 2,
    "maj": 2,
    "juni": 2,
    "juli": 3,
    "august": 3,
    "september": 3,
    "oktober": 4,
    "november": 4,
    "december": 4,
}


def kvartal(maaned: str) -> int:
    if maaned.lower() in danish_month_names:
        return danish_month_names[maaned.lower()]
    else:
        return None


if __name__ == "__main__":
    print(kvartal("AuGust"))  # 3
    print(kvartal("Niels"))  # None
