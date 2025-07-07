package solution

type Counter struct {
	Value int
}

func (c *Counter) Inc(delta int) {
	if delta == 0 {
		delta = 1
	}
	c.Value += delta
}

func (c *Counter) Dec(delta int) {
	if delta == 0 {
		delta = 1
	}
	c.Value = Max(0, c.Value-delta)
}

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

// Пример использования
// c := Counter{}
// c.Inc(0)
// c.Inc(0)
// c.Inc(40)
// fmt.Println(c.Value) // 42
//
// c.Dec(0)
// c.Dec(30)
// fmt.Println(c.Value) // 11
//
// c.Dec(100)
// fmt.Println(c.Value) // 0
