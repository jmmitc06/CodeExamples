package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func readlines(filepath string) []byte {
	content, _ := ioutil.ReadFile(filepath)
	return content
}

func solution_DNA(dna []byte, output_order string) []int {
	counter := make(map[byte]int)
	for _, nucleotide := range dna {
		counter[nucleotide] += 1
	}
	byte_output_order := []byte(output_order)
	result := make([]int, len(byte_output_order))
	for index, nucleotide := range byte_output_order {
		result[index] = counter[nucleotide]
	}
	return result
}

func main() {
	dna := readlines(os.Args[1])
	output_order := "ACGT"
	solution := solution_DNA(dna, output_order)
	fmt.Println(strings.Trim(fmt.Sprint(solution), "[]"))

}
