const repoUrl = "https://github.com/AlexeyKuzko/study_projects";

const courses = [
  {
    title: "Yandex Praktikum: Automation QA Engineer",
    provider: "Yandex Praktikum",
    category: "qa",
    status: "Завершено",
    path: "ya_praktikum_aqa_projects",
    summary:
      "Основной QA-трек: Python, unit-тесты, Selenium UI, Page Object, API-тестирование и три дипломных проекта.",
    stats: [
      ["8", "спринтов"],
      ["81", "файл кода"],
      ["38", "тестовых модулей"],
    ],
    tags: ["pytest", "Selenium", "Page Object", "API", "Allure", "Stellar Burgers"],
    modules: [
      "Sprint 1-3: основы Python и ООП",
      "Sprint 4: unit-тесты существующего приложения",
      "Sprint 5-6: UI-тесты и Page Object",
      "Sprint 7: API-тесты курьеров и заказов",
      "Diploma 1-3: unit, API и UI-проекты",
    ],
    source: `${repoUrl}/tree/main/ya_praktikum_aqa_projects`,
    extra: "https://practicum.yandex.ru/qa-automation-engineer-python/",
  },
  {
    title: "Stepik: Algorithms and Data Structures",
    provider: "Stepik",
    category: "algorithms",
    status: "В работе",
    path: "stepik/algorithms_data_structures",
    summary:
      "Алгоритмическая практика на Python: от моделей вычислений до графов, обходов и динамического программирования.",
    stats: [
      ["8", "разделов"],
      ["125", "решений"],
      ["Python", "язык"],
    ],
    tags: ["структуры данных", "сортировки", "поиск", "динамика", "графы", "BFS/DFS"],
    modules: [
      "Algorithms and Computing Models",
      "Basic Data Structures",
      "Sorting and Advanced Sorting",
      "Search Algorithms",
      "Dynamics Basics",
      "Graphs and Graph Algorithms",
    ],
    source: `${repoUrl}/tree/main/stepik/algorithms_data_structures`,
    extra: "https://stepik.org/course/181477",
  },
  {
    title: "Stepik: Generation Python",
    provider: "Stepik",
    category: "python",
    status: "В работе",
    path: "stepik/generation_py",
    summary:
      "Решения из продвинутого и профессионального треков Generation Python, собранные по темам и уровням сложности.",
    stats: [
      ["2", "трека"],
      ["100", "файлов"],
      ["Python", "язык"],
    ],
    tags: ["advanced Python", "professional Python", "чистый код", "практика"],
    modules: [
      "Generation Python: Advanced",
      "Generation Python: Professional",
      "Задачи на углубленные возможности языка",
    ],
    source: `${repoUrl}/tree/main/stepik/generation_py`,
    extra: "https://stepik.org/",
  },
  {
    title: "Yandex Academy: Python Handbook",
    provider: "Yandex Academy",
    category: "python",
    status: "В работе",
    path: "ya_academy_contest_problems",
    summary:
      "Contest-решения по разделам хендбука: основы, коллекции, функции, ООП, анализ данных и DevOps-задачи.",
    stats: [
      ["6", "секций"],
      ["205", "решений"],
      ["Contest", "формат"],
    ],
    tags: ["Python basics", "collections", "functions", "OOP", "pandas", "NumPy"],
    modules: [
      "Python basics",
      "Collections and memory management",
      "Functions",
      "Object-Oriented Programming",
      "Libraries for data collecting and processing",
      "DevOps contest",
    ],
    source: `${repoUrl}/tree/main/ya_academy_contest_problems`,
    extra: "https://education.yandex.ru/handbook/python",
  },
  {
    title: "Specialist: Python Level 2 OOP",
    provider: "Specialist",
    category: "python",
    status: "Завершено",
    path: "specialist",
    summary:
      "Практика объектно-ориентированного Python по дням обучения: примеры, домашние задания и решения.",
    stats: [
      ["5", "дней"],
      ["36", "практик"],
      ["OOP", "фокус"],
    ],
    tags: ["классы", "наследование", "магические методы", "исключения", "практика"],
    modules: [
      "Day 1-2: основы ООП и домашние задания",
      "Day 3-5: решения, практика и примеры",
      "Course extras: материалы и примеры преподавателя",
    ],
    source: `${repoUrl}/tree/main/specialist`,
    extra: "https://www.specialist.ru/course/python2",
  },
  {
    title: "Starting Out with Python",
    provider: "Tony Gaddis book",
    category: "python",
    status: "В работе",
    path: "sow_python_problems",
    summary:
      "Задачи по книге Starting Out with Python: сейчас заполнены разделы по вводу-выводу и ООП, остальные главы заведены как структура.",
    stats: [
      ["14", "глав"],
      ["28", "задач"],
      ["Python", "язык"],
    ],
    tags: ["input/output", "boolean logic", "OOP", "recursion", "files"],
    modules: [
      "Input, Processing, and Output",
      "Classes and Object-Oriented Programming",
      "Заготовки для функций, файлов, строк, коллекций, рекурсии и GUI",
    ],
    source: `${repoUrl}/tree/main/sow_python_problems`,
    extra: "https://www.pearson.com/en-us/subject-catalog/p/starting-out-with-python/P200000003356/9780136912330",
  },
  {
    title: "Code Basics: Python",
    provider: "Code Basics",
    category: "python",
    status: "Завершено",
    path: "code_basics/python",
    summary:
      "Компактный файл с решениями базового курса Python: от первых выражений до циклов, условий и функций.",
    stats: [
      ["72", "блока"],
      ["1", "модуль"],
      ["Python", "язык"],
    ],
    tags: ["syntax", "strings", "variables", "functions", "logic", "loops"],
    modules: [
      "Python basics and arithmetic",
      "Strings, variables and data types",
      "Function calls and definitions",
      "Logic, conditionals and loops",
    ],
    source: `${repoUrl}/tree/main/code_basics/python`,
    extra: "https://code-basics.com/languages/python",
  },
  {
    title: "Code Basics: Go",
    provider: "Code Basics",
    category: "go",
    status: "Завершено",
    path: "code_basics/golang",
    summary:
      "Практика по Go: основы языка, коллекции, строки, функции, методы и первые задачи на конкурентность.",
    stats: [
      ["5", "модулей"],
      ["35", "решений"],
      ["Go", "язык"],
    ],
    tags: ["Go", "collections", "strings", "methods", "interfaces", "concurrency"],
    modules: [
      "Foundations",
      "Collections",
      "Strings",
      "Functions and Methods",
      "Concurrency",
    ],
    source: `${repoUrl}/tree/main/code_basics/golang`,
    extra: "https://code-basics.com/languages/go",
  },
];

