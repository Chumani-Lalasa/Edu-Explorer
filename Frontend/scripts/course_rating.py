class CourseRating:
    def __init__(self, course_name):
        self.course_name = course_name
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0

# Sample Usage
course = CourseRating("Python Programming")
course.add_rating(5)
course.add_rating(4)
print(f"Average rating for {course.course_name}: {course.average_rating()}")
