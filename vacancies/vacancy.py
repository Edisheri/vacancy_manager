class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self):
        return f"Vacancy(title={self.title}, link={self.link}, salary={self.salary}, description={self.description})"

    def __eq__(self, other):
        # Сравниваем вакансии по зарплате
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return NotImplemented

    def __lt__(self, other):
        # Сортировка вакансий по зарплате (от меньшей к большей)
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return NotImplemented
