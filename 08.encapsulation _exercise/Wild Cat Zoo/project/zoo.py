class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []


    #     • Public attribute name: str
    #     • Private attribute budget: int
    #     • Private attribute animal_capacity: int
    #     • Private attribute workers_capacity: int

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for i in self.workers:
            if i.name == worker_name:
                self.workers.remove(i)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_sum = 0
        for i in self.workers:
            salary_sum += i.salary
        if salary_sum > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= salary_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        take_care_sum = 0
        for i in self.animals:
            take_care_sum += i.money_for_care
        if take_care_sum > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= take_care_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion = []
        tiger = []
        cheetah = []
        for i in self.animals:
            if i.__class__.__name__ == 'Lion':
                lion.append(i)
            if i.__class__.__name__ == 'Tiger':
                tiger.append(i)
            if i.__class__.__name__ == 'Cheetah':
                cheetah.append(i)

        result = f'You have {len(self.animals)} animals' + '\n'
        result += f'----- {len(lion)} Lions:' + '\n'
        for l in lion:
            result += f'{l}' + '\n'
        result += f'----- {len(tiger)} Tigers:' + '\n'
        for t in tiger:
            result += f'{t}' + '\n'
        result += f'----- {len(cheetah)} Cheetahs:' + '\n'
        for c in cheetah:
            result += f'{c}' + '\n'
        return result.strip()

    def workers_status(self):

        keepers = []
        caretakers = []
        vets = []
        for i in self.workers:
            if i.__class__.__name__ == 'Keeper':
                keepers.append(i)
            if i.__class__.__name__ == 'Caretaker':
                caretakers.append(i)
            if i.__class__.__name__ == 'Vet':
                vets.append(i)

        result = f'You have {len(self.workers)} workers' + '\n'
        result += f'----- {len(keepers)} Keepers:' + '\n'
        for k in keepers:
            result += f'{k}' + '\n'
        result += f'----- {len(caretakers)} Caretakers:' + '\n'
        for c in caretakers:
            result += f'{c}' + '\n'
        result += f'----- {len(vets)} Vets:' + '\n'
        for v in vets:
            result += f'{v}' + '\n'
        return result.strip()



# from project.animal import Animal
# from project.worker import Worker
#
#
# class Zoo:
#
#     def __init__(self, name, budget, animal_capacity, workers_capacity):
#         self.name = name
#         self.__budget = budget
#         self.__animal_capacity = animal_capacity
#         self.__workers_capacity = workers_capacity
#         self.animals = []
#         self.workers = []
#
#     def add_animal(self, animal, price):
#         if self.__animal_capacity == len(self.animals):
#             return "Not enough space for animal"
#         elif self.__budget < price:
#             return "Not enough budget"
#         self.animals.append(animal)
#         self.__budget -= price
#         return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
#
#     def hire_worker(self, worker):
#         if not self.__workers_capacity == len(self.workers):
#             self.workers.append(worker)
#             return f"{worker.name} the {worker.__class__.__name__} hired successfully"
#         else:
#             return "Not enough space for worker"
#
#     def fire_worker(self, worker_name):
#         for worker in self.workers:
#             if worker.name == worker_name:
#                 self.workers.remove(worker)
#                 return f"{worker_name} fired successfully"
#
#         return f"There is no {worker_name} in the zoo"
#
#     def pay_workers(self):
#         salaries = 0
#         for worker in self.workers:
#             salaries += worker.salary
#         if self.__budget >= salaries:
#             self.__budget -= salaries
#             return f"You payed your workers. They are happy. Budget left: {self.__budget}"
#         return "You have no budget to pay your workers. They are unhappy"
#
#     def tend_animals(self):
#         take_care = 0
#         for animal in self.animals:
#             take_care += animal.money_for_care
#         if self.__budget >= take_care:
#             self.__budget -= take_care
#             return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
#         return "You have no budget to tend the animals. They are unhappy."
#
#     def profit(self, amount):
#         self.__budget += amount
#
#     def animals_status(self):
#         data = f"You have {len(self.animals)} animals\n"
#         data += self.__get_animal_status_by_type("Lion")
#         data += self.__get_animal_status_by_type("Tiger")
#         data += self.__get_animal_status_by_type("Cheetah")
#
#         return data.strip()
#
#     def __get_animal_status_by_type(self, animal_type):
#         animals = [str(x) for x in self.animals if x.__class__.__name__ == animal_type]
#
#         data = f"----- {len(animals)} {animal_type}s:\n"
#         for animal in animals:
#             data += animal
#             data += "\n"
#
#         return data
#
#     def workers_status(self):
#         data = f"You have {len(self.workers)} workers\n"
#         data += self.__get_worker_status_by_type("Keeper")
#         data += self.__get_worker_status_by_type("Caretaker")
#         data += self.__get_worker_status_by_type("Vet")
#
#         return data.strip()
#
#     def __get_worker_status_by_type(self, worker_type):
#         workers = [str(x) for x in self.workers if x.__class__.__name__ == worker_type]
#
#         data = f"----- {len(workers)} {worker_type}s:\n"
#         for worker in workers:
#             data += worker
#             data += "\n"
#
#         return data
#
#
