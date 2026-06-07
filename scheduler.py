def schedule_tasks(tasks):
    tasks = sorted(tasks, key=lambda x: (-x["priority"], x["deadline"]))

    time = 0
    schedule = []
    missed = []

    for t in tasks:
        start = time
        end = time + t["duration"]

        if end > t["deadline"]:
            missed.append(t["task_id"])
        else:
            schedule.append((t["task_id"], start, end))
            time = end

    return schedule, missed