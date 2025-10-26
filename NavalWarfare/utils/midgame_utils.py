import arcade
import random
from Actor import Actor

def desacelerate(actor: Actor):
    actor.warship.current_speed -= actor.warship.desacceleration
    if actor.warship.current_speed < 0:
        actor.warship.current_speed = 0

def attack(attacker: Actor, defender: Actor, enemy_sprite_list: arcade.SpriteList) :
    damage = random.randint(0, attacker.warship.max_damage)
    chance = attacker.warship.acurrancy / (attacker.warship.acurrancy + defender.warship.current_speed)
    roll = random.random()

    if roll <= chance:
        print("Acierta!")
        enemy_sprite_list[0].visible = False
        enemy_sprite_list[1].visible = True
        defender.warship.current_integrity -= damage
    else:
        print("Falla!")

def reset_ship_sprite_list(sprite_list: arcade.SpriteList):
    sprite_list[0].visible = True
    sprite_list[1].visible = False
    sprite_list[2].visible = False