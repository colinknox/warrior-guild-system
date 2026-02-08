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

class Warrior(Hero):
    def __init__(self, name, health, stamina):
        super().__init__(name, health)
        self.__stamina = stamina

    def power_attack(self, target):
        if self.__stamina >= 20:
            self.__stamina -= 20
            target.take_damage(30)
        else:
            raise Exception("Not enough stamina")

    def get_stamina(self):
        return self.__stamina
    
    def rest(self):
        self.__stamina += 10

class EliteWarrior(Warrior):
    def __init__(self, name, health, stamina):
        super().__init__(name, health, stamina)
        self.__num_victories = 0

    def power_attack(self, target):
        super().power_attack(target)

        if target.is_alive() == False:
            self.__num_victories += 1

    def get_num_victories(self):
        return self.__num_victories

    def is_veteran(self):
        if self.__num_victories >= 5:
            return True
        else:
            return False

class Mage(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana



guts = Hero("Guts", 31)
optimus = Warrior("Optimus", 500, 100)
bruce_lee = EliteWarrior("Bruce Lee", 50, 100)

print(f"DEBUG: Number of victories = {bruce_lee.get_num_victories()}")
bruce_lee.power_attack(guts)
print(f"DEBUG: Number of victories = {bruce_lee.get_num_victories()}")
print(f"DEBUG: Is veteran = {bruce_lee.is_veteran()}")