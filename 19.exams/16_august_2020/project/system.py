class System:
    def __init__(self):

        self._hardware = []
        self._software = []

        # _hardware - an empty list that will be storing all the hardware components
        # _software - an empty list that will be storing all the software components

# All described methods below should be static!
# register_power_hardware(name: str, capacity: int, memory: int)
# Create a PowerHardware instance and add it to the hardware list
# register_heavy_hardware(name: str, capacity: int, memory: int)
# Create a HeavyHardware instance and add it to the hardware list
# register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int)
# If the hardware with the given name does NOT exist, return the message "Hardware does not exist"
# Otherwise, create an express software, install it on the hardware, and add it to the software list
# If the installation is not possible, raise Exception with the message "Software cannot be installed"
# register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int)
# If the hardware with the given name does NOT exist, return a message "Hardware does not exist"
# Otherwise, create a light software instance, install it on the hardware, and add it to the software list
# If the installation is not possible, raise Exception with the message "Software cannot be installed"
# release_software_component(hardware_name: str, software_name: str)
# If both components exist on the system, uninstall the software from the given hardware, and remove it from the software list
# Otherwise, return a message "Some of the components do not exist"
# analyze()
# Return the following information (as a string) for the total memory and capacity used (calculated for all hardware components in the system):
# "System Analysis
# Hardware Components: {number_of_hardware_components}
# Software Components: {number_of_software_components}
# Total Operational Memory: {total memory consumption for all registered software components} / {total memory for all registered hardware components}
# Total Capacity Taken: {total capacity consumption for all registered software components} / {total capacity of all registered hardware components}"
# system_split()
# Return the following information (as a string) for each hardware component:
# "Hardware Component - {component name}
# Express Software Components: {number of the installed express software components}
# Light Software Components: {number of the installed light software components}
# Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}
# Capacity Usage: {total capacity used of all installed software components } / {total capacity of the hardware}
# Type: {hardware_type}
# Software Components: {names of all software components separated by ', '} (or 'None' if no software components)"