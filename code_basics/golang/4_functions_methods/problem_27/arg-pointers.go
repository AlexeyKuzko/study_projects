package solution

type Parent struct {
	Name     string
	Children []Child
}

type Child struct {
	Name string
	Age  int
}

func CopyParent(p *Parent) Parent {
	if p == nil {
		return Parent{}
	}

	cp := Parent{
		Name: p.Name,
	}

	cp.Children = make([]Child, len(p.Children))
	copy(cp.Children, p.Children)

	return cp
}
