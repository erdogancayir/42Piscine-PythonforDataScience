from S1E9 import Character

class Baratheon(Character):
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
    def die(self):
        self.is_alive = False
    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    Representing the Lannister family.
    """
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
    
    def die(self):
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
