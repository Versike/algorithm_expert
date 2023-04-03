# Подключение классов
from classes.answer import Answer
from classes.task import Task
from classes.expert import Expert

# Подключение библиотек
import streamlit as st
import random

import harvested_information.harvested as hs

# Подключаем стримлитку st
st.title('Приложение для отработки алгоритмов')

expertList = []
st.write("Добавить случайного эксперта")
if st.button("Добавить эксперта"):
    expert = Expert(
        name=random.choice(hs.fio_list),
        subject_area=random.choice(hs.subjects_list),
        number_of_rate=1,
        access_to_additional_verification=False
    )
    expertList.append(expert)
    st.write(f"{expert.name} {expert.subjectArea} "
             f"добавлен!")
    del expert
# #Тестируем пока классы, чтобы выявить необхожимые параметры
#
# #Создание тестового эксперта
# expertTestOne = Expert(
#     name="Жмышенко В.А.",
#     subject_area="Физика",
#     number_of_rate=1,
#     access_to_additional_verification=False,
# )
# expertTestOne.debug_print_expert()
#
# #Создание тестового задания
# taskTestOne = Task(
#     subject_area="Физика",
#     number_of_task=2,
#     variant_of_task=1,
#     is_difficult=False,
#     number_of_rate=1,
#     is_third_rate=False
# )
# taskTestOne.debug_print_task()
#
# #Создание тестового ответа
# answerTestOne = Answer(
#     subject_area=taskTestOne.subjectArea,
#     number_of_task=taskTestOne.numberOfTask,
#     variant_of_task=taskTestOne.variantOfTask
# )
# answerTestOne.debug_print_answer()