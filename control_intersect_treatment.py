"""
Script: compute_pairwise_TF_intersections.py

Purpose:
    Computes pairwise intersections of TF-bound genomic regions across all
    combinations of neuronal and glial cell types in heroin users (treatment)
    and non-users (control). Intersection is based on shared transcription
    factor names in the 'transcription' column.

Input:
    All files located in resources/2023_Dec28/
    - GC_selected_new.xlsx : Selected TF-bound regions, glial cells, non-users (GC)
    - GT_selected_new.xlsx : Selected TF-bound regions, glial cells, heroin users (GT)
    - NC_selected_new.xlsx : Selected TF-bound regions, neuronal cells, non-users (NC)
    - NT_selected_new.xlsx : Selected TF-bound regions, neuronal cells, heroin users (NT)

Output:
    All files written to resources/2023_Dec28/
    - GC_intersect_GT.xlsx : TFs common to glia non-users and glia users
    - GT_intersect_GC.xlsx : TFs common to glia users and glia non-users
    - NC_intersect_NT.xlsx : TFs common to neuron non-users and neuron users
    - NT_intersect_NC.xlsx : TFs common to neuron users and neuron non-users
    - GT_intersect_NT.xlsx : TFs common to glia users and neuron users
    - NT_intersect_GT.xlsx : TFs common to neuron users and glia users
    - GC_intersect_NC.xlsx : TFs common to glia non-users and neuron non-users
    - NC_intersect_GC.xlsx : TFs common to neuron non-users and glia non-users

    Note: Pairwise intersections are computed in both directions (A∩B and B∩A)
    because the output dataframe retains rows from the first input file,
    so row content differs by direction even when TF sets are identical.

Key Parameter:
    - key_column = 'transcription' : Column used to match TFs across datasets

Dependencies:
    - excel_reading_utils (custom utility module, provided in this repository)
    - pandas
"""

import pandas as pd
from pandas import DataFrame
from excel_reading_utils import create_subset_df_from_keyset, get_sanitized_column_values_set


def compute_common_elements(xlsheet_path1: str, xlsheet_path2: str, key_column: str) -> DataFrame:
    """
    Computes the intersection of two Excel sheets based on a shared key column.
    
    Steps:
        1. Read both Excel files into DataFrames
        2. Extract unique values from the key column in each DataFrame
        3. Find the intersection of those value sets
        4. Return subset of path1 DataFrame containing only intersecting rows

    Args:
        xlsheet_path1 (str): Path to first Excel file (rows retained in output)
        xlsheet_path2 (str): Path to second Excel file (used for intersection only)
        key_column (str): Column name to match on (e.g., 'transcription')

    Returns:
        DataFrame: Subset of path1 containing rows where key_column value
                   exists in both path1 and path2
    """
    df_path1: DataFrame = pd.read_excel(io=xlsheet_path1)
    df_path2: DataFrame = pd.read_excel(io=xlsheet_path2)

    # Extract sanitized (cleaned) unique values from key column in each file
    path1_keycolumn_values_set: set = get_sanitized_column_values_set(df_path1, key_column)
    path2_keycolumn_values_set: set = get_sanitized_column_values_set(df_path2, key_column)

    # Compute intersection of key column values
    key_columnvals_path1_intersect_path2: set = path1_keycolumn_values_set.intersection(
        path2_keycolumn_values_set)

    # Subset path1 DataFrame to only rows with intersecting key values
    df_path1_intersect_path2: DataFrame = create_subset_df_from_keyset(
        key_column, key_columnvals_path1_intersect_path2, df_path1)

    return df_path1_intersect_path2


if __name__ == '__main__':

    # --- GC ∩ GT: Glia non-users intersect glia users ---
    df_gc_intersect_gt = compute_common_elements(
        'resources/2023_Dec28/GC_selected_new.xlsx',
        'resources/2023_Dec28/GT_selected_new.xlsx',
        'transcription')
    df_gc_intersect_gt.to_excel('resources/2023_Dec28/GC_intersect_GT.xlsx')
    print(f'rows in GC-GT output DF = {len(df_gc_intersect_gt)}')

    # --- GT ∩ GC: Glia users intersect glia non-users ---
    df_gt_intersect_gc = compute_common_elements(
        'resources/2023_Dec28/GT_selected_new.xlsx',
        'resources/2023_Dec28/GC_selected_new.xlsx',
        'transcription')
    df_gt_intersect_gc.to_excel('resources/2023_Dec28/GT_intersect_GC.xlsx')
    print(f'rows in GT-GC output DF = {len(df_gt_intersect_gc)}')

    # --- NC ∩ NT: Neuron non-users intersect neuron users ---
    df_nc_intersect_nt = compute_common_elements(
        'resources/2023_Dec28/NC_selected_new.xlsx',
        'resources/2023_Dec28/NT_selected_new.xlsx',
        'transcription')
    df_nc_intersect_nt.to_excel('resources/2023_Dec28/NC_intersect_NT.xlsx')
    print(f'rows in NC-NT output DF = {len(df_nc_intersect_nt)}')

    # --- NT ∩ NC: Neuron users intersect neuron non-users ---
    df_nt_intersect_nc = compute_common_elements(
        'resources/2023_Dec28/NT_selected_new.xlsx',
        'resources/2023_Dec28/NC_selected_new.xlsx',
        'transcription')
    df_nt_intersect_nc.to_excel('resources/2023_Dec28/NT_intersect_NC.xlsx')
    print(f'rows in NT-NC output DF = {len(df_nt_intersect_nc)}')

    # --- GT ∩ NT: Glia users intersect neuron users ---
    df_gt_intersect_nt = compute_common_elements(
        'resources/2023_Dec28/GT_selected_new.xlsx',
        'resources/2023_Dec28/NT_selected_new.xlsx',
        'transcription')
    df_gt_intersect_nt.to_excel('resources/2023_Dec28/GT_intersect_NT.xlsx')
    print(f'rows in GT-NT output DF = {len(df_gt_intersect_nt)}')

    # --- NT ∩ GT: Neuron users intersect glia users ---
    df_nt_intersect_gt = compute_common_elements(
        'resources/2023_Dec28/NT_selected_new.xlsx',
        'resources/2023_Dec28/GT_selected_new.xlsx',
        'transcription')
    df_nt_intersect_gt.to_excel('resources/2023_Dec28/NT_intersect_GT.xlsx')
    print(f'rows in NT-GT output DF = {len(df_nt_intersect_gt)}')

    # --- GC ∩ NC: Glia non-users intersect neuron non-users ---
    df_gc_intersect_nc = compute_common_elements(
        'resources/2023_Dec28/GC_selected_new.xlsx',
        'resources/2023_Dec28/NC_selected_new.xlsx',
        'transcription')
    df_gc_intersect_nc.to_excel('resources/2023_Dec28/GC_intersect_NC.xlsx')
    print(f'rows in GC-NC output DF = {len(df_gc_intersect_nc)}')

    # --- NC ∩ GC: Neuron non-users intersect glia non-users ---
    df_nc_intersect_gc = compute_common_elements(
        'resources/2023_Dec28/NC_selected_new.xlsx',
        'resources/2023_Dec28/GC_selected_new.xlsx',
        'transcription')
    df_nc_intersect_gc.to_excel('resources/2023_Dec28/NC_intersect_GC.xlsx')
    print(f'rows in NC-GC output DF = {len(df_nc_intersect_gc)}')
