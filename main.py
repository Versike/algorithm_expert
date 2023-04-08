# Подключение классов
from generator.objects_generator import generate_task
from generator.objects_generator import generate_expert

import random

list_of_tasks = []

for task in range(1, 25):
    task = generate_task()
    list_of_tasks.append(task)

expert_1 = generate_expert()
expert_1.add_task(list_of_tasks[5])
expert_1.debug_print_expert()
expert_1.tasks[0].debug_print_task()



