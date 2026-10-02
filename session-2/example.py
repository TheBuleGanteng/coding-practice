class StudentRecord:
    def __init__(self, total: int = 0, scores: list = []):   # the [] is created once
        self.total = total
        self.scores = scores

ann = StudentRecord()
bob = StudentRecord()
ann.scores.append(80)
print(bob.scores)   # [80]  <- bob got ann's score; both point to the same list