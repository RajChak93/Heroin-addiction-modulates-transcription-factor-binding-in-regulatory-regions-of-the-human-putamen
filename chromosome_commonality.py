"""
Script: find_common_TF_binding_regions.py

Purpose:
    Identifies common (shared) TF-bound genomic regions within and across
    neuronal and glial cell types in heroin users (treatment) and non-users (control).
    
Input:
    - Glia_control.xlsx   : TF-bound regions in glial cells, non-users
    - glia_treatment.xlsx : TF-bound regions in glial cells, heroin users
    - Neuron_control.xlsx : TF-bound regions in neuronal cells, non-users
    - Neuron_treatment.xlsx: TF-bound regions in neuronal cells, heroin users
    (All files located in resources/oct12/)

Output:
    - Glia_control_commonalities.txt         : Common regions across all sheets in glia control
    - glia_treatment_commonalities.txt       : Common regions across all sheets in glia treatment
    - neuron_control_commonalities.txt       : Common regions across all sheets in neuron control
    - neuron_treatment_commonalities.txt     : Common regions across all sheets in neuron treatment
    - commonality_set_glia_control_treatment.txt    : Shared regions between glia control and treatment
    - commonality_set_neuron_control_treatment.txt  : Shared regions between neuron control and treatment
    - commonality_set_all4.txt               : Regions common across all four groups

Parameters:
    - read_all_excel_sheets_data_into_set() called with 'col' parameter,
      meaning commonality is computed column-wise across sheets

Dependencies:
    - excel_reading_utils (custom utility module, provided in this repository)
"""

from excel_reading_utils import read_all_excel_sheets_data_into_set

# --- Input files ---
xl_files = [
    'resources/oct12/Glia_control.xlsx',
    'resources/oct12/glia_treatment.xlsx',
    'resources/oct12/Neuron_control.xlsx',
    'resources/oct12/Neuron_treatment.xlsx'
]

# --- Find common TF-bound regions within each group ---
commonality_set_glia_control = read_all_excel_sheets_data_into_set(
    'resources/oct12/Glia_control.xlsx', 'col')
print(f'commonality set of glia_control has {len(commonality_set_glia_control)} elements')
with open('resources/oct12/Glia_control_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_glia_control))

commonality_set_glia_treatment = read_all_excel_sheets_data_into_set(
    'resources/oct12/glia_treatment.xlsx', 'col')
print(f'commonality set of glia_treatment has {len(commonality_set_glia_treatment)} elements')
with open('resources/oct12/glia_treatment_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_glia_treatment))

commonality_set_neuron_control = read_all_excel_sheets_data_into_set(
    'resources/oct12/Neuron_control.xlsx', 'col')
print(f'commonality set of Neuron_control has {len(commonality_set_neuron_control)} elements')
with open('resources/oct12/neuron_control_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_neuron_control))

commonality_set_neuron_treatment = read_all_excel_sheets_data_into_set(
    'resources/oct12/Neuron_treatment.xlsx', 'col')
print(f'commonality set of Neuron_treatment has {len(commonality_set_neuron_treatment)} elements')
with open('resources/oct12/neuron_treatment_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_neuron_treatment))

# --- Cross-group intersections ---

# Common regions between glia control and glia treatment
commonality_set_glia_control_treatment = commonality_set_glia_control.intersection(
    commonality_set_glia_treatment)
print(f'commonality set of glia_control/glia_treatment has '
      f'{len(commonality_set_glia_control_treatment)} elements')
with open('resources/oct12/commonality_set_glia_control_treatment.txt', 'xt') as f:
    f.write("\n".join(commonality_set_glia_control_treatment))

# Common regions between neuron control and neuron treatment
commonality_set_neuron_control_treatment = commonality_set_neuron_control.intersection(
    commonality_set_neuron_treatment)
print(f'commonality set of neuron_control/neuron_treatment has '
      f'{len(commonality_set_neuron_control_treatment)} elements')
with open('resources/oct12/commonality_set_neuron_control_treatment.txt', 'xt') as f:
    f.write("\n".join(commonality_set_neuron_control_treatment))

# Common regions across all four groups
commonality_set_all4 = commonality_set_glia_control_treatment.intersection(
    commonality_set_neuron_control_treatment)
print(f'commonality set of all 4 has {len(commonality_set_all4)} elements')
with open('resources/oct12/commonality_set_all4.txt', 'xt') as f:
    f.write("\n".join(commonality_set_all4))

print("Done")
