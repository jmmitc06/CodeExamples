def solution_REVC(dataset_path):
    rev_complement_mapping = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    with open(dataset_path) as dataset_filehandle:
        nucleotide_string = str(dataset_filehandle.readlines()[0].rstrip())
    return ''.join(reversed([rev_complement_mapping[x] for x in nucleotide_string]))

if __name__ == '__main__':
    import sys
    print(solution_REVC(sys.argv[1]))