# Upon initialization the class will not receive any parameters. However, it should have the following attributes: customers (list of customer objects, empty upon initialization), trainers (list of trainer objects, empty upon initialization), equipment (list of equipment objects, empty upon initialization), plans (list of plan objects, empty upon initialization), subscriptions (list of subscription objects, empty upon initialization)
# Create the following methods:
#     • add_customer(customer: Customer) – add the customer in the customer list, if the customer is not already in it
#     • add_trainer(trainer: Trainer) – add the trainer to the trainers list, if the trainer is not already in it
#     • add_equipment(equipment: Equipment) – add the equipment to the equipment list, if the equipment is not already in it
#     • add_plan(plan: ExercisePlan) – add the plan to the plans list, if the plan is not already in it
#     • add_subscription(subscription: Subscription) – add the subscription in the subscriptions list, if the subscription is not already in it
#     • subscription_info(subscription_id: int) – get the subscription, the customer and trainer, the plan and the equipment. Then return their string representations each on a new line.
# Examples