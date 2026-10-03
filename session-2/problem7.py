'''
Session 2, Problem 6: TaskList

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes.

Write a class that keeps track of tasks and their priorities. A lower priority number means a more urgent task.

Class name: TaskList

Creating a TaskList() takes no arguments, and a new task list starts with no tasks.

Methods:

1. add_task(name, priority): name is a string, priority is an int. Adds a task with that priority. 
Returns True if the task was added, or False if a task with that name already exists (its priority is left unchanged).
2. change_priority(name, priority): name is a string, priority is an int. 
Sets the task's priority to the new value and returns its old priority, as an int. 
Returns None if there is no task with that name.
3. complete(name): name is a string. 
Removes the task from the list and returns its priority, as an int. Returns None if there is no task with that name.
4. next_task(): no arguments. 
Returns the name of the most urgent task. If tasks tie for most urgent, returns the name that comes first alphabetically. Returns None if there are no tasks.
'''

class TaskList:
    
    def __init__(self):
        self.records: dict[str, int] = {}
        
    def add_task(self, name: str, priority: int):
        task_data = self.records.get(name, None)
        if task_data is not None:
            return False
        self.records[name] = priority
        return True

    def change_priority(self, name: str, priority: int):
        task_data = self.records.get(name, None)
        if task_data is None:
            return None
        self.records[name] = priority
        print(f'name: {name}, self.records[name]: {self.records[name]}')
        return task_data

    def complete(self, name: str):
        task_data = self.records.get(name, None)
        if task_data is None:
            return None
        del(self.records[name])
        return task_data
    
    def next_task(self):
        if len(self.records.items()) == 0:
            return None
        most_urgent = min(self.records.items(), key= lambda kv:(kv[1], kv[0]))
        print(f'most_urgent: {most_urgent}')
        return most_urgent[0]
        
# Complexity:
# 1. add_task: O(1)
# 2. change_priority: O(1)
# 3. complete: O(1)
# 3. Min O(m)
# Worst case O(m) w/ memory of O(m)
        
# Example tests:

tasks = TaskList()
assert tasks.add_task("email", 2) is True
assert tasks.add_task("clean", 2) is True
assert tasks.add_task("email", 2) is False

assert tasks.change_priority('email', 3) == 2
assert tasks.change_priority('email', 2) == 3
assert tasks.change_priority('not included', 2) is None

assert tasks.complete('email') == 2
assert tasks.complete('not included') is None

assert tasks.add_task("email", 1) is True
assert tasks.next_task() == 'email'

assert tasks.complete("not included") is None
assert tasks.change_priority("clean", 1) == 2
assert tasks.next_task() == 'clean'

tasks2 = TaskList()
assert tasks2.next_task() is None

print('all tests pass')