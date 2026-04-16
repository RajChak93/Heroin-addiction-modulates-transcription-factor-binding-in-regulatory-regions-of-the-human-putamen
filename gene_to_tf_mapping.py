"""
Script: index_TF_binding_by_gene_target_glia.py

Purpose:
    Parses a tab-delimited TOBIAS output file containing TF binding site
    annotations for glial cells and re-indexes the data by gene target.
    Each gene target is listed with all TFs whose binding sites are
    annotated to that gene, enabling gene-centric downstream analysis.

Input:
    - resources/2024_Feb_25/glia_tobias.txt
      Tab-delimited file with 5 columns (no header):
      TF_Name | Chr | Start | End | Gene_Target
      Note: Gene_Target column may contain multiple genes separated by semicolons.

Output:
    - resources/2024_Feb_25/results/output_glia.txt
      Text file grouped by gene target. Format:
        <gene_target>
            <TF_Name>  <Chr>  <Start>  <End>
            <TF_Name>  <Chr>  <Start>  <End>
        ...

Key Parameters:
    - Input delimiter: tab (\t)
    - Gene targets split on: semicolon (;)
    - Expected columns per line: 5 (validated at runtime)

Dependencies:
    - None (standard Python only)
"""

# --- File paths ---
INPUT_FILE = 'resources/2024_Feb_25/glia_tobias.txt'
OUTPUT_FILE = 'resources/2024_Feb_25/results/output_glia.txt'

# Dictionary: gene_target -> list of [tf_name, chr, start, end] entries
gene_target_to_list_rest_map = {}


def validate(line_to_arr):
    """Ensures each parsed line contains exactly 5 tab-separated fields."""
    assert len(line_to_arr) == 5, f"Expected 5 columns, got {len(line_to_arr)}"


# --- Parse input file and index by gene target ---
with open(INPUT_FILE, 'rt') as f:
    for line in f:
        line = line.strip()
        line_to_arr = line.split('\t')
        validate(line_to_arr)

        tf_name, chromosome, start, end, gene_targets = line_to_arr
        curr_list_rest = [tf_name, chromosome, start, end]

        # Gene_Target field may contain multiple genes separated by semicolons
        gene_targets_list = gene_targets.split(';')

        # Index each gene target separately
        for gene_target in gene_targets_list:
            if gene_target in gene_target_to_list_rest_map:
                gene_target_to_list_rest_map[gene_target].append(curr_list_rest)
            else:
                gene_target_to_list_rest_map[gene_target] = [curr_list_rest]

# --- Write gene-centric output ---
with open(OUTPUT_FILE, 'wt') as f:
    for gene_target, list_rest in gene_target_to_list_rest_map.items():
        f.write(gene_target + '\n')
        for rest in list_rest:
            rest_to_str = '\t'.join(str(x) for x in rest)
            f.write('\t' + rest_to_str + '\n')
