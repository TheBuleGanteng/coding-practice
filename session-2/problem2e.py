# Redo for practice: plain class 
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

class ScoreData:
    def __init__(self):
        self.scores = []
        self.total = 0
        
class Gradebook:
    
    def __init__(self): # Doesn't take arguments per spec
        self.records: dict[str, ScoreData] = {} # Create a dict w/ key= string (student name) and value = ScoreData object (list for all scores and int for total score)
        
    def add_score(self, student: str, score: int):
        score_data = self.records.get(student, ScoreData()) # Find the existing record for this student and retrieve the value for that record (e.g. the ScoreData for this student), creating a new ScoreData structure if the student isn't already in Gradebook. 
        score_data.scores.append(score) # Append the new score to the scores section of this score_data (a ScoreData object)
        score_data.total += score # Add the new score to the total section of this score_data (a ScoreData object)
        self.records[student] = score_data # Store the newly-updated ScoreData object (the list of scores and total score) as the value in the dict for this student
    
    def average(self, student: str):
        score_data = self.records.get(student, ScoreData()) # Retrieve the ScoreData object for this student, or create and return an empty one if the student is new
        num_scores = len(score_data.scores) 
        if num_scores == 0: 
            return None # Per spec
        else:
            return float(score_data.total / num_scores) # Average as a float, per spec
    
    def top_student(self):
        if len(self.records) == 0:
            return None
        score_data = min(self.records.items(), key=lambda kv:(-self.average(kv[0]), kv[0])) # type: ignore # Find max score w/ name as tiebreaker. Note use of min, since can't use max -kv[text].
        return score_data[0] 
        
    def students(self):
        return sorted([student for student, score_data in self.records.items() if len(score_data.scores) > 0])

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