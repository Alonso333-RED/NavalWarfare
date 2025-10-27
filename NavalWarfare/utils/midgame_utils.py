import arcade
import random
from Actor import Actor
from utils import storage_utils
from utils import midgame_utils

def desacelerate(actor: Actor):
    actor.warship.current_speed -= actor.warship.desacceleration
    if actor.warship.current_speed < 0:
        actor.warship.current_speed = 0

def attack(attacker: Actor, defender: Actor, defender_sprite_list: arcade.SpriteList, damage_multiplier: float):
    damage = random.randint(attacker.warship.min_damage, round(attacker.warship.max_damage * damage_multiplier))
    
    chance = attacker.warship.acurrancy / (attacker.warship.acurrancy + defender.warship.current_speed)
    roll = random.random()

    if roll <= chance:
        print("Acierta!")
        defender_sprite_list[0].visible = False
        defender_sprite_list[1].visible = True
        defender.warship.current_integrity -= damage
    else:
        print("Falla!")

    storage_utils.execute_sound("weapon_shoot.mp3")
    attacker.warship.current_ammo -= attacker.warship.bullets_per_shot
    midgame_utils.desacelerate(attacker)

def reload(actor: Actor):
    actor.warship.current_ammo += actor.warship.bullets_per_reload
    if actor.warship.current_ammo >= actor.warship.ammo_storage:
        actor.warship.current_ammo = actor.warship.ammo_storage
    storage_utils.execute_sound("weapon_reload.mp3")
    midgame_utils.desacelerate(actor)

def accelerate(actor: Actor):
    actor.warship.current_speed += actor.warship.acceleration
    if actor.warship.current_speed >= actor.warship.max_speed:   
        actor.warship.current_speed = actor.warship.max_speed
    storage_utils.execute_sound("acceleration.mp3")

def repair(actor: Actor, actor_sprite_list: arcade.SpriteList):
    actor.warship.current_integrity += random.randint(0, actor.warship.repair)
    if actor.warship.current_integrity >= actor.warship.max_integrity:
        actor.warship.current_integrity = actor.warship.max_integrity
    storage_utils.execute_sound("repair.mp3")
    actor_sprite_list[0].visible = False
    actor_sprite_list[2].visible = True
    midgame_utils.desacelerate(actor)

def reset_ship_sprite_list(sprite_list: arcade.SpriteList):
    sprite_list[0].visible = True
    sprite_list[1].visible = False
    sprite_list[2].visible = False

import random

def roll_damage_opportunity():
    roll = random.random()

    if roll < (1/16): 
        return random.uniform(1, 2)
    elif roll < (1/8):
        return random.uniform(1, 1.5)
    elif roll < (1/4):
        return random.uniform(1, 1.25)
    else:
        return random.uniform(1, 1)

        