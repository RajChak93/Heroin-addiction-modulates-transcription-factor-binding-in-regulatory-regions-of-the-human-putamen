# TF_Name	Chr	Start	End	Gene Target

INPUT_FILE = 'resources/2024_Feb_25/glia_tobias.txt'
OUTPUT_FILE = 'resources/2024_Feb_25/results/output_glia.txt'


# Map of gene_target -> [tf,chr,start,end]1, [tf,chr,start,end]2 ... (list)
gene_target_to_list_rest_map = {}

# Iterate over the lines of the file
def validate(line_to_arr):
    assert len(line_to_arr) == 5


with open(INPUT_FILE, 'rt') as f:
    for line in f:
        # process line
        line = line.strip()
        line_to_arr = line.split('\t')
        validate(line_to_arr)
        tf_name, chromosome, start, end, gene_targets = line_to_arr
        curr_list_rest = [tf_name, chromosome, start, end]
        # break gene_targets
        gene_targets_list = gene_targets.split(';')
        # index every gene target
        for gene_target in gene_targets_list:
            if gene_target in gene_target_to_list_rest_map:
                # append to existing list
                existing_list_rest = gene_target_to_list_rest_map[gene_target]
                new_list_rest = existing_list_rest.append(curr_list_rest)
            else:
                gene_target_to_list_rest_map[gene_target] = [curr_list_rest]

# process gene_target_to_rest_map into a neat txt file
with open(OUTPUT_FILE, 'wt') as f:
    for gene_target,list_rest in gene_target_to_list_rest_map.items():
        f.write(gene_target+'\n')
        for rest in list_rest:
            rest_to_str = '\t'.join(str(x) for x in rest)
            f.write('\t'+rest_to_str+'\n')