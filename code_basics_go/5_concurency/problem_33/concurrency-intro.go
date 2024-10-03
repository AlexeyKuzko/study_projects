package solution

// MaxSum принимает два слайса целых чисел и возвращает слайс с наибольшей суммой
func MaxSum(nums1, nums2 []int) []int {
	sum1, sum2 := 0, 0

	// Вычисляем сумму первого слайса
	for _, num := range nums1 {
		sum1 += num
	}

	// Вычисляем сумму второго слайса
	for _, num := range nums2 {
		sum2 += num
	}

	// Сравниваем суммы и возвращаем соответствующий слайс
	if sum1 >= sum2 {
		return nums1
	}
	return nums2
}
