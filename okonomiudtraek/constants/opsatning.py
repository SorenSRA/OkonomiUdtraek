from dataclasses import dataclass


@dataclass
class Col_struktur:
    col_name: str
    std_data: str


drill_sheet_name = r"Drill-through"
afstem_sheet_name = r"SRAAfstemning"
budget_sheet_name = r"SRABudgetopfolgning"

opgave_sheet = r"Okonomi"
path_to_opgavenr = r"F:/EUOkonomi/LIFE-Okonomi/Opfolgning/SystemFiler/OpgaveNumre.xlsx"

index_col = r"Finanspost Detaljer Entry No"
opg_col = r"Opgave Dim Opgave"
arts_col = r"Artskonto Dim_artskonto"
formal_col = r"Formål Dim Formål"
maaned_col = r"Tid Tid.Måned"

proj_col = Col_struktur("SRA_Projekt", "")
konto_col = Col_struktur("SRA_Konto", "")
kvt_col = Col_struktur("SRA_Kvt", 0)
korr_col = Col_struktur("SRA_Korr", 0.0)
kat_col = Col_struktur("SRA_Kat", 0.0)
stat_col = Col_struktur("SRA_STA", "")

new_opfolg_col = [proj_col, konto_col, kvt_col]
new_afstem_col = [korr_col, kat_col, stat_col, proj_col]

indsaet_loc = 3  # som hvilket kolonnenummer skal de nye kolonner indsættes, startindex 0, så 3 betyder kolonne nr. 4
