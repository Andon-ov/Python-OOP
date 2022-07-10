class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        pass
        # – it should create a new instance using the provided data. The date will be in format "day.month.year" - all of them numbers.

    def __repr__(self):
        result = 'rented' if self.is_rented else 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {result}"

















# from project.mapper import mapper
#
#
# class DVD:
#     def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
#         self.name = name
#         self.id = id
#         self.creation_year = creation_year
#         self.creation_month = creation_month
#         self.age_restriction = age_restriction
#         self.is_rented = False
#
#     @classmethod
#     def from_date(cls, id: int, name: str, date: str, age_restriction: int):
#         _, month, year = [int(x) for x in date.split(".")]
#         month_name = mapper[month]
#         return cls(name, id, year, month_name, age_restriction)
#
#     def __repr__(self):
#         status = "rented" if self.is_rented else "not rented"
#         return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}"
