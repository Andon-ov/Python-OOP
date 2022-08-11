import abc


class BaseDecoration(abc.ABC):
    @abc.abstractmethod
    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price


# from abc import ABC, abstractmethod
#
#
# class BaseDecoration(ABC):
#     @abstractmethod
#     def __init__(self, comfort: int, price: float):
#         self.comfort = comfort
#         self.price = price
