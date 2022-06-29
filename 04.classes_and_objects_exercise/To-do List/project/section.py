# from project.task import Task


# class Section:
#     def __init__(self, name: str):
#         self.name = name
#         self.tasks = []

#     def add_task(self, new_task: Task):
#         for task in self.tasks:
#             if task.name == new_task.name:
#                 return f"Task is already in the section {self.name}"

#         self.tasks.append(new_task)
#         return f"Task {Task.details(new_task)} is added to the section"

#     def view_section(self):
#         data = f"Section {self.name}:\n"
#         data += "\n".join([Task.details(i) for i in self.tasks])
#         return data

#     def complete_task(self, task_name: str):
#         for task in self.tasks:
#             if task.name == task_name:
#                 task.completed = True
#                 return f"Completed task {task_name}"
#         else:
#             return f"Could not find task with the name {task_name}"

#     def clean_section(self):
#         task_counter = 0
#         for task in self.tasks:
#             if task.completed:
#                 self.tasks.clear()
#                 task_counter += 1

#         return f"Cleared {task_counter} tasks."


from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for section_task in self.tasks:
            if section_task.name == new_task:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {Task.details(new_task)} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task == task_name:
                task.completed = True
            return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount = 0

        for task in self.tasks:
            if task.completed is True:
                self.tasks.remove(task)
                amount += 1
        return f"Cleared {amount} tasks."

    def view_section(self):
        data = ''
        data += f"Section {self.name}:" + "\n"
        for task in self.tasks:
            data += task.details() + "\n"

        return data.strip()
