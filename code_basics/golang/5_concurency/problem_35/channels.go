package solution

import (
	"fmt"
)

func main() {
	numsCh := make(chan []int)
	sumCh := make(chan int)

	go SumWorker(numsCh, sumCh)

	numsCh <- []int{10, 10, 10}

	res := <-sumCh   // получаем результат
	fmt.Println(res) // выводит 30
}

// SumWorker суммирует числа из канала numsCh и передает результат в sumCh
func SumWorker(numsCh chan []int, sumCh chan int) {
	for nums := range numsCh {
		sum := 0
		for _, n := range nums {
			sum += n
		}
		sumCh <- sum // отправляем результат в канал sumCh
	}
}
