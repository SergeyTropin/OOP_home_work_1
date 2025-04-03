# Код из квиза
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def __str__(self):
        
        print(f' Student \n Name: {self.name} \n Surname: {self.surname}')
        dict_of_grades = self.grades
        mean_grade = calc_mean_grade(dict_of_grades)
        print(f' Mean_grade_for_home_works: {mean_grade}')
        print(f'Courses in progress: {self.courses_in_progress}')
        print(f'Finished_courses: {self.finished_courses}')
        print('')
     
    def __lt__(self, other):

        if isinstance(other, Student): 
            self_mean_grade = calc_mean_grade(self.grades)
            other_mean_grade = calc_mean_grade(other.grades)
            return self_mean_grade < other_mean_grade
        else:
            print('Ошибка сравнения экземпляров (студенты)')
            return None
    
    def __eq__(self, other):

        if isinstance(other, Student): 
            self_mean_grade = calc_mean_grade(self.grades)
            other_mean_grade = calc_mean_grade(other.grades)
            return self_mean_grade == other_mean_grade
        else:
            print('Ошибка сравнения экземпляров (студенты)')
            return None


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    

    def __str__(self):
        print(f' Lector \n Name: {self.name} \n Surname: {self.surname}')
        dict_of_grades = self.grades
        mean_grade = calc_mean_grade(dict_of_grades)
        print(f' Mean_grade_for_lectures: {mean_grade}')
        print('')
              
    def __lt__(self, other):

        if isinstance(other, Lector): 
            self_mean_grade = calc_mean_grade(self.grades)
            other_mean_grade = calc_mean_grade(other.grades)
            return self_mean_grade < other_mean_grade
        else:
            print('Ошибка сравнения экземпляров (лекторы)')
            return None
    
    def __eq__(self, other):

        if isinstance(other, Lector): 
            self_mean_grade = calc_mean_grade(self.grades)
            other_mean_grade = calc_mean_grade(other.grades)
            return self_mean_grade == other_mean_grade
        else:
            print('Ошибка сравнения экземпляров (лекторы)')
            return None
        
    # Выставлять оценки студентам может только эксперт
    def rate_lectures(self, student, course, grade):

        if isinstance(int(grade), int): 
            grade_int = int(grade)
        else:
            print('Оценка должна быть целым числом от 1 до 10')
            return None
        
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
            print('Ошибка в методе Lector.rate_lectures()')
            return None  

class Expert(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        print(f' Expert \n Name: {self.name} \n Surname: {self.surname}')
        print('')
    
    # Выставлять оценки студентам может только эксперт
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка в методе Expert.rate_hw()')
            return None


def calc_mean_grade(dict_grades):
    """ Function for calculating mean value of all grades in dict

    Args:
        dict_grades (dict): dict with many keys, values of keys: type(int)

    Returns:
        mean_value of all values in dict
    """

    sum_grade = 0
    num_grade = 0
        
    for key in dict_grades.keys():

        values = dict_grades.get(key)
        sum_grade +=sum(values)
        num_grade +=len(values)

    if num_grade >0:
        return sum_grade/num_grade
    else:
        print('Не выставлено ни одной оценки')
        return None   
       
def are_students_equal(student1, student2):

    if isinstance(student1, Student) and isinstance(student2, Student):
        return student1 == student2
    else:
        print('В аргументах нужно передать экземпляры класса Student')
    
def is_first_student_worse(student1, student2):

    if isinstance(student1, Student) and isinstance(student2, Student):
        return student1 < student2
    else:
        print('В аргументах нужно передать экземпляры класса Student')

# Студенты
first_student = Student('Berty', 'Fox', 'm')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress +=['Math']

second_student = Student('Breatny', 'Spearce', 'w')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress +=['C++']

# Лекторы и эксперты
hot_lector = Lector('Martin', 'McFly')
hot_lector.courses_attached += ['Python']
hot_lector.courses_attached += ['C++']
hot_lector.courses_attached += ['Math']

cool_expert = Expert('Doctor', 'Vatson')
cool_expert.courses_attached += ['Python']
cool_expert.courses_attached += ['C++']
cool_expert.courses_attached += ['Math']

# Выставление оценок студентам
cool_expert.rate_hw(first_student, 'Python', 10)
cool_expert.rate_hw(first_student, 'Python', 8)
cool_expert.rate_hw(first_student, 'Math', 6)

cool_expert.rate_hw(second_student, 'Python', 9)
cool_expert.rate_hw(second_student, 'Python', 8)
cool_expert.rate_hw(second_student, 'C++', 7)


print(f'First student:  {first_student.grades}')
print(f'Second_student: {second_student.grades}')

# Выставление оценок преподавателям

hot_lector.rate_lectures(first_student, 'Python', 8)
hot_lector.rate_lectures(first_student, 'Python', 8)
hot_lector.rate_lectures(first_student, 'Math', 9)
hot_lector.rate_lectures(first_student, 'Python', 5)
hot_lector.rate_lectures(first_student, 'Math', 5)
# средняя оценка 35/5 = 7

hot_lector.rate_lectures(second_student, 'C++', 5)
hot_lector.rate_lectures(second_student, 'C++', 7)
hot_lector.rate_lectures(second_student, 'C++', 3)
hot_lector.rate_lectures(second_student, 'Python', 9)
hot_lector.rate_lectures(second_student, 'Python', 6)

# средняя оценка 30/5 = 6
# общая средняя 65/10 = 6.5

print(f'Lector_courses: {hot_lector.courses_attached}')
print(f'Lector_grades: {hot_lector.grades}')
print('')
hot_lector.__str__()

print(f'Student {first_student.name} {first_student.surname}\
      is_studying_worse_than {second_student.name} {second_student.surname} \
         result_is:  {is_first_student_worse(first_student, second_student)}') 
print(f'Student {first_student.name} {first_student.surname}\
      is_equal_in_studying_with {second_student.name} {second_student.surname} \
         result_is:  {are_students_equal(first_student, second_student)}') 

print(f'Grades of first_student: {first_student.grades} \n \
      mean_grade: {calc_mean_grade(first_student.grades)}')
print(f'Grades of second_student: {second_student.grades} \n \
      mean_grade: {calc_mean_grade(second_student.grades)}')