package solution

// BEGIN (write your solution here)
func DomainForLocale(domain, locale string) string {
	if domain == "" {
		panic("domain is empty")
	}
	if locale == "" {
		return "en." + domain
	}
	return locale + "." + domain
}

// END
