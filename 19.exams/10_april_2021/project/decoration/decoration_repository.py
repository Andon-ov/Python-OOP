from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False

        self.decorations.remove(decoration)
        return True

        # return decoration in self.decorations

        # • Removes the decoration object from the list
        # if it exists and returns True, otherwise returns False.

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

        return "None"

        # • Returns the first decoration of the given type if there is.
        # Otherwise, returns a message "None".
