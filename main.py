# Подключение классов
from generator.objects_generator import generate_task
from generator.objects_generator import generate_expert

def distribute_task_to_expert():
    pass

list_of_tasks = []
list_of_experts = []

# Генерация заданий
for task in range(1, 100):
    task = generate_task()
    list_of_tasks.append(task)

# Генерация экспертов
for expert in range(1, 5):
    expert = generate_expert()
    list_of_experts.append(expert)

for expert in list_of_experts:
    for task in list_of_tasks:
        if expert.subjectArea == task.subjectArea:
            expert.add_task(task)
            print(f'Эксперт по предмету "{expert.subjectArea}" - Задание по "{task.subjectArea}"')







