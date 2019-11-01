package problem14

import "testing"

func TestExecute(t *testing.T) {
	tests := []struct {
		name string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			Execute()
		})
	}
}

func Test_getNext(t *testing.T) {
	type args struct {
		current int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getNext(tt.args.current); got != tt.want {
				t.Errorf("getNext() = %v, want %v", got, tt.want)
			}
		})
	}
}
