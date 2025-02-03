import json

class TaskTracker:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = {
                "Sunday": [
                    {"time": "5:30-6:00am", "task": "Brush teeth, take a shower", "completed": False},
                    {"time": "6:30-7:00am", "task": "Worship time with family", "completed": False},
                    {"time": "7:00-7:30am", "task": "Breakfast", "completed": False},
                    {"time": "7:30-8:00am", "task": "Bible time", "completed": False},
                    {"time": "8:00-12:00pm", "task": "Help siblings with school", "completed": False},
                    {"time": "12:00-1:00pm", "task": "Lunch", "completed": False},
                    {"time": "1:00-2:00pm", "task": "TV", "completed": False},
                    {"time": "2:00-3:00pm", "task": "Bible time", "completed": False},
                    {"time": "3:00-5:00pm", "task": "Errands", "completed": False},
                    {"time": "5:00-6:30pm", "task": "Dinner", "completed": False},
                    {"time": "6:30-7:00pm", "task": "Worship", "completed": False},
                    {"time": "7:00-8:00pm", "task": "Shower", "completed": False},
                    {"time": "8:00-9:30pm", "task": "Bible time", "completed": False},
                    {"time": "9:30-10:00pm", "task": "Get ready for bed", "completed": False}
                ],
            }
            self.save_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def complete_task(self, day, index):
        if day in self.tasks and 0 <= index < len(self.tasks[day]):
            self.tasks[day][index]["completed"] = True
            print("You earned a butterfly! 🦋")
            self.save_tasks()
        else:
            print("Invalid task selection.")
    
    def add_task(self, day, time, task):
        if day not in self.tasks:
            self.tasks[day] = []
        self.tasks[day].append({"time": time, "task": task, "completed": False})
        self.save_tasks()
    
    def edit_task(self, day, index, time=None, task=None):
        if day in self.tasks and 0 <= index < len(self.tasks[day]):
            if time:
                self.tasks[day][index]["time"] = time
            if task:
                self.tasks[day][index]["task"] = task
            self.save_tasks()
        else:
            print("Invalid task selection.")
    
    def display_tasks(self, day):
        if day in self.tasks:
            print(f"Tasks for {day}:")
            for i, t in enumerate(self.tasks[day]):
                status = "✔️" if t["completed"] else "❌"
                print(f"[{i}] {t['time']}: {t['task']} {status}")
        else:
            print("No tasks for this day.")

# Example Usage
task_tracker = TaskTracker()
task_tracker.display_tasks("Sunday")
task_tracker.complete_task("Sunday", 0)