import pandas as pd
from pandas import DataFrame

from excel_reading_utils import create_subset_df_from_keyset, get_sanitized_column_values_set


def compute_common_elements(xlsheet_path1: str, xlsheet_path2: str, key_column: str) -> DataFrame:
    """
    Main runner of the business logic. Does the following-
    1. Read path1 and path2 in dataframes
    2. For given key column name, find the column value in path1 & path2
    3. Find intersection of key column values path1 - path2, create a dataframe of the subset
    :return: dataframes path1 INTERSECT path2
    """
    df_path1: DataFrame = pd.read_excel(io=xlsheet_path1)
    df_path2: DataFrame = pd.read_excel(io=xlsheet_path2)
    # compute intersection between path1 and path2 for a particular column
    path1_keycolumn_values_set: set = get_sanitized_column_values_set(df_path1, key_column)
    path2_keycolumn_values_set: set = get_sanitized_column_values_set(df_path2, key_column)
    key_columnvals_path1_intersect_path2: set = path1_keycolumn_values_set.intersection(path2_keycolumn_values_set)
    df_path1_intersect_path2: DataFrame = create_subset_df_from_keyset(key_column, key_columnvals_path1_intersect_path2,
                                                                   df_path1)
    return df_path1_intersect_path2


if __name__ == '__main__':
    # -------GC-GT---------
    df_gc_intersect_gt = compute_common_elements('resources/2023_Dec28/GC_selected_new.xlsx',
                                        'resources/2023_Dec28/GT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gc_intersect_gt.to_excel('resources/2023_Dec28/GC_intersect_GT.xlsx')
    print(f'rows in GC-GT output DF = {len(df_gc_intersect_gt)}')

    # -------GT-GC---------
    df_gt_intersect_gc = compute_common_elements('resources/2023_Dec28/GT_selected_new.xlsx',
                                        'resources/2023_Dec28/GC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gt_intersect_gc.to_excel('resources/2023_Dec28/GT_intersect_GC.xlsx')
    print(f'rows in GT-GC output DF = {len(df_gt_intersect_gc)}')

    # -------NC-NT---------
    df_nc_intersect_nt = compute_common_elements('resources/2023_Dec28/NC_selected_new.xlsx',
                                        'resources/2023_Dec28/NT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nc_intersect_nt.to_excel('resources/2023_Dec28/NC_intersect_NT.xlsx')
    print(f'rows in NC-NT output DF = {len(df_nc_intersect_nt)}')

    # -------NT-NC---------
    df_nt_intersect_nc = compute_common_elements('resources/2023_Dec28/NT_selected_new.xlsx',
                                        'resources/2023_Dec28/NC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nt_intersect_nc.to_excel('resources/2023_Dec28/NT_intersect_NC.xlsx')
    print(f'rows in NT-NC output DF = {len(df_nt_intersect_nc)}')

    # -------GT-NT---------
    df_gt_intersect_nt = compute_common_elements('resources/2023_Dec28/GT_selected_new.xlsx',
                                        'resources/2023_Dec28/NT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gt_intersect_nt.to_excel('resources/2023_Dec28/GT_intersect_NT.xlsx')
    print(f'rows in GT-NT output DF = {len(df_gt_intersect_nt)}')

    # -------NT-GT---------
    df_nt_intersect_gt = compute_common_elements('resources/2023_Dec28/NT_selected_new.xlsx',
                                        'resources/2023_Dec28/GT_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nt_intersect_gt.to_excel('resources/2023_Dec28/NT_intersect_GT.xlsx')
    print(f'rows in NT-GT output DF = {len(df_nt_intersect_gt)}')

    # -------GC-NC---------
    df_gc_intersect_nc = compute_common_elements('resources/2023_Dec28/GC_selected_new.xlsx',
                                        'resources/2023_Dec28/NC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_gc_intersect_nc.to_excel('resources/2023_Dec28/GC_intersect_NC.xlsx')
    print(f'rows in GC-NC output DF = {len(df_gc_intersect_nc)}')

    # -------NC-GC---------
    df_nc_intersect_gc = compute_common_elements('resources/2023_Dec28/NC_selected_new.xlsx',
                                        'resources/2023_Dec28/GC_selected_new.xlsx',
                                        'transcription')
    # write result DFs to excel sheet
    df_nc_intersect_gc.to_excel('resources/2023_Dec28/NC_intersect_GC.xlsx')
    print(f'rows in NC-GC output DF = {len(df_nc_intersect_gc)}')
