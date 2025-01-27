class Dashboard:
    def __init__(self, courses):
        self.courses = courses
        self.enrolled_students_data = {
            "Python": ["John", "Jane", "Doe", "Alice"],
            "Data Structures": ["Mike", "Sophia", "Tom"],
            "Machine Learning": ["Charlie", "Eve", "Nina", "Steve"]
        }

    def display_statistics(self):
        print("Course Statistics")
        print(f"Total Courses: {len(self.courses)}")
        for course in self.courses:
            enrolled_students = self.get_enrolled_students(course)
            print(f"Course: {course} - Enrolled Students: {len(enrolled_students)}")
            self.display_student_list(course, enrolled_students)

    def get_enrolled_students(self, course):
        return self.enrolled_students_data.get(course, [])

    def display_student_list(self, course, enrolled_students):
        print(f"Students enrolled in {course}:")
        for student in enrolled_students:
            print(f"- {student}")

# Sample Usage
dashboard = Dashboard(["Python", "Data Structures", "Machine Learning"])
dashboard.display_statistics()
