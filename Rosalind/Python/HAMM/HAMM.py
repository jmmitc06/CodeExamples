import itertools

def read_input(filepath):
    dna_string_pairs = []
    with open(filepath) as filehandle:
        #this iterates over the file two lines at a time
        for dna1, dna2 in itertools.zip_longest(*[filehandle]*2):
            dna_string_pairs.append((dna1.rstrip(), dna2.rstrip()))
    return dna_string_pairs

def solution_HAMM(dna1, dna2):
    return sum([bp_1 != bp_2 for bp_1, bp_2 in zip([*dna1], [*dna2])])

if __name__ == '__main__':
    import sys
    dna_string_pairs = read_input(sys.argv[1])
    for dna_string_pair in dna_string_pairs:
        print(solution_HAMM(*dna_string_pair))


