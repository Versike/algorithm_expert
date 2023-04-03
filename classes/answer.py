class Answer:
    """
    Класс овтета содержит в себе поля:
    Предметная область - subjectArea: string
    Номер задания - numberOfTask: int
    Вариант задания - variantOfTask: int
    """
    def __init__(
            self,
            subject_area: str,
            number_of_task: int,
            variant_of_task: int,
    ):
        self.subjectArea = subject_area
        self.numberOfTask = number_of_task
        self.variantOfTask = variant_of_task

    def debug_print_answer(self):
        print(f"Информация об ответе:\n"
              f"Предметная область - {self.subjectArea}\n"
              f"Номер задания - {self.numberOfTask}\n"
              f"Вариант задания - {self.variantOfTask}\n",
              )