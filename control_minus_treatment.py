import pandas as pd
from pandas import DataFrame

from excel_reading_utils import create_subset_df_from_keyset, get_sanitized_column_values_set


def compute_difference(xlsheet_path1: str, xlsheet_path2: str, key_column: str) -> DataFrame:
    """
    Main runner of the business logic. Does the following-
    1. Read path1 and path2 in dataframes
    2. For given key column name, find the column value in path1 & path2
    3. Find diff of key column values path1 - path2, create a dataframe of the subset
    :return: dataframes path1-path2
    """
    df_path1: DataFrame = pd.read_excel(io=xlsheet_path1)
    df_path2: DataFrame = pd.read_excel(io=xlsheet_path2)
    # compute difference between path1 and path2 for a particular column
    path1_keycolumn_values_set: set = get_sanitized_column_values_set(df_path1, key_column)
    path2_keycolumn_values_set: set = get_sanitized_column_values_set(df_path2, key_column)
    key_columnvals_path1_minus_path2: set = path1_keycolumn_values_set.difference(path2_keycolumn_values_set)
    df_path1_minus_path2: DataFrame = create_subset_df_from_keyset(key_column, key_columnvals_path1_minus_path2,
                                                                   df_path1)
    return df_path1_minus_path2


if __name__ == '__main__':
    # -------GC-GT---------
    df_gc_minus_gt = compute_difference('resources/2023_Dec7/GC_selected_new.xlsx',
                                        'resources/2023_Dec7/GT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gc_minus_gt.to_excel('resources/2023_Dec7/GC_minus_GT.xlsx')
    print(f'rows in GC-GT output DF = {len(df_gc_minus_gt)}')

    # -------GT-GC---------
    df_gt_minus_gc = compute_difference('resources/2023_Dec7/GT_selected_new.xlsx',
                                        'resources/2023_Dec7/GC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gt_minus_gc.to_excel('resources/2023_Dec7/GT_minus_GC.xlsx')
    print(f'rows in GT-GC output DF = {len(df_gt_minus_gc)}')

    # -------NC-NT---------
    df_nc_minus_nt = compute_difference('resources/2023_Dec7/NC_selected_new.xlsx',
                                        'resources/2023_Dec7/NT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nc_minus_nt.to_excel('resources/2023_Dec7/NC_minus_NT.xlsx')
    print(f'rows in NC-NT output DF = {len(df_nc_minus_nt)}')

    # -------NT-NC---------
    df_nt_minus_nc = compute_difference('resources/2023_Dec7/NT_selected_new.xlsx',
                                        'resources/2023_Dec7/NC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nt_minus_nc.to_excel('resources/2023_Dec7/NT_minus_NC.xlsx')
    print(f'rows in NT-NC output DF = {len(df_nt_minus_nc)}')

    # -------GT-NT---------
    df_gt_minus_nt = compute_difference('resources/2023_Dec7/GT_selected_new.xlsx',
                                        'resources/2023_Dec7/NT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gt_minus_nt.to_excel('resources/2023_Dec7/GT_minus_NT.xlsx')
    print(f'rows in GT-NT output DF = {len(df_gt_minus_nt)}')

    # -------NT-GT---------
    df_nt_minus_gt = compute_difference('resources/2023_Dec7/NT_selected_new.xlsx',
                                        'resources/2023_Dec7/GT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nt_minus_gt.to_excel('resources/2023_Dec7/NT_minus_GT.xlsx')
    print(f'rows in NT-GT output DF = {len(df_nt_minus_gt)}')

    # -------GC-NC---------
    df_gc_minus_nc = compute_difference('resources/2023_Dec7/GC_selected_new.xlsx',
                                        'resources/2023_Dec7/NC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gc_minus_nc.to_excel('resources/2023_Dec7/GC_minus_NC.xlsx')
    print(f'rows in GC-NC output DF = {len(df_gc_minus_nc)}')

    # -------NC-GC---------
    df_nc_minus_gc = compute_difference('resources/2023_Dec7/NC_selected_new.xlsx',
                                        'resources/2023_Dec7/GC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nc_minus_gc.to_excel('resources/2023_Dec7/NC_minus_GC.xlsx')
    print(f'rows in NC-GC output DF = {len(df_nc_minus_gc)}')
