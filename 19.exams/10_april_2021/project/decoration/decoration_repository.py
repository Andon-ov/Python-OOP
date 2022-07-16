from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    # decorations: list – empty list that will contain all decorations (objects).

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        for d in self.decorations:
            if d.__class__.__name__ == decoration_type:
                return d
        return None
# Returns the first decoration of the given type if there is. Otherwise, returns a message "None".
