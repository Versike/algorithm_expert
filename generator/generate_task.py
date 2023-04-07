# Подключение классов
from classes.task import Task

# Подключение библиотек
import random

# Подключение доп файлов
import harvested_information.harvested as hs


# Генерация заданий

def generate_expert():
    subject_area = random.choice(hs.subjects_list)
    number_of_task = random.randint(1, 21)
    variant_of_task = random.randint(1, 30)
    is_difficult = random.choice([True, False])
    number_of_rate = random.randint(1, 2)
    is_third_rate = random.choice([True, False])
    task = Task(
        subject_area=subject_area,
        number_of_task=number_of_task,
        variant_of_task=variant_of_task,
        is_difficult=is_difficult,
        number_of_rate=number_of_rate,
        is_third_rate=is_third_rate,
    )
    return task
