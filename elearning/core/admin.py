from django.contrib import admin
from django.contrib import admin
from .models import UserProfile, Course, Module, Content, Lesson, Quiz, Question, CourseProgress, QuizProgress, QuestionAnswer, Certificate, Answer

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Content)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(CourseProgress)
admin.site.register(QuizProgress)
admin.site.register(QuestionAnswer)
admin.site.register(Certificate)
admin.site.register(Answer)

