def read_input(filepath):
    population_descriptions = []
    with open(filepath) as filehandle:
        for line in filehandle:
            k, m, n = [int(x) for x in line.split()]
            population_descriptions.append((k, m, n))
    return population_descriptions

def solution_IPRB(k,m,n):
    total = k + m + n
    # prob we pick two homo recessive
    Pnn = n/total * (n-1)/(total-1)
    # prob we pick one homo recessive and one heterozygous, order of picking matters
    Pmn = m/total * n/(total-1)
    Pnm = n/total * m/(total-1)
    # prob we pick two heterozygous
    Pmm = m/total * (m-1)/(total-1)

    # adjust for allele combining
    # all offspring of Pnn do not have a dominant allele
    # half of Pmn and Pnm do not have a dominant allele
    # a quarter of Pmm do not have a dominant allele
    prob_no_dominant = Pnn + Pnm * .5 + Pmn * .5 + Pmm * .25
    return 1 - prob_no_dominant

if __name__ == '__main__':
    import sys
    population_descriptions = read_input(sys.argv[1])
    for population_description in population_descriptions:
        print(solution_IPRB(*population_description))