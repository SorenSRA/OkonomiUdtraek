from pathlib import Path  # core python module
from os.path import join
import datetime

import PySimpleGUI as sg  # pip install pysimplegui

# import af egne moduler
from lisudtraek import lisudtraek


def main_window():
    default_folder = settings["PROGRAM"]["outputfolder_default"]
    layout = [
        [sg.Text("Nyt LIS-udtræk Vælg fil")],
        [
            sg.Text("Filnavn: ", s=15, justification="r"),
            sg.Input(s=70, key="-NEWFILE-"),
            sg.FileBrowse(
                initial_folder=default_folder, file_types=(("Excel Files", "*.xls*"),)
            ),
        ],
        [
            sg.Text("Output Folder: ", s=15, justification="r"),
            sg.Input(s=70, default_text=default_folder, key="-OUTPUTFOLDER-"),
            sg.FolderBrowse(
                initial_folder=default_folder,
            ),
        ],
        [sg.Text("Seneste Økonomiudtræk Vælg fil")],
        [
            sg.Text("Filnavn: ", s=15, justification="r"),
            sg.Input(s=70, key="-OLDFILE-"),
            sg.FileBrowse(
                initial_folder=default_folder, file_types=(("Excel Files", "*.xls*"),)
            ),
        ],
        [
            sg.Text("", s=20),
            sg.Exit(s=15, button_color="tomato"),
            sg.B("Settings", s=15),
            sg.B("Kør", s=15),
            sg.Text("", s=20),
        ],
    ]

    window = sg.Window("Økonomiudtræk", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break

        if event in ("Kør"):
            current_date = datetime.date.today().strftime("%Y%m%d")
            file_name_newanalyse = (
                current_date + "_" + settings["PROGRAM"]["basis_file_name"]
            )
            file_path_newanalyse = join(values["-OUTPUTFOLDER-"], file_name_newanalyse)
            exit_code = lisudtraek(
                values["-NEWFILE-"], values["-OLDFILE-"], file_path_newanalyse
            )
            if exit_code == 0:
                sg.popup("Nyt Økonomiudtrækket dannet")
                break
            else:
                sg.popup("Der skete en fejl - Prøv igen")

    window.close()


if __name__ == "__main__":
    SETTINGS_PATH = Path.cwd()
    # create the settings object and use ini format
    settings = sg.UserSettings(
        path=SETTINGS_PATH,
        filename="okonomiudtraek.ini",
        use_config_file=True,
        convert_bools_and_none=True,
    )
    theme = settings["GUI"]["theme"]
    font_family = settings["GUI"]["font_family"]
    font_size = int(settings["GUI"]["font_size"])
    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))
    main_window()
