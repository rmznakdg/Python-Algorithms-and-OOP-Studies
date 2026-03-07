class Student:
    def __init__(self, name: str, grades: list[int]):
        self.name = name
        self.grades = list(grades)

    def add_grade(self, added_grades: list[int]):
        for g in added_grades:
            if not isinstance(g, int):
                raise ValueError("Notlar tam sayı olmalıdır.")
            if g < 0 or g > 100:
                raise ValueError("Notlar 0 ile 100 arasında olmalıdır.")
        self.grades.extend(added_grades)

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def is_passing(self, threshold: float = 50.0) -> bool:
        return self.average() >= threshold

    def __str__(self):
        return f"{self.name} - Ortalama: {self.average():.2f}"
