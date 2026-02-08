class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def heal(self, amount):
        self.health += amount

    
guts = Hero("Guts", 100)

# print(f"DEBUG: Name = {guts.name}")
print(f"DEBUG: Health = {guts.health}")
guts.take_damage(100)
print(f"DEBUG: Health = {guts.health}")
guts.heal(56)
print(f"DEBUG: Health = {guts.health}")
print(f"DEBUG: Is alive? = {guts.is_alive()}")