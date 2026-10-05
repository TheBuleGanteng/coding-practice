'''
Session 2, Problem 11: Course registration (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Write a class that manages course enrollments.

Class name: Registrar

Creating a Registrar() takes no arguments, and a new registrar starts with no courses.

Methods:

create_course(course_id, capacity): course_id is a string, capacity is a positive int. Creates a course that can hold at most capacity students. Returns True if the course was created, or False if a course with that id already exists (the existing course is left unchanged).
enroll(student, course_id): student and course_id are strings. Enrolls the student in the course. Returns True if the student was enrolled. Returns False, with nothing changed, if the course doesn't exist, if the student is already enrolled in it, or if the course is full.
drop(student, course_id): student and course_id are strings. Removes the student from the course. Returns True if the student was enrolled and has been removed, or False otherwise.

----------------------------------------------------

Session 2, Problem 11: Course registration. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Add two methods to your Registrar class. Everything from Level 1 must keep working.

New methods:

student_courses(student): student is a string. Returns a list of the ids of all courses the student is currently enrolled in, sorted alphabetically. Returns an empty list if the student isn't enrolled in any course.
popular_courses(n): n is a non-negative int. Returns a list of the n courses with the most students currently enrolled, each as a string in the format "course_id(count)". The list is sorted by count, largest first; courses with equal counts are sorted alphabetically by id. Every course is included in the ranking, including courses with no students (count 0). If there are fewer than n courses, returns all of them.
'''

class Registrar:
    
    def __init__(self):
        self.course_capacities: dict[str, int] = {} # course_id: capacity
        self.course_enrollments: dict[str, set] = {} #course_id:set of student names

    '''1. create_course(course_id, capacity): course_id is a string, capacity is a positive int. 
    Creates a course that can hold at most capacity students. 
    Returns True if the course was created, or False if a course with that id already exists (the existing course is left unchanged).'''
    def create_course(self, course_id: str, capacity: int):
        # Pull capacity for this course
        course_capacity = self.course_capacities.get(course_id, None)
        # If this course already exists, return False per spec
        if course_capacity is not None:
            return False
        self.course_capacities[course_id] = capacity
        self.course_enrollments[course_id] = set()
        print(f'self.course_capacities[course_id]: {self.course_capacities[course_id]}, self.course_enrollments[course_id]: {self.course_enrollments[course_id]}')
        return True

    '''2. enroll(student, course_id): student and course_id are strings. 
    Enrolls the student in the course. Returns True if the student was enrolled. 
    Returns False, with nothing changed, if the course doesn't exist, if the student is already enrolled in it, or if the course is full.'''
    def enroll(self, student: str, course_id: str):
        # Pull capacity for this course
        course_capacity = self.course_capacities.get(course_id, None)
        course_enrollment = self.course_enrollments.get(course_id, set())
        # Return false if (a) course doesn't exist (b) 
        if course_capacity is None or student in course_enrollment or len(course_enrollment) >= course_capacity:
            return False
        # Otherwise, enroll the student
        course_enrollment.add(student)
        self.course_enrollments[course_id] = course_enrollment
        return True
         
    '''3. drop(student, course_id): student and course_id are strings. 
    Removes the student from the course. 
    Returns True if the student was enrolled and has been removed, or False otherwise.'''
    def drop(self, student: int, course_id: str):
        # Pull capacity for this course
        course_capacity = self.course_capacities.get(course_id, None)
        course_enrollment = self.course_enrollments.get(course_id, set())
        print(f'course_capacity: {course_capacity}, course_enrollment: {course_enrollment}')
        # If course exists and student is enrolled, remove student
        if course_capacity is not None and student in course_enrollment:
            course_enrollment.remove(student)
            self.course_enrollments[course_id] = course_enrollment
            print(f'self.course_enrollments[course_id]: {self.course_enrollments[course_id]}')
            return True
        return False     
    
    '''4. student_courses(student): student is a string. 
    Returns a list of the ids of all courses the student is currently enrolled in, sorted alphabetically. 
    Returns an empty list if the student isn't enrolled in any course.'''
    def student_courses(self, student: str):
        return sorted([(course) for course, enrollments in self.course_enrollments.items() if student in enrollments])

    '''5. popular_courses(n): n is a non-negative int. 
    Returns a list of the n courses with the most students currently enrolled, each as a string in the format "course_id(count)". 
    The list is sorted by count, largest first; courses with equal counts are sorted alphabetically by id. Every course is included in the ranking, including courses with no students (count 0). 
    If there are fewer than n courses, returns all of them.'''
    def popular_courses(self, n: int):
        # Stores course: enrollment
        course_enrollments = {}
        # Loop, appending dict with course:enrollment
        for course, enrollments in self.course_enrollments.items():
            course_enrollments[course] = len(enrollments)
        # Sort by # enrolled, alph
        course_enrollments_sorted = sorted(course_enrollments.items(), key=lambda kv:(-kv[1], kv[0]))
        # Window
        course_enrollments_sorted_windowed = course_enrollments_sorted[:n]
        print(f'course_enrollments_sorted_windowed: {course_enrollments_sorted_windowed}')
        # Formatting
        course_enrollments_sorted_windowed_formatted = [(f'{course}({enrollment})') for course, enrollment in course_enrollments_sorted_windowed]
        return course_enrollments_sorted_windowed_formatted
        
