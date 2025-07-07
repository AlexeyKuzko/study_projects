package solution

// Person is a struct that keeps info about person's age
type Person struct {
	Age uint8
}

// PersonList is a slice of Person structs
type PersonList []Person

// GetAgePopularity returns a map where the key is the age and the value is the count of people with that age
func (pl PersonList) GetAgePopularity() map[uint8]int {
	agePopularity := make(map[uint8]int)
	for _, person := range pl {
		agePopularity[person.Age]++
	}
	return agePopularity
}

// Example usage
/*
pl := PersonList{
  {Age: 18},
  {Age: 44},
  {Age: 18},
}

fmt.Println(pl.GetAgePopularity()) // map[18:2 44:1]
*/
