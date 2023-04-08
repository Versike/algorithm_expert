class Task:
    """
    Класс задание содержит в себе поля:
    Предметная область - subjectArea: string
    Номер задания - numberOfTask: int
    Вариант задания - variantOfTask: int
    Уровень задания(простой false или развернутый true) - isDifficult: bool
    Кол-во проверок(1 2) - numberOfRate: int
    Необходимость в 3 проверке - isThirdRate: bool
    """
    def __init__(
            self,
            subject_area: str,
            number_of_task: int,
            variant_of_task: int,
            is_difficult: bool,
            number_of_rate: int,
            is_third_rate: bool
    ):
        self.subjectArea = subject_area
        self.numberOfTask = number_of_task
        self.variantOfTask = variant_of_task
        self.isDifficult = is_difficult
        self.numberOfRate = number_of_rate
        self.isThirdRate = is_third_rate

    def debug_print_task(self):
        print(f"Информация о задании:\n"
              f"Предметная область - {self.subjectArea}\n"
              f"Номер задания - {self.numberOfTask}\n"
              f"Вариант задания - {self.variantOfTask}\n"
              f"Уровень задания - {self.isDifficult}\n"
              f"Количество проверок - {self.numberOfRate}\n"
              f"Необходимость в 3 проверке - {self.isThirdRate}\n"
              )
