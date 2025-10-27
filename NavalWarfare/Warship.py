class Warship:
    def __init__(self, name: str, max_integrity: int, max_damage: int, min_damage_factor: float,
                acurrancy: int, max_speed: int, acceleration: int, desacceleration: int,
                ammo_storage: int, reload_time: int, bullets_per_shot: int, bullets_per_reload: int,
                repair: int, default_sprite: str, damaged_sprite: str = None, repaired_sprite: str = None):
        self.name = name
        self.max_integrity = max_integrity # (Lenght * Sleeve)/class_asc{+1.5}
        self.current_integrity = max_integrity
        self.max_damage = max_damage #((caliber_cannon{mm})*turret_cannons)
        self.min_damage_factor = min_damage_factor #1/turret_cannons
        self.min_damage = min(round(max_damage * max(0, min(1, min_damage_factor))), max_damage)
        self.acurrancy = acurrancy #Weapon_max_range{km}*class_asc{+1}
        self.max_speed = max_speed #(km/h)/class_asc{+0.5}
        self.current_speed = 0
        self.acceleration = acceleration #original_max-speed/(class_acs+3)
        self.desacceleration = desacceleration #acceleration/(class__decs{-0.5})
        self.ammo_storage = ammo_storage #total_cannons
        self.current_ammo = 0
        self.reload_time = reload_time #{real-life}/10
        self.current_reload = 0
        self.bullets_per_shot = bullets_per_shot #per_turret
        self.bullets_per_reload = bullets_per_reload
        self.repair = repair # (100*original_integrtity)/tripulation)/class_desc
        self.default_sprite = default_sprite
        self.damaged_sprite = damaged_sprite
        self.repaired_sprite = repaired_sprite

    def to_dict(self):
        return {
            "name": self.name,
            "max_integrity": self.max_integrity,
            "max_damage": self.max_damage,
            "min_damage_factor": self.min_damage_factor,
            "acurrancy": self.acurrancy,
            "max_speed": self.max_speed,
            "acceleration": self.acceleration,
            "desacceleration": self.desacceleration,
            "ammo_storage": self.ammo_storage,
            "reload_time": self.reload_time,
            "bullets_per_shot": self.bullets_per_shot,
            "bullets_per_reload": self.bullets_per_reload,
            "repair": self.repair,
            "default_sprite": self.default_sprite,
            "damaged_sprite": self.damaged_sprite,
            "repaired_sprite": self.repaired_sprite
        }

    def get_base_stats(self):
        printing = []
        printing.append(f"--- {self.name} ---\n")
        printing.append(f"Integridad: {self.max_integrity}\n")
        printing.append(f"Daño Máximo: {self.max_damage}\n")
        printing.append(f"Daño Mínimo: {self.min_damage}\n")
        printing.append(f"Precisión: {self.acurrancy}\n")
        printing.append(f"Velocidad: {self.max_speed}\n")
        printing.append(f"Aceleración: {self.acceleration}\n")
        printing.append(f"Desaceleración: {self.desacceleration}\n")
        printing.append(f"Munición: {self.ammo_storage}\n")
        printing.append(f"Tiempo de Recarga: {self.reload_time}\n")
        printing.append(f"Balas por Disparo: {self.bullets_per_shot}\n")
        printing.append(f"Balas por Recarga: {self.bullets_per_reload}\n")
        printing.append(f"Reparación por Turno: {self.repair}\n")
        return "".join(printing)
        
    def get_current_stats(self):
        printing = []
        printing.append(f"--- {self.name} ---\n")
        printing.append(f"Integridad: {self.current_integrity}/{self.max_integrity}\n")
        printing.append(f"Velocidad Actual: {self.current_speed}/{self.max_speed}\n")
        printing.append(f"Munición Actual: {self.current_ammo}/{self.ammo_storage}\n")
        printing.append(f"Recarga Actual: {self.current_reload}/{self.reload_time}\n")
        return "".join(printing)