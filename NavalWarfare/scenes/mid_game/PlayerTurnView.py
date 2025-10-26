import random
import arcade
from arcade.gui import UIManager
import config
from Actor import Actor
from utils import storage_utils
from utils import midgame_utils
from utils import debug_utils

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION


class PlayerTurnView(arcade.View):
    def __init__(self, player: Actor, enemy: Actor, background: arcade.Sprite, bg_color: tuple = (26, 26, 64)):
        super().__init__()
        self.background_color = bg_color
        self.uimanager = UIManager()
        self.uimanager.enable()
        self.v_box = arcade.gui.UIBoxLayout(space_between=0)
        self.player = player
        self.enemy = enemy
        self.background = background
        self.timer = 0
        self.waiting_for_enemy = False

        self.bg_sprite_list = arcade.SpriteList()
        self.background.center_x = (WINDOW_WIDTH / 2)
        self.background.center_y = (WINDOW_HEIGHT / 2)
        self.background.scale = 1.25
        self.bg_sprite_list.append(self.background)

        self.player_sprite_list = self.player.load_sprite_list()
        self.enemy_sprite_list = self.enemy.load_sprite_list()

        #Botones
        btn_atacar = arcade.gui.UIFlatButton(text="Atacar", width=70, height=70)
        btn_atacar.on_click = self.on_click_atacar
        self.v_box.add(btn_atacar)

        btn_recargar = arcade.gui.UIFlatButton(text="Recargar", width=70, height=70)
        btn_recargar.on_click = self.on_click_recargar
        self.v_box.add(btn_recargar)

        btn_acelerar = arcade.gui.UIFlatButton(text="Acelerar", width=70, height=70)
        btn_acelerar.on_click = self.on_click_acelerar
        self.v_box.add(btn_acelerar)

        btn_reparar = arcade.gui.UIFlatButton(text="Reparar", width=70, height=70)
        btn_reparar.on_click = self.on_click_reparar
        self.v_box.add(btn_reparar)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.anchor_layout.add(
            child=self.v_box,
            anchor_x="center_x",
            anchor_y="center_y",
            align_y = -75,
            align_x = -325
        )
        self.uimanager.add(self.anchor_layout)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.bg_sprite_list.draw()
        self.player_sprite_list.draw()
        self.enemy_sprite_list.draw()
        self.uimanager.draw()

    def on_update(self, delta_time):
        if self.waiting_for_enemy:
            self.timer += delta_time
            if self.timer >= 1.0:
                self.waiting_for_enemy = False
                self.timer = 0
                midgame_utils.reset_ship_sprite_list(self.player_sprite_list)
                midgame_utils.reset_ship_sprite_list(self.enemy_sprite_list)

    def on_click_atacar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: atacar_btn")
        if self.waiting_for_enemy:
            print("Rejected for enemy")
            return
        if (self.player.warship.current_ammo < self.player.warship.bullets_per_shot):
            storage_utils.execute_sound("weapon_empty.mp3")
            debug_utils.print_warship_current_state(self.player.warship)
            return
        storage_utils.execute_sound("weapon_shoot.mp3")
        self.player.warship.current_ammo -= self.player.warship.bullets_per_shot
        midgame_utils.desacelerate(self.player)
        debug_utils.print_warship_current_state(self.player.warship)  
        midgame_utils.attack(self.player, self.enemy, self.enemy_sprite_list)
        debug_utils.print_warship_current_state(self.enemy.warship)  
        self.waiting_for_enemy = True
        self.timer = 0

    def on_click_recargar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: recargar_btn")
        if self.waiting_for_enemy:
            print("Rejected for enemy")
            return
        if self.player.warship.current_ammo >= self.player.warship.ammo_storage:
            self.player.warship.current_ammo = self.player.warship.ammo_storage
            storage_utils.execute_sound("button_sound1.mp3")
            debug_utils.print_warship_current_state(self.player.warship)
            return
        self.player.warship.current_ammo += self.player.warship.bullets_per_reload
        if self.player.warship.current_ammo >= self.player.warship.ammo_storage:
            self.player.warship.current_ammo = self.player.warship.ammo_storage
        storage_utils.execute_sound("weapon_reload.mp3")
        midgame_utils.desacelerate(self.player)
        debug_utils.substract_integrity(self.player.warship)
        debug_utils.print_warship_current_state(self.player.warship)
        self.waiting_for_enemy = True
        self.timer = 0

    def on_click_acelerar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: acelerar_btn")
        if self.waiting_for_enemy:
            print("Rejected for enemy")
            return
        if self.player.warship.current_speed == self.player.warship.max_speed:
            storage_utils.execute_sound("button_sound1.mp3")
            debug_utils.print_warship_current_state(self.player.warship)
            return
        self.player.warship.current_speed += self.player.warship.acceleration
        if self.player.warship.current_speed >= self.player.warship.max_speed:
            self.player.warship.current_speed = self.player.warship.max_speed
        storage_utils.execute_sound("acceleration.mp3")
        debug_utils.print_warship_current_state(self.player.warship)
        self.waiting_for_enemy = True
        self.timer = 0

    def on_click_reparar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: reparar_btn")
        if self.waiting_for_enemy:
            print("Rejected for enemy")
            return
        if self.player.warship.current_integrity == self.player.warship.max_integrity:
            storage_utils.execute_sound("button_sound1.mp3")
            debug_utils.print_warship_current_state(self.player.warship)
            return
        self.player.warship.current_integrity += random.randint(0, self.player.warship.repair)
        if self.player.warship.current_integrity >= self.player.warship.max_integrity:
            self.player.warship.current_integrity = self.player.warship.max_integrity
        storage_utils.execute_sound("repair.mp3")
        self.player_sprite_list[0].visible = False
        self.player_sprite_list[2].visible = True
        debug_utils.print_warship_current_state(self.player.warship)
        self.waiting_for_enemy = True
        self.timer = 0
        
