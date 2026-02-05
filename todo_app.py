import streamlit as st


# App Title
# -------------------------------
st.title("Simple To-Do List")




# -------------------------------
# Initialize task list
# (Using session_state so tasks are not lost on refresh)
# -------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []





# -------------------------------
# Text input for new task
# -------------------------------
task = st.text_input("Enter a task")





# -------------------------------
# Add Task Button
# -------------------------------
if st.button("Add Task"):
    if task.strip() != "":
        st.session_state.tasks.append(task)
        st.success("Task added successfully!")
    else:
        st.warning("Please enter a task before adding.")




        

# -------------------------------
# Display Tasks
# -------------------------------
st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.write("No tasks added yet.")
else:
    for index, task in enumerate(st.session_state.tasks, start=1):
        st.write(f"{index}. {task}")
