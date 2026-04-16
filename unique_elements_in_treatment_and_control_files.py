"""
Script: extract_unique_TF_binding_coordinates.py

Purpose:
    For a given TF (here ZNF610), reads a CSV file containing genomic binding
    coordinates for heroin users (treatment) and non-users (control) and
    identifies coordinates unique to each group via set difference.
    Produces two output files per TF: regions exclusive to control and
    regions exclusive to treatment.

Input:
    - resources/2024_04_09/ZNF610_MA1713.csv
      CSV file with 6 columns (no header row expected):
      Col 0: Chr (treatment) | Col 1: Start (treatment) | Col 2: End (treatment)
      Col 3: Chr (control)   | Col 4: Start (control)   | Col 5: End (control)
      Note: Empty rows (NaN in Start column) are skipped automatically.
      Note: Original file format has 7 columns with a blank middle column;
            this was removed manually before processing (Piu's edit).

Output:
    - resources/2024_04_09/results/ZNF610_MA1713.csv_unique_elements_c_minus_t.txt
      Genomic coordinates unique to control (not found in treatment)
    - resources/2024_04_09/results/ZNF610_MA1713.csv_unique_elements_t_minus_c.txt
      Genomic coordinates unique to treatment (not found in control)

    Output format per line: Chr,Start,End (comma-separated string)

Key Parameters:
    - Coordinates represented as strings: "chr,start,end" with int-cast
      start/end to remove trailing .0 from float parsing
    - Empty rows detected by NaN check on Start column (col index 1)

Dependencies:
    - pandas
    - math (for NaN detection)
"""

import math
import pandas as pd


def read_two_sets_from_xl_file(path_to_xl: str):
    """
    Reads a 6-column CSV file and returns two sets of genomic coordinates:
    one for treatment (heroin users) and one for control (non-users).

    Args:
        path_to_xl (str): Path to the CSV file

    Returns:
        tuple: (treatment_set, control_set)
               Each set contains strings of format "Chr,Start,End"
    """
    df = pd.read_csv(path_to_xl)

    # First 3 columns = treatment; next 3 columns = control
    df_treatment = df.iloc[:, 0:3]
    df_control = df.iloc[:, 3:6]  # middle blank column removed prior to input

    treatment_set = set()
    control_set = set()

    # Build treatment set; skip empty rows (NaN in Start column)
    for i in range(len(df_treatment)):
        if math.isnan(df_treatment.iloc[i, 1]):
            continue
        string_rep = (str(df_treatment.iloc[i, 0]) + ',' +
                      str(int(df_treatment.iloc[i, 1])) + ',' +
                      str(int(df_treatment.iloc[i, 2])))
        treatment_set.add(string_rep)

    # Build control set; skip empty rows
    for i in range(len(df_control)):
        if math.isnan(df_control.iloc[i, 1]):
            continue
        string_rep = (str(df_control.iloc[i, 0]) + ',' +
                      str(int(df_control.iloc[i, 1])) + ',' +
                      str(int(df_control.iloc[i, 2])))
        control_set.add(string_rep)

    return treatment_set, control_set


def print_set_to_file(filepath: str, objset: set):
    """
    Writes all elements of a set to a text file, one element per line.

    Args:
        filepath (str): Output file path
        objset (set): Set of coordinate strings to write
    """
    output_str = '\n'.join(str(element) for element in objset)
    with open(filepath, 'wt') as f:
        print(output_str, file=f)


# --- Main processing ---
# Note: Input CSV must be exported from Excel/Numbers to CSV before running
FOLDER_PATH = "resources/2024_04_09/"
filenames = ['ZNF610_MA1713.csv']

for filename in filenames:
    xl_file_path = FOLDER_PATH + filename
    output_c_minus_t_path = FOLDER_PATH + 'results/' + filename + '_unique_elements_c_minus_t.txt'
    output_t_minus_c_path = FOLDER_PATH + 'results/' + filename + '_unique_elements_t_minus_c.txt'

    # Read treatment and control coordinate sets
    set_t, set_c = read_two_sets_from_xl_file(xl_file_path)

    # Compute unique coordinates per group
    unique_elements_c_minus_t = set_c.difference(set_t)  # unique to control
    unique_elements_t_minus_c = set_t.difference(set_c)  # unique to treatment

    print(f'''
    File {filename}:
      set_c (control) has {len(set_c)} elements
      set_t (treatment) has {len(set_t)} elements
      unique to control (c - t): {len(unique_elements_c_minus_t)} elements
      unique to treatment (t - c): {len(unique_elements_t_minus_c)} elements
    ''')

    print_set_to_file(output_c_minus_t_path, unique_elements_c_minus_t)
    print_set_to_file(output_t_minus_c_path, unique_elements_t_minus_c)
