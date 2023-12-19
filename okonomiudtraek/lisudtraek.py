import pandas as pd


from helper.helper import findesexcelark
from ownfunc.artskonti import srakonto
from ownfunc.opagvenr import projekt
from ownfunc.kvartal import kvartal

from constants.opsatning import *


def indlas_df(path, sheet):
    if findesexcelark(path):
        return pd.read_excel(path, sheet_name=sheet)
    else:
        return None


def lav_dataframes_new(path_to_new_udtrak):
    df_drill = indlas_df(path_to_new_udtrak, drill_sheet_name)
    if isinstance(df_drill, pd.DataFrame):
        df_budgetop = df_drill.copy()
        df_afstem = df_drill.copy()
        df_afstem.set_index(index_col, inplace=True)
        df_afstem.sort_index(inplace=True)

    else:
        print(path_to_new_udtrak)
        print("Ny indlæsnings-Fil findes ikke")
        return 99

    return (df_drill, df_budgetop, df_afstem)


def lav_dataframes_old(path_to_old_udtrak):
    df_oldafstem = indlas_df(path_to_old_udtrak, afstem_sheet_name)
    if isinstance(df_oldafstem, pd.DataFrame):
        df_oldafstem.set_index(index_col, inplace=True)
    else:
        print(path_to_old_udtrak)
        print("Gammel afstemning-Fil findes ikke")
        return 99

    return df_oldafstem


def indsat_col(df, loc, cols):
    for col in cols:
        df.insert(loc=loc, column=col.col_name, value=col.std_data)
        loc += 1

    return df


def opdater_opfolg(df):
    df = indsat_col(df, indsaet_loc, new_opfolg_col)
    for index, row in df.iterrows():
        df.loc[index, proj_col.col_name] = projekt(df.loc[index, opg_col])
        df.loc[index, kvt_col.col_name] = kvartal(df.loc[index, maaned_col])
        df.loc[index, konto_col.col_name] = srakonto(
            df.loc[index, arts_col], df.loc[index, formal_col]
        )
    df.sort_values(index_col, axis=0, inplace=True)
    return df


def opdater_afstem(df, df_old):
    df = indsat_col(df, indsaet_loc, new_afstem_col)
    for index, row in df.iterrows():
        if skal_rk_slettes(df.loc[index, arts_col]):
            df.drop(index, axis=0, inplace=True)
        else:
            df.loc[index, proj_col.col_name] = projekt(df.loc[index, opg_col])
            df.loc[index, korr_col.col_name] = hent_fra_old(
                df_old, index, korr_col.col_name
            )
            df.loc[index, kat_col.col_name] = hent_fra_old(
                df_old, index, kat_col.col_name
            )
            df.loc[index, stat_col.col_name] = hent_fra_old(
                df_old, index, stat_col.col_name
            )

    return df


def hent_fra_old(df, index, col):
    if index in df.index:
        return df.loc[index, col]
    else:
        return


def skal_rk_slettes(artskonto: str) -> bool:
    konto_nr = int(artskonto[:6])
    if konto_nr < 315501:
        return False
    else:
        return True


def lisudtraek(file_path_newudtrak, file_path_oldudtrak, file_path_newanalyse):
    df_tupple = lav_dataframes_new(file_path_newudtrak)
    if df_tupple == 99:
        return 99
    else:
        df_drill, df_budgetop, df_afstem = df_tupple

    df_oldafstem = lav_dataframes_old(file_path_oldudtrak)
    if df_tupple == 99:
        return 99

    df_budgetop = opdater_opfolg(df_budgetop)
    df_afstem = opdater_afstem(df_afstem, df_oldafstem)

    # df_empty = pd.DataFrame()
    # df_empty.to_excel(file_path_newanalyse, index)

    with pd.ExcelWriter(file_path_newanalyse, mode="w") as writer:
        # Insert the DataFrame into an Excel sheet
        df_drill.to_excel(writer, sheet_name=drill_sheet_name, index=False)
        df_afstem.to_excel(writer, sheet_name=afstem_sheet_name, index=True)
        df_budgetop.to_excel(writer, sheet_name=budget_sheet_name, index=False)

    return 0  # alt gik godt


if __name__ == "__main__":
    exit_code = lisudtraek()
    exit(exit_code)
