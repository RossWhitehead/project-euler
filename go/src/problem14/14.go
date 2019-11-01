package problem14

import "fmt"

func Execute() {
	maxSteps := 0
	leader := 1
	var next int
	var steps int

	for i := 2; i <= 1000000; i++ {
		next = i
		steps = 0
		for {
			next = getNext(next)
			steps++
			if next == 1 {
				break
			}
		}

		if steps > maxSteps {
			maxSteps = steps
			leader = i
		}
	}

	fmt.Println("Leader:", leader)
	fmt.Println("Steps:", maxSteps)
}

func getNext(current int) int {
	if current%2 == 0 {
		return current / 2
	}
	return 3*current + 1
}
