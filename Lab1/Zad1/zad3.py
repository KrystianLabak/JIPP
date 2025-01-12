class Task:
    def __init__(self, execution_time: int, reward: int):
        self.execution_time = execution_time
        self.reward = reward

    @staticmethod
    def sort_tasks_functional(taskslist: list['Task']) -> list['Task']:
        return sorted(taskslist, key=lambda task: (-task.reward, task.execution_time))

    @staticmethod
    def sort_tasks_procedural(taskslist: list['Task']) -> list['Task']:
        def qsort(tasks, low, high):
            if low < high:
                part = partition(tasks, low, high)
                qsort(tasks, low, part - 1)
                qsort(tasks, part + 1, high)

        def partition(tasks, low, high):
            pivot = tasks[high]
            i = low - 1
            for j in range(low, high):
                if (tasks[j].reward > pivot.reward) or \
                   (tasks[j].reward == pivot.reward and tasks[j].execution_time < pivot.execution_time):
                    i += 1
                    tasks[i], tasks[j] = tasks[j], tasks[i]
            tasks[i + 1], tasks[high] = tasks[high], tasks[i + 1]
            return i + 1

        qsort(taskslist, 0, len(taskslist) - 1)
        return taskslist


if __name__ == "__main__":
    tasks = [
        Task(execution_time=3, reward=10),
        Task(execution_time=1, reward=20),
        Task(execution_time=2, reward=15),
        Task(execution_time=5, reward=5),
        Task(execution_time=4, reward=10),
        Task(execution_time=2, reward=20),
        Task(execution_time=50, reward=50)
    ]

    sorted_tasks_functional = Task.sort_tasks_functional(tasks)
    print("Functional sorted:")
    for task in sorted_tasks_functional:
        print(f"Reward: {task.reward}, Execution Time: {task.execution_time}")
    sorted_tasks_procedural = Task.sort_tasks_procedural(tasks)
    print("\nProcerudal sorted:")
    for task in sorted_tasks_procedural:
        print(f"Reward: {task.reward}, Execution Time: {task.execution_time}")