const courseGrid = document.querySelector("#courseGrid");
const searchInput = document.querySelector("#searchInput");
const filters = Array.from(document.querySelectorAll(".filter"));
const resultCount = document.querySelector("#resultCount");

let activeFilter = "all";

function normalize(value) {
  return value.toLowerCase().trim();
}

function courseMatches(course, query) {
  if (!query) {
    return true;
  }

  const haystack = [
    course.title,
    course.provider,
    course.path,
    course.summary,
    course.category,
    course.status,
    ...course.tags,
    ...course.modules,
  ]
    .join(" ")
    .toLowerCase();

  return haystack.includes(query);
}

function courseTemplate(course) {
  const statusClass = course.status === "В работе" ? " is-progress" : "";

  return `
    <article class="course-card" data-category="${course.category}">
      <div class="course-top">
        <span class="course-provider">${course.provider}</span>
        <span class="course-status${statusClass}">${course.status}</span>
      </div>
      <div>
        <h3>${course.title}</h3>
        <p>${course.summary}</p>
      </div>
      <div class="course-stats" aria-label="Показатели ${course.title}">
        ${course.stats
          .map(
            ([value, label]) => `
              <div class="course-stat">
                <strong>${value}</strong>
                <span>${label}</span>
              </div>
            `,
          )
          .join("")}
      </div>
      <div class="tag-list" aria-label="Темы">
        ${course.tags.map((tag) => `<span class="tag">${tag}</span>`).join("")}
      </div>
      <ul class="module-list">
        ${course.modules.map((module) => `<li>${module}</li>`).join("")}
      </ul>
      <div class="course-links">
        <a class="course-link" href="${course.source}">Открыть папку</a>
        <a class="course-link secondary" href="${course.extra}">Источник курса</a>
      </div>
    </article>
  `;
}

function renderCourses() {
  const query = normalize(searchInput.value);
  const visibleCourses = courses.filter((course) => {
    const byFilter = activeFilter === "all" || course.category === activeFilter;
    return byFilter && courseMatches(course, query);
  });

  courseGrid.innerHTML = visibleCourses.map(courseTemplate).join("");
  resultCount.textContent = `Показано: ${visibleCourses.length} из ${courses.length}`;
}

filters.forEach((button) => {
  button.addEventListener("click", () => {
    activeFilter = button.dataset.filter;
    filters.forEach((item) => item.classList.toggle("is-active", item === button));
    renderCourses();
  });
});

searchInput.addEventListener("input", renderCourses);

renderCourses();
