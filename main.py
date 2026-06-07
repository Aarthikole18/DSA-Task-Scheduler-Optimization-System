from sample_tasks import get_tasks
from scheduler import schedule
from metrics import compute_metrics


def main():
    tasks = get_tasks()

    print("\n🧠 TASK SCHEDULER OPTIMIZATION SYSTEM")
    print("=" * 50)

    schedule_result, missed = schedule(tasks)
    metrics = compute_metrics(schedule_result, tasks)

    print("\n📌 OPTIMIZED SCHEDULE:")
    for s in schedule_result:
        print(f"Task {s[0]} -> Start: {s[1]} | End: {s[2]}")

    print("\n❌ MISSED TASKS:", missed)

    print("\n📊 PERFORMANCE METRICS:")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    print("\n🚀 SYSTEM EXECUTION COMPLETE")


if __name__ == "__main__":
    main()