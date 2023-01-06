from collections import Counter, defaultdict

def solution_DNA(dataset_path):
    with open(dataset_path) as dataset_filehandle:
        nucleotide_string = dataset_filehandle.readlines()[0].rstrip()
    nucleotide_counter = defaultdict(int, Counter(nucleotide_string))
    return nucleotide_counter["A"], nucleotide_counter["C"], nucleotide_counter["G"], nucleotide_counter["T"]

if __name__ == '__main__':
    import sys
    print(*solution_DNA(sys.argv[1]))
