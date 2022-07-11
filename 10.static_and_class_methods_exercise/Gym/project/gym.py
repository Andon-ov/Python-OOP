from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        result = ''
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:

                result += repr(subscription)
                result += '\n'
                result += repr(*[x for x in self.customers if x.id == subscription_id])
                result += '\n'
                result += repr(*[x for x in self.trainers if x.id == subscription_id])
                result += '\n'
                result += repr(*[x for x in self.equipment if x.id == subscription_id])
                result += '\n'
                result += repr(*[x for x in self.plans if x.id == subscription_id])
        return result


        # '''
        # Subscription <1> on 14.05.2020
        # Customer <1> John; Address: Maple Street; Email: john.smith@gmail.com
        # Trainer <1> Peter
        # Equipment <1> Treadmill
        # Plan <1> with duration 20 minutes
        # '''

        # – get the subscription, the customer and trainer, the plan and the equipment.
        # Then return their string representations each on a new line.