# Complexity:
# 1. create_course --> O(1)
# 2. enroll --> if student in set() --> O(1) 
# 3. drop --> set.remove() --> O(1) 
# 4. student_courses --> does this for each course (n courses): "if student in enrollments" O(n*1) n= # courses, then sorts the result O(n log n) w/ n=courses --> O(n + n log n) --> O(n log n)
# 5. popular_courses --> loop O(n) + sort O(n log n) + list comp O(n) --> O(n log n)



# Worse case complexity: O(n log n)
# Memory: O(n + m) w/ n = # classes, m = # enrollments 
    
    
# Example tests:

registrar = Registrar()
registrar.create_course("cs101", 1)
assert registrar.create_course("cs101", 1) is False # Course already exists
assert registrar.enroll("ann", "cs101") is True
assert registrar.enroll("bob", "cs101") is False
assert registrar.enroll("bob", "history") is False # course doesn't exist
assert registrar.enroll("ann", "cs101") is False # Re-register

registrar = Registrar()
assert registrar.drop("ann", "cs101") is False # type: ignore
registrar.create_course("cs101", 1) 
assert registrar.drop("ann", "cs101") is False # Course exists but student isn't in it # type: ignore
assert registrar.enroll("ann", "cs101") is True
assert registrar.drop("ann", "cs101") is True # Course exists but student isn't in it # type: ignore

registrar = Registrar()
registrar.create_course("math", 5)
registrar.create_course("art", 5)
registrar.enroll("ann", "math")
registrar.enroll("ann", "art")
assert registrar.student_courses("ann") == ["art", "math"]
assert registrar.student_courses("joe") == [] # Isn't enrolled
assert registrar.drop("ann", "math") is True # type: ignore
assert registrar.drop("ann", "art") is True # type: ignore
assert registrar.student_courses("joe") == [] # Isn't enrolled
assert registrar.student_courses("ann") == [] # Isn't enrolled


registrar = Registrar()
registrar.create_course("math", 5)
registrar.create_course("art", 5)
registrar.enroll("ann", "math")
assert registrar.popular_courses(2) == ["math(1)", "art(0)"]
assert registrar.enroll("ann", "art") is True
assert registrar.popular_courses(2) == ["art(1)", "math(1)"] #enrollment tie --> aplh
assert registrar.popular_courses(10) == ["art(1)", "math(1)"] # if n > courses, return all
assert registrar.popular_courses(1) == ["art(1)"] # Tie + alpha sort
assert registrar.drop("ann", "art") is True # type: ignore
assert registrar.drop("ann", "math") is True # type: ignore
assert registrar.popular_courses(2) == ["art(0)", "math(0)"] # zero enrollment


print(f'all tests pass')