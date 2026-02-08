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



guts = Hero("Guts", 100)
optimus = Warrior("Optimus", 500, 100)

