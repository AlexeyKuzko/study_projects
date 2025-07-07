package solution

type Voicer interface {
	Voice() string
}

type Cat struct {
	// …
}

type Cow struct {
	// …
}

type Dog struct {
	// …
}

// BEGIN (write your solution here)
func (c Cat) Voice() string {
	return "Мяу"
}
func (c Cow) Voice() string {
	return "Мууу"
}
func (d Dog) Voice() string {
	return "Гав"
}

// END
