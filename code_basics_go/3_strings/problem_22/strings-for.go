package solution

// shiftASCII принимает строку s и число step, и возвращает новую строку,
// где каждый символ сдвинут вперед на число step
func shiftASCII(s string, step int) string {
	result := make([]byte, len(s))
	for i, char := range s {
		// Применяем сдвиг и берем по модулю 256
		shiftedChar := (int(char) + step) % 256
		// Если результат отрицательный, добавляем 256 чтобы остаться в диапазоне ASCII
		if shiftedChar < 0 {
			shiftedChar += 256
		}
		result[i] = byte(shiftedChar)
	}
	return string(result)
}
