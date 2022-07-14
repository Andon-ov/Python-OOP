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

        # Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}
        # Capacity Usage: {total capacity used of all installed software components } / {total capacity of the hardware}

        # Memory Usage: 205 / 350
        # Capacity Usage: 50 / 50
