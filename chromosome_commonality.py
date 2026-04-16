from excel_reading_utils import read_all_excel_sheets_data_into_set

xl_files = ['resources/oct12/Glia_control.xlsx', 'resources/oct12/glia_treatment.xlsx',
            'resources/oct12/Neuron_control.xlsx', 'resources/oct12/Neuron_treatment.xlsx']

commonality_set_glia_control = read_all_excel_sheets_data_into_set('resources/oct12/Glia_control.xlsx', 'col')
print(f'commanlity set of glia_control has {len(commonality_set_glia_control)} elements')
with open('resources/oct12/Glia_control_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_glia_control))

commonality_set_glia_treatment = read_all_excel_sheets_data_into_set('resources/oct12/glia_treatment.xlsx', 'col')
print(f'commanlity set of glia_treatment has {len(commonality_set_glia_treatment)} elements')
with open('resources/oct12/glia_treatment_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_glia_treatment))

commonality_set_neuron_control = read_all_excel_sheets_data_into_set('resources/oct12/Neuron_control.xlsx', 'col')
print(f'commanlity set of Neuron_control has {len(commonality_set_neuron_control)} elements')
with open('resources/oct12/neuron_control_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_neuron_control))

commonality_set_neuron_treatment = read_all_excel_sheets_data_into_set('resources/oct12/Neuron_treatment.xlsx', 'col')
print(f'commanlity set of Neuron_treatment has {len(commonality_set_neuron_treatment)} elements')
with open('resources/oct12/neuron_treatment_commonalities.txt', 'xt') as f:
    f.write("\n".join(commonality_set_neuron_treatment))

commonality_set_glia_control_treatment = commonality_set_glia_control.intersection(commonality_set_glia_treatment)
print(f'commanlity set of glia_control/glia_treatment has {len(commonality_set_glia_control_treatment)} elements')
with open('resources/oct12/commonality_set_glia_control_treatment.txt', 'xt') as f:
    f.write("\n".join(commonality_set_glia_control_treatment))

commonality_set_neuron_control_treatment = commonality_set_neuron_control.intersection(commonality_set_neuron_treatment)
print(f'commanlity set of neuron_control/neuron_treatment has {len(commonality_set_neuron_control_treatment)} elements')
with open('resources/oct12/commonality_set_neuron_control_treatment.txt', 'xt') as f:
    f.write("\n".join(commonality_set_neuron_control_treatment))

commonality_set_all4 = commonality_set_glia_control_treatment.intersection(commonality_set_neuron_control_treatment)
print(f'commanlity set of all 4 has {len(commonality_set_all4)} elements')
with open('resources/oct12/commonality_set_all4.txt', 'xt') as f:
    f.write("\n".join(commonality_set_all4))

print("Done")
