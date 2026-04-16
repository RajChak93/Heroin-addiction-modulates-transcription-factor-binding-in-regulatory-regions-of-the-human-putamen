"""
Script: compute_pairwise_TF_differences.py

Purpose:
    Computes pairwise differences of TF-bound genomic regions across all
    combinations of neuronal and glial cell types in heroin users (treatment)
    and non-users (control). Identifies TFs unique to one group by subtracting
    shared TFs found in the comparison group, based on the 'transcription' column.

Input:
    All files located in resources/2023_Dec7/
    - GC_selected_new.xlsx : Selected TF-bound regions, glial cells, non-users (GC)
    - GT_selected_new.xlsx : Selected TF-bound regions, glial cells, heroin users (GT)
    - NC_selected_new.xlsx : Selected TF-bound regions, neuronal cells, non-users (NC)
    - NT_selected_new.xlsx : Selected TF-bound regions, neuronal cells, heroin users (NT)

Output:
    All files written to resources/2023_Dec7/
    - GC_minus_GT.xlsx : TFs unique to glia non-users (not in glia users)
    - GT_minus_GC.xlsx : TFs unique to glia users (not in glia non-users)
    - NC_minus_NT.xlsx : TFs unique to neuron non-users (not in neuron users)
    - NT_minus_NC.xlsx : TFs unique to neuron users (not in neuron non-users)
    - GT_minus_NT.xlsx : TFs unique to glia users (not in neuron users)
    - NT_minus_GT.xlsx : TFs unique to neuron users (not in glia users)
    - GC_minus_NC.xlsx : TFs unique to glia non-users (not in neuron non-users)
    - NC_minus_GC.xlsx : TFs unique to neuron non-users (not in glia non-users)

Key Parameter:
    - key_column = 'transcription' : Column used to identify and subtract TFs

Dependencies:
    - excel_reading_utils (custom utility module, provided in this repository)
    - pandas
"""

import pandas as pd
from pandas import DataFrame
from excel_reading_utils import create_subset_df_from_keyset, get_sanitized_column_values_set


def compute_difference(xlsheet_path1: str, xlsheet_path2: str, key_column: str) -> DataFrame:
    """
    Computes the set difference of two Excel sheets based on a shared key column.
    Returns rows from path1 whose key_column value is NOT present in path2.

    Steps:
        1. Read both Excel files into DataFrames
        2. Extract unique values from key column in each DataFrame
        3. Compute set difference: path1 values minus path2 values
        4. Return subset of path1 DataFrame containing only rows unique to path1

    Args:
        xlsheet_path1 (str): Path to first Excel file (rows retained in output)
        xlsheet_path2 (str): Path to second Excel file (used for subtraction only)
        key_column (str): Column name to match on (e.g., 'transcription')

    Returns:
        DataFrame: Subset of path1 containing rows where key_column value
                   is absent in path2 (i.e., unique to path1)
    """
    df_path1: DataFrame = pd.read_excel(io=xlsheet_path1)
    df_path2: DataFrame = pd.read_excel(io=xlsheet_path2)

    # Extract sanitized unique values from key column in each file
    path1_keycolumn_values_set: set = get_sanitized_column_values_set(df_path1, key_column)
    path2_keycolumn_values_set: set = get_sanitized_column_values_set(df_path2, key_column)

    # Compute set difference: TFs in path1 but not in path2
    key_columnvals_path1_minus_path2: set = path1_keycolumn_values_set.difference(
        path2_keycolumn_values_set)

    # Subset path1 DataFrame to only unique rows
    df_path1_minus_path2: DataFrame = create_subset_df_from_keyset(
        key_column, key_columnvals_path1_minus_path2, df_path1)

    return df_path1_minus_path2


if __name__ == '__main__':

    # --- GC - GT: TFs unique to glia non-users ---
    df_gc_minus_gt = compute_difference(
        'resources/2023_Dec7/GC_selected_new.xlsx',
        'resources/2023_Dec7/GT_selected_new.xlsx',
        'transcription')
    df_gc_minus_gt.to_excel('resources/2023_Dec7/GC_minus_GT.xlsx')
    print(f'rows in GC-GT output DF = {len(df_gc_minus_gt)}')

    # --- GT - GC: TFs unique to glia users ---
    df_gt_minus_gc = compute_difference(
        'resources/2023_Dec7/GT_selected_new.xlsx',
        'resources/2023_Dec7/GC_selected_new.xlsx',
        'transcription')
    df_gt_minus_gc.to_excel('resources/2023_Dec7/GT_minus_GC.xlsx')
    print(f'rows in GT-GC output DF = {len(df_gt_minus_gc)}')

    # --- NC - NT: TFs unique to neuron non-users ---
    df_nc_minus_nt = compute_difference(
        'resources/2023_Dec7/NC_selected_new.xlsx',
        'resources/2023_Dec7/NT_selected_new.xlsx',
        'transcription')
    df_nc_minus_nt.to_excel('resources/2023_Dec7/NC_minus_NT.xlsx')
    print(f'rows in NC-NT output DF = {len(df_nc_minus_nt)}')

    # --- NT - NC: TFs unique to neuron users ---
    df_nt_minus_nc = compute_difference(
        'resources/2023_Dec7/NT_selected_new.xlsx',
        'resources/2023_Dec7/NC_selected_new.xlsx',
        'transcription')
    df_nt_minus_nc.to_excel('resources/2023_Dec7/NT_minus_NC.xlsx')
    print(f'rows in NT-NC output DF = {len(df_nt_minus_nc)}')

    # --- GT - NT: TFs unique to glia users vs neuron users ---
    df_gt_minus_nt = compute_difference(
        'resources/2023_Dec7/GT_selected_new.xlsx',
        'resources/2023_Dec7/NT_selected_new.xlsx',
        'transcription')
    df_gt_minus_nt.to_excel('resources/2023_Dec7/GT_minus_NT.xlsx')
    print(f'rows in GT-NT output DF = {len(df_gt_minus_nt)}')

    # --- NT - GT: TFs unique to neuron users vs glia users ---
    df_nt_minus_gt = compute_difference(
        'resources/2023_Dec7/NT_selected_new.xlsx',
        'resources/2023_Dec7/GT_selected_new.xlsx',
        'transcription')
    df_nt_minus_gt.to_excel('resources/2023_Dec7/NT_minus_GT.xlsx')
    print(f'rows in NT-GT output DF = {len(df_nt_minus_gt)}')

    # --- GC - NC: TFs unique to glia non-users vs neuron non-users ---
    df_gc_minus_nc = compute_difference(
        'resources/2023_Dec7/GC_selected_new.xlsx',
        'resources/2023_Dec7/NC_selected_new.xlsx',
        'transcription')
    df_gc_minus_nc.to_excel('resources/2023_Dec7/GC_minus_NC.xlsx')
    print(f'rows in GC-NC output DF = {len(df_gc_minus_nc)}')

    # --- NC - GC: TFs unique to neuron non-users vs glia non-users ---
    df_nc_minus_gc = compute_difference(
        'resources/2023_Dec7/NC_selected_new.xlsx',
        'resources/2023_Dec7/GC_selected_new.xlsx',
        'transcription')
    df_nc_minus_gc.to_excel('resources/2023_Dec7/NC_minus_GC.xlsx')
    print(f'rows in NC-GC output DF = {len(df_nc_minus_gc)}')
