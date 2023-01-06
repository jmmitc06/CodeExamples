def solution_RNA(dataset_path):
    with open(dataset_path) as dataset_filehandle:
        nucleotide_string = str(dataset_filehandle.readlines()[0].rstrip())
    return nucleotide_string.replace("T", "U")

if __name__ == '__main__':
    import sys
    print(solution_RNA(sys.argv[1]))