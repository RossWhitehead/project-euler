package problem14

import "fmt"

const visitedLength int = 1000001 // Add one to make poitions easier to work with
var visited [visitedLength]bool

func ExecuteOptimized() {
	starter := 2
	next := starter
	steps := 0
	leader := 0
	maxSteps := 0

	visited[starter] = true
	visited[starter-1] = true

	for {
		next = getNext(next)
		fmt.Println(next)
		visited[next] = true
		steps++
		if next == 1 {
			if steps > maxSteps {
				maxSteps = steps
				leader = starter
			}
			starter = getStarter(starter)
		}

		fmt.Println(starter)

		if starter == 1000000 {
			break
		}
	}

	fmt.Println(leader)
}

func getNext(current int) int {
	if current%2 == 0 {
		return current / 2
	} else {
		return 3*current + 1
	}
}

func getStarter(lastStarter int) int {
	i := lastStarter
	for i <= visitedLength {
		if visited[i] == false {
			return i
		}
	}
	return i
}
