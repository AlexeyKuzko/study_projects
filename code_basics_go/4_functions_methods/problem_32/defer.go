package solution

import "errors"

// MergeDictsJob is a job to merge dictionaries into a single dictionary.
type MergeDictsJob struct {
	Dicts      []map[string]string
	Merged     map[string]string
	IsFinished bool
}

// errors
var (
	errNotEnoughDicts = errors.New("at least 2 dictionaries are required")
	errNilDict        = errors.New("nil dictionary")
)

// ExecuteMergeDictsJob merges dictionaries and returns the job and error if any.
func ExecuteMergeDictsJob(job *MergeDictsJob) (*MergeDictsJob, error) {
	// Используем defer для установки IsFinished в true в любом случае
	defer func() {
		job.IsFinished = true
	}()

	// Проверка, что словарей не меньше двух
	if len(job.Dicts) < 2 {
		return job, errNotEnoughDicts
	}

	// Инициализируем результирующую мапу, если она еще не инициализирована
	if job.Merged == nil {
		job.Merged = make(map[string]string)
	}

	// Перебор каждого словаря
	for _, dict := range job.Dicts {
		// Проверка на nil
		if dict == nil {
			return job, errNilDict
		}

		// Объединение словарей
		for key, value := range dict {
			job.Merged[key] = value
		}
	}

	// Возвращаем успешное завершение
	return job, nil
}
