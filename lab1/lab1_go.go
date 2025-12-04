package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)


func readCoefficient(name string, cliValue string, hasCli bool, reader *bufio.Reader) float64 {
    usedCli := false
    for {
        var text string
        if hasCli && !usedCli {
            text = cliValue
            usedCli = true
        } else {
            fmt.Printf("Введите коэффициент %s: ", name)
            line, _ := reader.ReadString('\n')
            text = line
        }
        text = strings.TrimSpace(text)
        value, err := strconv.ParseFloat(text, 64)
        if err == nil {
            return value
        }
        fmt.Printf("Ошибка: коэффициент %s должен быть действительным числом.\n", name)
    }
}


func solveBiquadratic(a, b, c float64) ([]float64, bool) {
    if a == 0 && b == 0 && c == 0 {
        return nil, true
    }

    if a == 0 {
        if b == 0 {
            return []float64{}, false
        }
        t := -c / b
        if t < 0 {
            return []float64{}, false
        }
        if t == 0 {
            return []float64{0.0}, false
        }
        r := math.Sqrt(t)
        return []float64{-r, r}, false
    }

    D := b*b - 4*a*c
    roots := []float64{}
    if D < 0 {
        return roots, false
    } else if D == 0 {
        t := -b / (2 * a)
        if t > 0 {
            r := math.Sqrt(t)
            roots = append(roots, -r, r)
        } else if t == 0 {
            roots = append(roots, 0.0)
        }
    } else {
        sqrtD := math.Sqrt(D)
        t1 := (-b + sqrtD) / (2 * a)
        t2 := (-b - sqrtD) / (2 * a)

        for _, t := range []float64{t1, t2} {
            if t > 0 {
                r := math.Sqrt(t)
                roots = append(roots, -r, r)
            } else if t == 0 {
                roots = append(roots, 0.0)
            }
        }
    }

    unique := []float64{}             
    seen := map[float64]bool{}     

    for _, x := range roots {
        if !seen[x] {
            seen[x] = true
            unique = append(unique, x)
        }
    }

    sort.Float64s(unique)
    return unique, false
}


func main() {
    args := os.Args[1:]
    var cliA, cliB, cliC string
    hasA, hasB, hasC := false, false, false

    if len(args) > 0 {
        cliA = args[0]
        hasA = true
    }
    if len(args) > 1 {
        cliB = args[1]
        hasB = true
    }
    if len(args) > 2 {
        cliC = args[2]
        hasC = true
    }

    reader := bufio.NewReader(os.Stdin)

    A := readCoefficient("A", cliA, hasA, reader)
    B := readCoefficient("B", cliB, hasB, reader)
    C := readCoefficient("C", cliC, hasC, reader)

    fmt.Printf("Решаем уравнение: %.6f * x^4 + %.6f * x^2 + %.6f = 0\n", A, B, C)

    if A != 0 {
        D := B*B - 4*A*C
        fmt.Printf("Дискриминант относительно t = x^2: D = %.6f\n", D)
    } else {
        fmt.Println("Коэффициент A = 0, решаем упрощённое уравнение (дискриминант не вычисляется).")
    }

    roots, infinite := solveBiquadratic(A, B, C)

    if infinite {
        fmt.Println("Уравнение тождественно 0 = 0, бесконечно много решений.")
        return
    }

    if len(roots) == 0 {
        fmt.Println("Действительных корней нет.")
    } else {
        fmt.Println("Действительные корни уравнения:")
        for i, x := range roots {
            fmt.Printf("x%d = %.6f\n", i+1, x)
        }
    }
}
