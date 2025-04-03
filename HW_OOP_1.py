
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
            print('Mistake in comparison (students)')
            return None
    
    def __eq__(self, other):

        if isinstance(other, Student): 
            self_mean_grade = calc_mean_grade(self.grades)
            other_mean_grade = calc_mean_grade(other.grades)
            return self_mean_grade == other_mean_grade
        else:
            print('Mistake in comparison (students)')
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
            print('Mistake in comparison (lectors)')
            return None
    
    def __eq__(self, other):

        if isinstance(other, Lector): 
            self_mean_grade = calc_mean_grade(self.grades)
            other_mean_grade = calc_mean_grade(other.grades)
            return self_mean_grade == other_mean_grade
        else:
            print('Mistake in comparison (lectors)')
            return None
        
    # Выставлять оценки студентам может только эксперт
    def rate_lectures(self, student, course, grade):

        if isinstance(int(grade), int): 
            grade_int = int(grade)
        else:
            print('Grade must be int from 1 to 10')
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
            print('Mistake in method Lector.rate_lectures()')
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
            print('Mistake in method Expert.rate_hw()')
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
        print('No grades got')
        return None   
       
def are_persons_equal(person1, person2):

    if (isinstance(person1, Student) and isinstance(person2, Student)) or \
        (isinstance(person1, Lector) and isinstance(person2, Lector)):
        return person1 == person2
    else:
        print('Args must be both samples of class Student or Lectors')
    
def is_first_person_worse(person1, person2):

    if (isinstance(person1, Student) and isinstance(person2, Student)) or \
        (isinstance(person1, Lector) and isinstance(person2, Lector)):
        return person1 < person2
    else:
        print('Args must be both samples of class Student or Lectors')


def meancourse_grade_stud_lec(course, stud_lec_list):

    """ Функция подсчета средней оценки по курсу 
    для выбранной группы студентов или лекторов
    """

    sum_values = 0
    num_values = 0

    for person in stud_lec_list:
        dict_grades = person.grades
        print(f'{person.name} {person.surname} {course}')
        values = dict_grades.get(course)
        print(f'Degrees {values}')
        print('')
        if values:
            sum_values += sum(values) 
            num_values += len(values)

    if num_values:
        mean_grade = sum_values/ num_values 
        return mean_grade
    else:
        print('Mistake in zero division')
        return None
    

    

# Полевые испытания
# Студенты
first_student = Student('Berty', 'Fox', 'm')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Math']

second_student = Student('Breatny', 'Spearce', 'w')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['C++']

# Выставление оценок студентам
# Лекторы и эксперты
hot_lector = Lector('Martin', 'McFly')
hot_lector.courses_attached += ['Python','C++','Math']

lazy_lector = Lector('Chechirskiy', 'Cat')
lazy_lector.courses_attached += ['Python','C++','Math']

cool_expert = Expert('Doctor', 'Vatson')
cool_expert.courses_attached += ['Python','C++','Math']

ice_expert = Expert('Snow', 'Queen')
ice_expert.courses_attached += ['Python','C++','Math']

print("Students lectures experts initiated")
# Выставление оценок студентам
cool_expert.rate_hw(first_student, 'Python', 10)
cool_expert.rate_hw(first_student, 'Python', 8)
cool_expert.rate_hw(first_student, 'Math', 6)

cool_expert.rate_hw(second_student, 'Python', 7)
cool_expert.rate_hw(second_student, 'Python', 8)
cool_expert.rate_hw(second_student, 'C++', 9)

ice_expert.rate_hw(first_student, 'Python', 4)
ice_expert.rate_hw(first_student, 'Python', 6)
ice_expert.rate_hw(first_student, 'Math', 8)

ice_expert.rate_hw(second_student, 'Python', 5)
ice_expert.rate_hw(second_student, 'Python', 6)
ice_expert.rate_hw(second_student, 'C++', 7)

# Выставление оценок преподавателям

hot_lector.rate_lectures(first_student, 'Python', 8)
hot_lector.rate_lectures(first_student, 'Python', 8)
hot_lector.rate_lectures(first_student, 'Math', 9)

hot_lector.rate_lectures(second_student, 'C++', 3)
hot_lector.rate_lectures(second_student, 'Python', 9)
hot_lector.rate_lectures(second_student, 'Python', 6)

lazy_lector.rate_lectures(first_student, 'Python', 4)
lazy_lector.rate_lectures(first_student, 'Python', 4)
lazy_lector.rate_lectures(first_student, 'Math', 6)

lazy_lector.rate_lectures(second_student, 'C++', 2)
lazy_lector.rate_lectures(second_student, 'Python', 10)
lazy_lector.rate_lectures(second_student, 'Python', 9)

print("Grades initiated \n")

# Сравнение студентов
print('Compare students')

print(f'Student {first_student.name} {first_student.surname}\
      is_studying_worse_than {second_student.name} {second_student.surname} \
         result_is:  {is_first_person_worse(first_student, second_student)}') 
print('')
print(f'Student {first_student.name} {first_student.surname}\
      is_equal_in_studying_with {second_student.name} {second_student.surname} \
         result_is:  {are_persons_equal(first_student, second_student)}') 
print('')

print('Grades of students:')
print(f'Grades of first_student: {first_student.grades} \n \
      mean_grade: {calc_mean_grade(first_student.grades)}')
print(f'Grades of second_student: {second_student.grades} \n \
      mean_grade: {calc_mean_grade(second_student.grades)}')
print('')

# Сравнение лекторов

print('Compare lectors')
hot_lector.__str__()

print(f'grades: {hot_lector.grades}')
print('')

lazy_lector.__str__()

print(f'grades: {lazy_lector.grades}')
print('')

print(f'Lector {hot_lector.name} {hot_lector.surname}\
      is_teaching_worse_than {lazy_lector.name} {lazy_lector.surname} \
         result_is:  {is_first_person_worse(hot_lector, lazy_lector)}') 
print('')
print(f'Student {hot_lector.name} {hot_lector.surname}\
      is_equal_in_teaching_with {lazy_lector.name} {lazy_lector.surname} \
         result_is:  {are_persons_equal(hot_lector, lazy_lector)}') 
print('')

course1 = 'Math'
print(f'Mean_degree_on_course {course1}: \
      {meancourse_grade_stud_lec(course1, [hot_lector, lazy_lector])}')
print('')

course2 = 'Python'
print(f'Mean_degree_on_course {course2}: \
      {meancourse_grade_stud_lec(course2, [hot_lector, lazy_lector])}')
print('')

course3 = 'Python'
print(f'Mean_degree_on_course {course3}: \
      {meancourse_grade_stud_lec(course3, [first_student, second_student])}')
print('')

course4 = 'C++'
print(f'Mean_degree_on_course {course4}: \
      {meancourse_grade_stud_lec(course4, [first_student, second_student])}')
print('')