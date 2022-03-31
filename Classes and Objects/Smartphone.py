class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def install(self, app, app_memory):

        if app_memory <= self.memory and self.is_on:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"

        if app_memory <= self.memory and self.is_on is False:
            return f"Turn on your phone to install {app}"

        else:
            return f"Not enough memory to install {app}"

    def power(self):
        self.is_on = not self.is_on

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


"""


        ◦ If there is enough memory on the phone and it is on, install the app (add it to apps and decrease the memory of the phone) and return "Installing {app}"
        ◦ If there is enough memory, but the phone is off, return "Turn on your phone to install {app}"
        ◦ Otherwise return "Not enough memory to install {app}"
"""

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
