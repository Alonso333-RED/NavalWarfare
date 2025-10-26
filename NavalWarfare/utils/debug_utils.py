import random
from Warship import Warship
def print_warship_current_state(warship: Warship):
        print(f"Integrity {warship.current_integrity}/{warship.max_integrity}")
        print(f"Ammo: {warship.current_ammo}/{warship.ammo_storage}")
        print(f"Speed: {warship.current_speed}/{warship.max_speed}")

def substract_integrity(warship: Warship, randomize: bool = True, factor: float = 0):
        damage = 0
        if randomize:
                damage = random.randint(0, warship.current_integrity)
        elif not randomize:
                damage = round(warship.max_integrity * factor)
        before_integrity = warship.current_integrity
        warship.current_integrity -= damage
        print(f"Damage: {damage} ---> {before_integrity}->{warship.current_integrity}/{warship.max_integrity}")