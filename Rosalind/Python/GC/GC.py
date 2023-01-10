from collections import OrderedDict


def calculate_GC(dna):
    GC_count = dna.count("G") + dna.count("C")
    return round(100*GC_count / len(dna),4)

def solution_GC(dataset_path):
    current_fasta, current_fasta_id = None, None
    with open(dataset_path) as dataset_filehandle:
        for line in dataset_filehandle:
            if line.startswith(">Rosalind"):
                if current_fasta:
                    print(current_fasta_id)
                    print(calculate_GC(current_fasta))
                current_fasta, current_fasta_id = '', line.rstrip()[1:]
            else:
                current_fasta += line.rstrip()
    if current_fasta:
        print(current_fasta_id)
        print(calculate_GC(current_fasta))

if __name__ == '__main__':
    import sys
    solution_GC(sys.argv[1])