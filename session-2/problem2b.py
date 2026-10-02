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

1. add_score(student, score): student is a string, score an int from 0 to 100. Records one score for that student. A student can have any number of scores. Returns nothing.
2. average(student): student is a string. Returns the student's average score as a float, or None if the student has no scores.
3. top_student(): no arguments. Returns the name of the student with the highest average. 
If students tie on the highest average, it returns the name that comes first alphabetically. 
Returns None if no scores have been recorded.
4. students(): no arguments. Returns a list of the names of all students with at least one score, sorted alphabetically.
'''
'''
STEPS TO SOLVE
1. Class must remember (stored on self)? --> student and the corresponding scores for that student
2. What the structure of that item stored on self? 
key = item used to look up values --> student (a string)
value = the value corresponding to that key that would allow the methods to work --> scores (a list of ints)  
'''

from dataclasses import dataclass, field

@dataclass
class Gradebook:
    
    # A "record" is a dict w/ the following compontents:
    # 1. key=student (string) and 
    # 2. a container (in the form of a list). This container will itself contain 2 items: 
    # 2a: another list, wherein value=scores (list of ints, each representing a score for that student)
    # 2b. an int, representing the total of those scores
    record: dict[str, list] = field(default_factory=dict)  
    
    def add_score(self, student: str, score: int):
        # Needed in case the student isn't already in the dict (in which case, there is no list to which we can append the new score).
        # To solve this, we use .get() to return either:
        # (a) the student's list of scores (if the student already has a record) OR
        # (b) a list that contains an empty list at pos [0] and 0 at pos [1]
        # We return nothing
        
        # Pull either the existing list of scores + total or return an empty list containing (a) another empty list (to hold the scores) and (b) and int (to store the total)
        scores = self.record.get(student, [[] , 0])
        print(f'runnning .add_score() scores: {scores}')
        
        # For the value corresponding to this student, do the following:
        # at pos [0]: append the new score to the list of scores (either existing scores or an empty list, per the fallback in .get())
        # at pos [1]: the prior total (either the prior total or 0, per the fallback in .get(), plus the new score)
        scores[0].append(score)
        scores[1] = scores[1] + score

        # Update the record for this student with (a) the updated list of scores and (b) the updated total
        self.record[student] = scores  
        print(f'Gradebook.add_score() updated self.record[student] to: {self.record[student]} by appending score: {score}')
        
    def average(self, student:str):
        student_record = self.record.get(student) # You never need the fallback None with .get, since that's the default fallback anyway
        
        if student_record is not None:
            print(f'student_record: {student_record}')
            scores_mean = student_record[1] / len(student_record[0])
            print(f'Gradebook.average() returning scores_mean: {scores_mean}')
            return (scores_mean)
        else:
            print(f'Gradebook.average() returning None')
            return None
    
    def top_student(self):
        all_records = self.record.items()
        # If no records recorded, return None, per spec
        if len(all_records) == 0:
            return None
        # If there are records, get the average score for each student
        else:
            averages = {} # k=student name, v=avg score for student
            for name, student_record in all_records:
                averages[name] = self.average(name)
            print(f'averages: {averages}')
        
        # Sort by top score, then name, per spec     
        top = min(averages.items(), key=lambda kv:(-kv[1], kv[0])) # IMPT: Never use max when sorting text, better to use min and reverse signs for the kv[]  items    
        print(f'top: {top}, returning top[0]: {top[0]}')
        return top[0]
    
    def students(self):
        solution = sorted([name for name, student_record in self.record.items() if len(student_record[0]) > 0])
        print(f'returning solution: {solution}')
        return solution


'''
Complexity:
s = # of scores for a specific student
n = number of total scores in aggregate
m = number of students
1. add_score --> all items lookups or artithmithic are O(1) --> O(1)
2. average --> simply reads existing total from dict --> O(1)
3. top_student --> calls .average() once per student O(m) + does a min across students O(m) --> O(m + m) --> O(2m) --> O(m) 
3. students --> sort --> O(m log m)
Most expensive: O(m + m log m) --> O(m log m)
Total memory: O(n + m) --> since m <= n --> O(n)
'''

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