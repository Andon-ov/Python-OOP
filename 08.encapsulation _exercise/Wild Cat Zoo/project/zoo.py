from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if not self.__workers_capacity == len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        take_care = 0
        for animal in self.animals:
            take_care += animal.money_for_care
        if self.__budget >= take_care:
            self.__budget -= take_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        data = f"You have {len(self.animals)} animals\n"
        data += self.__get_animal_status_by_type("Lion")
        data += self.__get_animal_status_by_type("Tiger")
        data += self.__get_animal_status_by_type("Cheetah")

        return data.strip()

    def __get_animal_status_by_type(self, animal_type):
        animals = [str(x) for x in self.animals if x.__class__.__name__ == animal_type]

        data = f"----- {len(animals)} {animal_type}s:\n"
        for animal in animals:
            data += animal
            data += "\n"

        return data

    def workers_status(self):
        data = f"You have {len(self.workers)} workers\n"
        data += self.__get_worker_status_by_type("Keeper")
        data += self.__get_worker_status_by_type("Caretaker")
        data += self.__get_worker_status_by_type("Vet")

        return data.strip()

    def __get_worker_status_by_type(self, worker_type):
        workers = [str(x) for x in self.workers if x.__class__.__name__ == worker_type]

        data = f"----- {len(workers)} {worker_type}s:\n"
        for worker in workers:
            data += worker
            data += "\n"

        return data


"""

…
    • Hint: use the __repr__ methods of the animals to print them on the console
workers_status()
    • Returns the following string:
You have {total_workers_count} workers
----- {amount_of_keepers} Keepers:
{keeper1}
…
----- {amount_of_caretakers} Caretakers:
{caretaker1}
…
----- {amount_of_vetes} Vets:
{vet1}
…
    • Hint: use the __repr__ methods of the workers to print them on the console"""
