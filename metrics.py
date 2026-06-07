def compute_metrics(schedule, tasks):
    task_map = {t.task_id: t for t in tasks}

    total = len(schedule)
    on_time = 0
    lateness = 0

    for t_id, start, end in schedule:
        task = task_map[t_id]

        if end <= task.deadline:
            on_time += 1
        else:
            lateness += end - task.deadline

    return {
        "total_tasks_scheduled": total,
        "on_time_tasks": on_time,
        "lateness": lateness
    }