from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
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
        hardware = System.found_hardware(hardware_name)

        if hardware is None:
            return "Hardware does not exist"
        try:
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except Exception:
            raise Exception("Software cannot be installed")

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.found_hardware(hardware_name)

        if hardware is None:
            return "Hardware does not exist"
        try:
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except Exception:
            raise Exception("Software cannot be installed")

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.found_hardware(hardware_name)
        software = System.found_software(software_name)
        if software is None or hardware is None:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        result = 'System Analysis' + '\n'
        result += f'Hardware Components: {len(System._hardware)}' + '\n'
        result += f'Software Components: {len(System._software)}' + '\n'
        result += f'Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / {sum([x.memory for x in System._hardware])}' + '\n'
        result += f'Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / {sum([x.capacity for x in System._hardware])}' + '\n'
        return result.strip()

    @staticmethod
    def system_split():
        hardware_result = ''
        for hardware in System._hardware:
            hardware_result += f'Hardware Component - {hardware.name}' + '\n'
            express_software = sum(
                [1 for software in hardware.software_components if software.software_type == "Express"])
            light_software = sum([1 for software in hardware.software_components if software.software_type == "Light"])
            hardware_result += f'Express Software Components: {express_software}' + '\n'
            hardware_result += f'Light Software Components: {light_software}' + '\n'
            hardware_result += f'Memory Usage: {sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}' + '\n'
            hardware_result += f'Capacity Usage: {sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}' + '\n'
            hardware_result += f'Type: {hardware.hardware_type}' + '\n'
            names_software_components = [software.name for software in hardware.software_components]
            software_names = ', '.join([x for x in names_software_components]) if len(
                names_software_components) > 0 else 'None'
            hardware_result += f'Software Components: {software_names}' + '\n'

        return hardware_result

    @staticmethod
    def found_hardware(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware
        return None

    @staticmethod
    def found_software(software_name):
        for software in System._software:
            if software.name == software_name:
                return software
        return None



# class System:
#     _hardware: list = []
#     # empty list that will be storing all the hardware components
#     _software: list = []
#
#     # empty list that will be storing all the software components
#
#     @staticmethod
#     def register_power_hardware(name: str, capacity: int, memory: int):
#         power_hardware = PowerHardware(name, capacity, memory)
#         System._hardware.append(power_hardware)
#         # Create a PowerHardware instance and add it to the hardware list
#
#     @staticmethod
#     def register_heavy_hardware(name: str, capacity: int, memory: int):
#         heavy_hardware = HeavyHardware(name, capacity, memory)
#         System._hardware.append(heavy_hardware)
#
#     @staticmethod
#     def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
#         hardware = System.found_hardware(hardware_name)
#         if hardware is None:
#             return "Hardware does not exist"
#
#         software = ExpressSoftware(name, capacity_consumption, memory_consumption)
#         hardware.install(software)
#         System._software.append(software)
#
#     @staticmethod
#     def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
#         hardware = System.found_hardware(hardware_name)
#         if hardware is None:
#             return "Hardware does not exist"
#
#         software = LightSoftware(name, capacity_consumption, memory_consumption)
#         hardware.install(software)
#         System._software.append(software)
#
#     @staticmethod
#     def release_software_component(hardware_name: str, software_name: str):
#
#         hardware = System.found_hardware(hardware_name)
#         software = System.found_software(software_name)
#         if hardware is None or software is None:
#             return "Some of the components do not exist"
#
#         hardware.uninstall(software)
#         System._software.remove(software)
#
#
#     @staticmethod
#     def analyze():
#         result = 'System Analysis\n'
#         # for hardware in System._hardware:
#         result += f'Hardware Components: {len(System._hardware)}\n'
#         result += f'Software Components: {len(System._software)}\n'
#         result += f'Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / {sum([x.memory for x in System._hardware])}\n'
#         result += f'Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / {sum([x.capacity for x in System._hardware])}\n'
#         return result.strip()
#
#     @staticmethod
#     def system_split():
#         result = ''
#         for hardware in System._hardware:
#             all_software = []
#             for software in hardware.software_components:
#                 all_software.append(software)
#             software_result = None if len(all_software) == 0 else ', '.join([x.name for x in all_software])
#
#             result += f'Hardware Component - {hardware.name}\n'
#             result += f'Express Software Components: {sum([1 for x in hardware.software_components if x.software_type == "Express"])}\n'
#             result += f'Light Software Components: {sum([1 for x in hardware.software_components if x.software_type == "Light"])}\n'
#             result += f'Memory Usage: {sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}\n'
#             result += f'Capacity Usage: {sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}\n'
#             result += f'Type: {hardware.hardware_type}\n'
#             result += f'Software Components: {software_result}\n'
#         return result.strip()
#
#     @staticmethod
#     def found_hardware(hardware_name):
#         for hardware in System._hardware:
#             if hardware.name == hardware_name:
#                 return hardware
#
#         return None
#
#     @staticmethod
#     def found_software(software_name):
#         for software in System._software:
#             if software.name == software_name:
#                 return software
#
#         return None