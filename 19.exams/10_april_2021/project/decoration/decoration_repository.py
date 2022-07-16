class DecorationRepository:
    def __init__(self):
        self.decorations = []

    # decorations: list – empty list that will contain all decorations (objects).

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for d in self.decorations:
            if d.type == decoration_type:
                return d

        return None
# Returns the first decoration of the given type if there is. Otherwise, returns a message "None".
