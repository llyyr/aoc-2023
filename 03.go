package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
)

type coordinates struct {
    r, c int
}

type set map[coordinates]struct{}

func get_adjacents(r, c, R, C int) set {
    out := make(set)
    for _, n := range []coordinates{{r - 1, c - 1}, {r, c - 1}, {r + 1, c - 1},
                                    {r - 1, c}, {r + 1, c},
                                    {r - 1, c + 1}, {r, c + 1}, {r + 1, c + 1}} {
        if n.r >= 0 && n.r < R && n.c >= 0 && n.c < C {
            out[n] = struct{}{}
        }
    }
    return out
}

func solve(G []string, R, C int) (int, int) {
    d := make(map[coordinates][]int)
    p1 := 0

    for r := 0; r < R; r++ {
        c := 0
        for c < C {
            if !is_digit(G[r][c]) {
                c++
                continue
            }

            adjacents := get_adjacents(r, c, R, C)
            num := string(G[r][c])
            for cc := c + 1; cc < C; cc++ {
                if !is_digit(G[r][cc]) {
                    break
                }
                num += string(G[r][cc])
                for k := range get_adjacents(r, cc, R, C) {
                    adjacents[k] = struct{}{}
                }
                c++
            }

            for n := range adjacents {
                if G[n.r][n.c] == '*' {
                    d[n] = append(d[n], Atoi(num))
                }
            }

            if is_symbol(G, adjacents) {
                p1 += Atoi(num)
            }
            c++
        }
    }

    p2 := 0
	for _, nums := range d {
		if len(nums) == 2 {
			p2 += nums[0] * nums[1]
		}
	}

    return p1, p2
}

func main() {
    file, _ := os.Open("03.txt")
    defer file.Close()

    var G []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        G = append(G, scanner.Text())
    }

    R, C := len(G), len(G[0])
    result1, result2 := solve(G, R, C)
    fmt.Println(result1, result2)
}

func is_digit(c byte) bool {
    return c >= '0' && c <= '9'
}

func Atoi(s string) int {
    num, _ := strconv.Atoi(s)
    return num
}

func is_symbol(G []string, coords set) bool {
    for n := range coords {
        if !is_digit(G[n.r][n.c]) && G[n.r][n.c] != '.' {
            return true
        }
    }
    return false
}
