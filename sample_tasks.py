from models import Task

def get_tasks():
    return [
        Task("T1", 5, 10, 3),
        Task("T2", 2, 8, 2, ["T1"]),
        Task("T3", 4, 15, 4, ["T1"]),
        Task("T4", 1, 12, 3),
        Task("T5", 3, 20, 2, ["T2", "T4"])
    ]