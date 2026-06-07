class Task:
    def __init__(self, task_id, priority, deadline, duration, dependencies=None):
        self.task_id = task_id
        self.priority = priority
        self.deadline = deadline
        self.duration = duration
        self.dependencies = dependencies or []

    def __lt__(self, other):
        # Higher priority first, then earlier deadline
        if self.priority == other.priority:
            return self.deadline < other.deadline
        return self.priority > other.priority