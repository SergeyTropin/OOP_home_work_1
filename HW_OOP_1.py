# Код из квиза
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Задание № 1. Наследование

class Lector(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    # Выставлять оценки студентам может только эксперт
    def rate_lectures(self, student, course, grade):

        if isinstance(int(grade), int): 
            grade_int = int(grade)
        else:
            return 'Оценка должна быть целым числом от 1 до 10'
        
        grades_list = [x+1 for x in range(10)] 

        if isinstance(student, Student) and \
            course in self.courses_attached and \
                course in student.courses_in_progress and \
                    grade_int in grades_list:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'  

class Expert(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    # Выставлять оценки студентам может только эксперт
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
# Задание № 2. Атрибуты и классы взаимодействия.

    
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_expert = Expert('Some', 'Buddy')
cool_expert.courses_attached += ['Python']
 
cool_expert.rate_hw(best_student, 'Python', 10)
cool_expert.rate_hw(best_student, 'Python', 10)
cool_expert.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)
print(cool_expert.courses_attached)

hot_lector = Lector('Martin', 'McFly')
hot_lector.courses_attached += ['Python']
hot_lector.rate_lectures(best_student, 'Python', 8)

print(hot_lector.courses_attached)
print(hot_lector.grades)
