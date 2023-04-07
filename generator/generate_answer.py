# # Подключение классов
# from classes.answer import Answer
#
# # Подключение библиотек
# import random
#
# # Подключение доп файлов
# import harvested_information.harvested as hs
#
#
# # Генерация экспертов
#
# def generate_expert():
#     name = random.choice(hs.fio_list)
#     subject_area = random.choice(hs.subjects_list)
#     number_of_rate = random.randint(1, 2)
#     access_to_additional_verification = random.choice([True, False])
#     expert = Expert(
#         name=name,
#         subject_area=subject_area,
#         number_of_rate=number_of_rate,
#         access_to_additional_verification=access_to_additional_verification,
#     )
#     return expert
