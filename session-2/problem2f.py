# Redo for practice: plain class w/ helper class 
'''
Session 2, Problem 2: Gradebook (class warm-up)

Time limit: none. This is another untimed warm-up. 
As a rough guide, aim for about 25 minutes. Try it from memory first. 
If you're stuck on syntax for more than 5 minutes, looking it up is fine; note that you did.

The step up from yesterday: each student has several scores, so the values stored in your dict won't be single numbers.

Write a class that records students' test scores.

Class name: Gradebook

Creating a Gradebook() takes no arguments, and a new gradebook starts empty.

Methods:

1. add_score(student, score): student is a string, score an int from 0 to 100. Records one score for that student. 
A student can have any number of scores. Returns nothing.
2. average(student): student is a string. Returns the student's average score as a float, or None if the student has no scores.
3. top_student(): no arguments. Returns the name of the student with the highest average. 
If students tie on the highest average, it returns the name that comes first alphabetically. 
Returns None if no scores have been recorded.
4. students(): no arguments. Returns a list of the names of all students with at least one score, sorted alphabetically.
'''
'''
THOUGHTS:
1. class Gradebook needs:
(a) student name
(b) list of student scores + total of scores
2. Create a helper class ScoreData
scores = []
total = 0
'''

class ScoreData:
    
    def __init__(self):
        self.scores = []
        self.total = 0
        
class Gradebook:
    
    def __init__(self):
        self.records: dict[str, ScoreData] = {}
        
    def add_score(self, student: str, score: int):
        student_data = self.records.get(student, ScoreData())
        student_data.scores.append(score) # Update list of scores
        if len(student_data.scores) == 0: # Update score total
            student_data.total = score
        else:
            student_data.total += score
        self.records[student] = student_data
    
    def average(self, student: str):
        student_data = self.records.get(student, ScoreData())
        num_scores = len(student_data.scores) 
        if num_scores == 0: # Return None, per spec
            return None
        return float(student_data.total / num_scores)
    
    def top_student(self):
        if len(self.records) == 0:  # Per spec
            return None
        top_student_data = min(self.records.items(), key=lambda kv:(-self.average(kv[0]), kv[0])) # type: ignore
        return top_student_data[0]
    
    def students(self):
        return sorted([student for student, score_data in self.records.items() if len(score_data.scores) > 0])
    
# Complexity:
# 1. add_score --> append and arithmatic --> O(1) 
# 2. average --> lookup, arithmatic --> O(1)
# 3. top_student --> max/min by number of students --> O(m)
# 4. students --> sorting by number of students --> O(m log m)
# Worse case: O(m + m log m) --> O(m log m)
# Memory: O(m + n) --> m <= n --> O(2n)  --> O(n)

# Tests

gb = Gradebook()
assert gb.average("ann") is None
assert gb.top_student() is None
assert gb.students() == []

gb.add_score("ann", 80)
gb.add_score("bob", 90)
gb.add_score("ann", 100)
assert gb.average("ann") == 90.0
assert gb.average("bob") == 90.0
assert gb.top_student() == "ann"      # tie on 90.0, so the alphabetically first name wins

gb.add_score("cat", 95)
assert gb.top_student() == "cat"
assert gb.students() == ["ann", "bob", "cat"]

gb2 = Gradebook()
assert gb2.students() == []           # a second gradebook must not share data with the first
print("all tests passed")