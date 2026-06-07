import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Task Scheduler", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center; color:#00ffd5;'>⚡ Task Scheduler Optimization System</h1>
<p style='text-align:center; color:gray;'>DSA • Greedy Algorithm • Priority Scheduling</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- SESSION STATE ----------------
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"task": "T1", "priority": 8, "deadline": 10, "duration": 3},
        {"task": "T2", "priority": 3, "deadline": 8, "duration": 2},
        {"task": "T3", "priority": 6, "deadline": 15, "duration": 4},
    ]

# ---------------- SIDEBAR INPUT ----------------
st.sidebar.header("➕ Add Task")

task_name = st.sidebar.text_input("Task Name")
priority = st.sidebar.slider("Priority", 1, 10, 5)
deadline = st.sidebar.number_input("Deadline", 1, 100, 10)
duration = st.sidebar.number_input("Duration", 1, 20, 3)

add_btn = st.sidebar.button("Add Task")

if add_btn and task_name:
    st.session_state.tasks.append({
        "task": task_name,
        "priority": priority,
        "deadline": deadline,
        "duration": duration
    })
    st.success(f"Task {task_name} added!")

# ---------------- GREEDY SCHEDULER ----------------
def schedule(tasks):
    tasks = sorted(tasks, key=lambda x: (-x["priority"], x["deadline"]))

    time = 0
    result = []
    missed = []

    for t in tasks:
        start = time
        end = time + t["duration"]

        if end > t["deadline"]:
            missed.append(t["task"])
        else:
            result.append([t["task"], start, end])
            time = end

    return result, missed


schedule_result, missed = schedule(st.session_state.tasks)

# ---------------- DATAFRAME ----------------
df = pd.DataFrame(schedule_result, columns=["Task", "Start", "End"])

# ---------------- KPI SECTION ----------------
col1, col2, col3 = st.columns(3)

col1.metric("📌 Total Tasks", len(st.session_state.tasks))
col2.metric("✅ Scheduled", len(schedule_result))
col3.metric("❌ Missed", len(missed))

st.markdown("---")

# ---------------- GRAPH (FIXED VERSION) ----------------
st.subheader("📊 Execution Timeline")

if schedule_result:

    tasks = [x[0] for x in schedule_result]
    start = [x[1] for x in schedule_result]
    end = [x[2] for x in schedule_result]
    duration = [e - s for s, e in zip(start, end)]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=duration,
        y=tasks,
        orientation='h',
        marker=dict(color='#00ffd5')
    ))

    fig.update_layout(
        title="Task Execution Flow",
        xaxis_title="Time Units",
        yaxis_title="Tasks",
        height=500,
        plot_bgcolor="#0f0f0f",
        paper_bgcolor="#0f0f0f",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No schedule generated!")

# ---------------- TABLE ----------------
st.subheader("📋 Execution Plan")
st.dataframe(df, use_container_width=True)

# ---------------- MISSED TASKS ----------------
st.subheader("❌ Missed Tasks")
st.write(missed if missed else "No missed tasks 🎉")

# ---------------- RAW DATA ----------------
st.subheader("📦 All Tasks")
st.write(st.session_state.tasks)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
<div style='text-align:center;color:gray;'>
Built by Aarthi • DSA Project • Task Scheduling System
</div>
""", unsafe_allow_html=True)