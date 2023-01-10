import functools

def read_input(filepath):
    gen_offspring_pairs = []
    with open(filepath) as filehandle:
        for line in filehandle:
            num_generations, num_offspring = line.split()
            gen_offspring_pairs.append((int(num_generations), int(num_offspring)))
    return gen_offspring_pairs

#this decorator will make this solution equivalent to the dynamic programming solution
@functools.cache
def solution_FIB(num_generations, num_offspring, num_starting_pairs=1):
    if num_generations == 0:
        return 0
    elif num_generations == 1:
        return num_starting_pairs
    else:
        num_pairs_last_gen = solution_FIB(num_generations - 1, num_offspring)
        new_pairs_this_gen = num_offspring * solution_FIB(num_generations - 2, num_offspring)
        return num_pairs_last_gen + new_pairs_this_gen

if __name__ == '__main__':
    import sys
    for num_generations, num_offspring in read_input(sys.argv[1]):
        print(solution_FIB(num_generations, num_offspring))



