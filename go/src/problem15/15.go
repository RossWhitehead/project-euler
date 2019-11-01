package problem15

func Execute() {
	gridSize := 20
	x := gridSize
	y := gridSize
	pathCount := 0

	pathCount = traverse(x, y)

	println("Path count:", pathCount)
}

func traverse(x int, y int) {
	if x == 1 || y == 1 {
		return 1
	}
	return traverse(x--, y) + traverse(x, y--)
}
