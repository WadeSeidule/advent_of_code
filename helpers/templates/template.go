package main

import (
	"os"
	"fmt"
	"bufio"
)

func readInput(filename string) []string {
	wd, _ := os.Getwd()
	file, err := os.Open(fmt.Sprintf("%s/%s", wd, filename))
	if err != nil {
        panic(err)
    }

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}

func main(){
	lines := readInput("input.txt")
}

