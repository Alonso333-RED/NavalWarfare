class Battleship:
    def __init__(self, name: str, max_integrity: int, max_damage: int, acurrancy: float,
                max_speed: int, acelleration: int, desacelleration: int, ammo_storage: int,
                reload_time: int, bullets_per_shot: int, bullets_per_reload: int, repair: int, 
                default_sprite: str, damaged_sprite: str, repaired_sprite: str):
        self.name = name
        self.max_integrity = max_integrity
        self.current_integrity = max_integrity
        self.max_damage = max_damage
        self.acurrancy = acurrancy
        self.max_speed = max_speed
        self.current_speed = 0
        self.acelleration = acelleration
        self.desacelleration = desacelleration
        self.ammo_storage = ammo_storage
        self.current_ammo = 0
        self.reload_time = reload_time
        self.current_reload = 0
        self.bullets_per_shot = bullets_per_shot
        self.bullets_per_reload = bullets_per_reload
        self.repair = repair
        self.default_sprite = default_sprite
        self.damaged_sprite = damaged_sprite
        self.repaired_sprite = repaired_sprite
        
    def get_stats(self):
        printing = []
        printing.append(f"--- {self.name} ---\n")
        printing.append(f"Integridad: {self.current_integrity}/{self.max_integrity}\n")
        printing.append(f"Daño Máximo: {self.max_damage}\n")
        printing.append(f"Precisión: {self.acurrancy*100}%\n")
        printing.append(f"Velocidad: {self.current_speed}/{self.max_speed}\n")
        printing.append(f"Aceleración: {self.acelleration}\n")
        printing.append(f"Desaceleración: {self.desacelleration}\n")
        printing.append(f"Munición: {self.current_ammo}/{self.ammo_storage}\n")
        printing.append(f"Recarga: {self.current_reload}/{self.reload_time}\n")
        printing.append(f"Balas por Disparo: {self.bullets_per_shot}\n")
        printing.append(f"Balas por Recarga: {self.bullets_per_reload}\n")
        printing.append(f"Reparación por Turno: {self.repair}\n")
        return "".join(printing)
        
    def get_state(self):
        printing = []
        printing.append(f"--- {self.name} ---\n")
        printing.append(f"Integridad: {self.current_integrity}/{self.max_integrity}\n")
        printing.append(f"Velocidad: {self.current_speed}/{self.max_speed}\n")
        printing.append(f"Munición: {self.current_ammo}/{self.ammo_storage}\n")
        return "".join(printing)