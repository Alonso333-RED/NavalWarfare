class Battleship:
    def __init__(self, name: str, max_integrity: int, armor: int, max_damage: int,
                 min_damage_factor: float, penetration: int, acurrancy: int,
                 max_speed: int, acelleration: float, desacelleration: float,
                 ammo_storage: int, reload: int, repair: float):
        self.name = name
        self.max_integrity = max_integrity
        self.current_integrity = max_integrity
        self.armor = armor
        self.max_damage = max_damage
        self.min_damage_factor = min_damage_factor
        self.penetration = penetration
        self.acurrancy = acurrancy
        self.max_speed = max_speed
        self.current_speed = max_speed
        self.acelleration = acelleration
        self.desacelleration = desacelleration
        self.ammo_storage = ammo_storage
        self.current_ammo = 0
        self.reload = reload
        self.repair = repair
        
    def get_stats(self):
        printing = []
        printing.append(f"--- {self.name} ---\n")
        printing.append(f"Integridad: {self.current_integrity}/{self.max_integrity}\n")
        printing.append(f"Armadura: {self.armor}\n")
        printing.append(f"Daño máximo: {self.max_damage}\n")
        printing.append(f"Daño mínimo: {int(self.max_damage * self.min_damage_factor)}\n")
        printing.append(f"Penetración: {self.penetration}\n")
        printing.append(f"Precisión: {self.acurrancy}\n")
        printing.append(f"Velocidad máxima: {self.max_speed}\n")
        printing.append(f"Aceleración: {self.acelleration}\n")
        printing.append(f"Desaceleración: {self.desacelleration}\n")
        printing.append(f"Munición: {self.ammo_storage}\n")
        printing.append(f"Recarga: {self.reload}\n")
        printing.append(f"Capacidad de reparación: {self.repair}\n")
        return "".join(printing)
        
    def get_state(self):
        printing = []
        printing.append(f"--- {self.name} ---\n")
        printing.append(f"Integridad: {self.current_integrity}/{self.max_integrity}\n")
        printing.append(f"Velocidad: {self.current_speed}/{self.max_speed}\n")
        printing.append(f"Munición: {self.current_ammo}/{self.ammo_storage}\n")
        return "".join(printing)