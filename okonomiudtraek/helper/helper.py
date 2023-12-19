from os.path import exists


def findesexcelark(path_to_ark: str) -> bool:
    if exists(path_to_ark):
        return True
    else:
        return False
