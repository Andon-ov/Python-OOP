from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        # hardware_obj = found_hardware(hardware_name)
        hardware_obj = [x for x in System._hardware if x.name == hardware_name][0]
        if hardware_obj is None:
            return "Hardware does not exist"

        software_obj = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware_obj.install(software_obj)
        System._software.append(software_obj)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware_obj = [x for x in System._hardware if x.name == hardware_name][0]
        if hardware_obj is None:
            return "Hardware does not exist"

        software_obj = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware_obj.install(software_obj)
        System._software.append(software_obj)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        software_obj = [x for x in System._software if x.name == software_name][0]
        hardware_obj = [x for x in System._hardware if x.name == hardware_name][0]
        if hardware_obj is None or software_obj is None:
            return "Some of the components do not exist"

        hardware_obj.uninstall(software_obj)
        System._software.remove(software_obj)

    @staticmethod
    def analyze():
        result = 'System Analysis' + '\n'
        result += f'Hardware Components: {len(System._hardware)}' + '\n'
        result += f'Software Components: {len(System._software)}' + '\n'
        result += f'Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / {sum([x.memory for x in System._hardware])}' + '\n'
        result += f'Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / {sum([x.capacity for x in System._hardware])}' + '\n'
        return result.strip()

    # "System Analysis
    # Hardware Components: {number_of_hardware_components}
    # Software Components: {number_of_software_components}
    # Total Operational Memory: {total memory consumption for all registered software components} / {total memory for all registered hardware components}
    # Total Capacity Taken: {total capacity consumption for all registered software components} /{total capacity of all registered hardware components}"

    # System Analysis
    # Hardware Components: 2
    # Software Components: 5
    # Total Operational Memory: 455 / 650
    # Total Capacity Taken: 160 / 850

    @staticmethod
    def system_split():
        pass

    # Return the following information (as a string) for each hardware component:
    # "Hardware Component - {component name}
    # Express Software Components: {number of the installed express software components}
    # Light Software Components: {number of the installed light software components}
    # Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}
    # Capacity Usage: {total capacity used of all installed software components } / {total capacity of the hardware}
    # Type: {hardware_type}
    # Software Components: {names of all software components separated by ', '} (or 'None' if no software components)"

    # Hardware Component - HDD
    # Express Software Components: 1
    # Light Software Components: 1
    # Memory Usage: 205 / 350
    # Capacity Usage: 50 / 50
    # Type: Power
    # Software Components: Test, Test3
    # Hardware Component - SSD
    # Express Software Components: 0
    # Light Software Components: 2
    # Memory Usage: 50 / 300
    # Capacity Usage: 60 / 800
    # Type: Heavy
    # Software Components: Windows, Unix
