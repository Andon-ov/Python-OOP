from project.software.software import Software
from typing import List


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        if software.capacity_consumption > self.available_capacity or software.memory_consumption > self.available_memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    # If there is enough capacity and memory, add the software object to the software components.
    # Otherwise, raise Exception with the message "Software cannot be installed"

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def available_capacity(self):
        return self.capacity - sum([x.capacity_consumption for x in self.software_components])

    @property
    def available_memory(self):
        return self.memory - sum([x.memory_consumption for x in self.software_components])
