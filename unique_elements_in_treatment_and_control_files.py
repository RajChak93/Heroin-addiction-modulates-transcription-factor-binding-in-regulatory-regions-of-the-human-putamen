import glob
import math

import pandas as pd
import argparse


def read_two_sets_from_xl_file(path_to_xl: str):
    """
    XL file has 6 cols - treatment,start,end,BLANK, control,start,end
    We are reading first 3 cols (treatment) into a set and the next 3 cols (control) in another set
    :param path_to_xl: xl file path
    :return: 2 sets- treatment and control
    """
    obj_set = set()
    df = pd.read_csv(path_to_xl)
    df_treatment = df.iloc[:, 0:3]
    # df_control = df.iloc[:, 4:7] Piu removed middle space
    df_control = df.iloc[:, 3:6]
    treatment_set = set()
    control_set = set()
    for i in range(len(df_treatment)):
        # ignore empty rows, so checking if the second element (integer) is nan
        if math.isnan(df_treatment.iloc[i, 1]):
            continue
        # TODO: better hashing, we have to put int(col1) and int(col2) to eliminate .0s
        string_rep = str(df_treatment.iloc[i, 0]) + ',' + str(int(df_treatment.iloc[i, 1])) + ',' + str(
            int(df_treatment.iloc[i, 2]))
        treatment_set.add(string_rep)

    for i in range(len(df_control)):
        if math.isnan(df_control.iloc[i, 1]):
            continue
        string_rep = str(df_control.iloc[i, 0]) + ',' + str(int(df_control.iloc[i, 1])) + ',' + str(
            int(df_control.iloc[i, 2]))
        control_set.add(string_rep)
    return treatment_set, control_set


def print_set_to_file(filepath: str, objset: set):
    output_str = ''
    for element in objset:
        output_str = output_str + str(element) + '\n'
    with open(filepath, 'wt') as f:
        print(output_str, file=f)


# business logic
FOLDER_PATH = "resources/2024_04_09/"
# processing: 1) Open xlsx file using Numbers 2)export to CSV
filenames = ['ZNF610_MA1713.csv']

for filename in filenames:
    xl_file_path = FOLDER_PATH + filename
    output_c_minus_t_path = FOLDER_PATH + 'results/' + filename + '_unique_elements_c_minus_t.txt'
    output_t_minus_c_path = FOLDER_PATH + 'results/' + filename + '_unique_elements_t_minus_c.txt'
    set_t, set_c = read_two_sets_from_xl_file(xl_file_path)
    unique_elements_c_minus_t = set_c.difference(set_t)
    unique_elements_t_minus_c = set_t.difference(set_c)
    print(f'''
    File {filename} : set_c has {len(set_c)} elements, set_t has {len(set_t)} elements
    unique_elements_c_minus_t has {len(unique_elements_c_minus_t)} elements,
    unique_elements_t_minus_c has {len(unique_elements_t_minus_c)} elements
    ''')
    print_set_to_file(output_c_minus_t_path, unique_elements_c_minus_t)
    print_set_to_file(output_t_minus_c_path, unique_elements_t_minus_c)
