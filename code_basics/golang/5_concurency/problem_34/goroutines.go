package solution

import (
	"sync"
	"time"
)

// MaxSum принимает два слайса целых чисел и возвращает слайс с наибольшей суммой
func MaxSum(nums1, nums2 []int) []int {
	var sum1, sum2 int
	var wg sync.WaitGroup

	// Функция для вычисления суммы
	calculateSum := func(nums []int, result *int) {
		defer wg.Done()
		time.Sleep(100 * time.Millisecond) // Симуляция времени вычисления
		for _, num := range nums {
			*result += num
		}
	}

	// Запускаем горутины для расчета каждой суммы
	wg.Add(2)
	go calculateSum(nums1, &sum1)
	go calculateSum(nums2, &sum2)

	wg.Wait() // Ждем завершения всех горутин

	// Сравниваем суммы и возвращаем соответствующий слайс
	if sum1 >= sum2 {
		return nums1
	}
	return nums2
}
