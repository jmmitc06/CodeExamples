package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func solution_FIB(num_generations int64, num_offspring int64) int64 {
	if num_generations == 0 {
		return 0
	} else if num_generations == 1 {
		return 1
	} else {
		num_pairs_last_gen := solution_FIB(num_generations-1, num_offspring)
		num_pairs_this_gen := num_offspring * solution_FIB(num_generations-2, num_offspring)
		return num_pairs_last_gen + num_pairs_this_gen
	}
}

func readlines(filepath string) (int64, int64) {
	content, _ := ioutil.ReadFile(filepath)
	var num_generations, num_offspring int64
	fmt.Sscanf(string(content), "%d %d", &num_generations, &num_offspring)
	return num_generations, num_offspring
}

func main() {
	num_generations, num_offspring := readlines(os.Args[1])
	fmt.Println(solution_FIB(num_generations, num_offspring))
}
