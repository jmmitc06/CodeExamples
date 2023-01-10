import itertools
import re

def read_input(filepath):
    dna_motif_pairs = []
    with open(filepath) as filehandle:
        #this iterates over the file two lines at a time
        for dna, motif in itertools.zip_longest(*[filehandle]*2):
            dna_motif_pairs.append((dna.rstrip(), motif.rstrip()))
    return dna_motif_pairs

def solution_SUBS(dna_motif_pairs):
    solutions = []
    for dna, motif in dna_motif_pairs:
        matches = []
        start = 0
        while True:
            start = dna.find(motif, start)
            if start != -1:
                #indexing starts at 1 for rosalind
                matches.append(start + 1)
                start += 1
            else:
                break
        print(' '.join([str(x) for x in matches]))
        solutions.append((dna, motif, matches))

if __name__ == '__main__':
    import sys
    dna_motif_pairs = read_input(sys.argv[1])
    solution_SUBS(dna_motif_pairs)
