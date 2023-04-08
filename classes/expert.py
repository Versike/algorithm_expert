class Expert:
    """
    Класс эксперт содержит в себе поля:
    ФИО - name: string
    Предметная область - subjectArea: string
    Кол-во проверок - numberOfRate: int
    Доступ к 3 проверки - accessToAdditionalVerification: bool
    """
    def __init__(
            self, name: str,
            subject_area: str,
            number_of_rate: int,
            access_to_additional_verification: bool,
    ):
        self.name = name
        self.subjectArea = subject_area
        self.numberOfRate = number_of_rate
        self.accessToAdditionalVerification = access_to_additional_verification
        self.tasks = []
        self.completed_tasks = []
# Дополнение заданий к эксперту
    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        self.completed_tasks.append(task)

    def debug_print_expert(self):
        print(f"Информация об эксперте:\n"
              f"ФИО - {self.name}\n"
              f"Предметная область - {self.subjectArea}\n"
              f"Количество проверок - {self.numberOfRate}\n"
              f"Доступ к 3 проверке - {self.accessToAdditionalVerification}\n"
              f"Количество заданий: {len(self.tasks)}\n"
              )
