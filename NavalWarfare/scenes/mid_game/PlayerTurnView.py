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
        self.player_damage_opportunity = round(midgame_utils.roll_damage_opportunity(), 2)
        self.enemy_damage_opportunity = round(midgame_utils.roll_damage_opportunity(), 2)

        self.bg_sprite_list = arcade.SpriteList()
        self.background.center_x = (WINDOW_WIDTH / 2)
        self.background.center_y = (WINDOW_HEIGHT / 2)
        self.background.scale = 1.25
        self.bg_sprite_list.append(self.background)

        self.player_sprite_list = self.player.load_sprite_list()
        self.enemy_sprite_list = self.enemy.load_sprite_list()

        storage_utils.execute_sound("dirty_siren.mp3")

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

        # Textos
        self.player_damage_opportunity_text = arcade.Text(
            f"{self.player_damage_opportunity}",
        (WINDOW_WIDTH / 2)-135, (WINDOW_HEIGHT / 2)+30,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        self.player_ammo_text = arcade.Text(
            f"{self.player.warship.current_ammo}/{self.player.warship.ammo_storage}",
        (WINDOW_WIDTH / 2)-135, (WINDOW_HEIGHT / 2)-40,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        self.player_speed_text = arcade.Text(
            f"{self.player.warship.current_speed}/{self.player.warship.max_speed}",
        (WINDOW_WIDTH / 2)-135, (WINDOW_HEIGHT / 2)-110,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        self.player_integrity_text = arcade.Text(
            f"{self.player.warship.current_integrity}/{self.player.warship.max_integrity}",
        (WINDOW_WIDTH / 2)-135, (WINDOW_HEIGHT / 2)-180,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        self.enemy_damage_opportunity_text = arcade.Text(
            f"{self.enemy_damage_opportunity}",
        (WINDOW_WIDTH / 2)+435, (WINDOW_HEIGHT / 2) + 200,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        self.enemy_ammo_text = arcade.Text(
            f"{self.enemy.warship.current_ammo}/{self.enemy.warship.ammo_storage}",
        (WINDOW_WIDTH / 2+435), (WINDOW_HEIGHT / 2)+175,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        self.enemy_speed_text = arcade.Text(
            f"{self.enemy.warship.current_speed}/{self.enemy.warship.max_speed}",
        (WINDOW_WIDTH / 2+435), (WINDOW_HEIGHT / 2)+150,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        self.enemy_integrity_text = arcade.Text(
            f"{self.enemy.warship.current_integrity}/{self.enemy.warship.max_integrity}",
        (WINDOW_WIDTH / 2+435), (WINDOW_HEIGHT / 2)+125,
        color=arcade.color.WHITE,
        font_size=12,
        anchor_x="center",
        anchor_y="center",
        multiline=True,
        width=300 
        )

        #self.player.warship.current_integrity = 1

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.bg_sprite_list.draw()
        self.player_sprite_list.draw()
        self.enemy_sprite_list.draw()
        self.uimanager.draw()
        self.draw_hud()

    def on_update(self, delta_time):
        if self.waiting_for_enemy:
            self.timer += delta_time
            if self.timer >= 1.0:
                self.waiting_for_enemy = False
                self.timer = 0
                if self.enemy.warship.current_integrity <= 0:
                    self.goto_game_over(True)
                midgame_utils.reset_ship_sprite_list(self.player_sprite_list)
                midgame_utils.reset_ship_sprite_list(self.enemy_sprite_list)
                self.enemy_turn()
                if self.player.warship.current_integrity <= 0:
                    self.goto_game_over(False)
                self.player_damage_opportunity = round(midgame_utils.roll_damage_opportunity(), 2)
                self.enemy_damage_opportunity = round(midgame_utils.roll_damage_opportunity(), 2)

    def draw_hud(self):

        self.player_damage_opportunity_text.text = f"{self.player_damage_opportunity}"
        self.player_damage_opportunity_text.draw()

        self.player_ammo_text.text = f"{self.player.warship.current_ammo}/{self.player.warship.ammo_storage}"
        self.player_ammo_text.draw()

        self.player_speed_text.text = f"{self.player.warship.current_speed}/{self.player.warship.max_speed}"
        self.player_speed_text.draw()

        self.player_integrity_text.text = f"{self.player.warship.current_integrity}/{self.player.warship.max_integrity}"
        self.player_integrity_text.draw()

        self.enemy_damage_opportunity_text.text = f"{self.enemy_damage_opportunity}"
        self.enemy_damage_opportunity_text.draw()

        self.enemy_ammo_text.text = f"{self.enemy.warship.current_ammo}/{self.enemy.warship.ammo_storage}"
        self.enemy_ammo_text.draw()

        self.enemy_speed_text.text = f"{self.enemy.warship.current_speed}/{self.enemy.warship.max_speed}"
        self.enemy_speed_text.draw()

        self.enemy_integrity_text.text = f"{self.enemy.warship.current_integrity}/{self.enemy.warship.max_integrity}"
        self.enemy_integrity_text.draw()

    def on_click_atacar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: atacar_btn")
        if self.waiting_for_enemy:
            print("Rejected for enemy")
            return
        if (self.player.warship.current_ammo < self.player.warship.bullets_per_shot):
            storage_utils.execute_sound("weapon_empty.mp3")
            #debug_utils.print_warship_current_state(self.player.warship)
            return
        #debug_utils.print_warship_current_state(self.player.warship)  
        midgame_utils.attack(self.player, self.enemy, self.enemy_sprite_list, self.player_damage_opportunity)
        #debug_utils.print_warship_current_state(self.enemy.warship)  
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
            #debug_utils.print_warship_current_state(self.player.warship)
            return
        midgame_utils.reload(self.player)
        #debug_utils.substract_integrity(self.player.warship)
        #debug_utils.print_warship_current_state(self.player.warship)
        self.waiting_for_enemy = True
        self.timer = 0

    def on_click_acelerar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: acelerar_btn")
        if self.waiting_for_enemy:
            print("Rejected for enemy")
            return
        if self.player.warship.current_speed == self.player.warship.max_speed:
            storage_utils.execute_sound("button_sound1.mp3")
            #debug_utils.print_warship_current_state(self.player.warship)
            return
        midgame_utils.accelerate(self.player)
        #debug_utils.print_warship_current_state(self.player.warship)
        self.waiting_for_enemy = True
        self.timer = 0

    def on_click_reparar(self, event: arcade.gui.UIOnClickEvent):
        print("Clicked: reparar_btn")
        if self.waiting_for_enemy:
            print("Rejected for enemy")
            return
        if self.player.warship.current_integrity == self.player.warship.max_integrity:
            storage_utils.execute_sound("button_sound1.mp3")
            #debug_utils.print_warship_current_state(self.player.warship)
            return
        midgame_utils.repair(self.player, self.player_sprite_list)
        #debug_utils.print_warship_current_state(self.player.warship)
        self.waiting_for_enemy = True
        self.timer = 0

    def enemy_turn(self):
        decision_pool = ["attack", "reload", "accelerate", "repair"]
        decision = random.choice(decision_pool)
        decided = False
        while not decided:
            if (decision == "attack") and (self.enemy.warship.current_ammo >= self.enemy.warship.bullets_per_shot):
                midgame_utils.attack(self.enemy, self.player, self.player_sprite_list, self.enemy_damage_opportunity)
                decided = True
            elif (decision == "reload") and (self.enemy.warship.current_ammo < self.enemy.warship.ammo_storage):
                midgame_utils.reload(self.enemy)
                decided = True
            elif (decision == "accelerate") and (self.enemy.warship.current_speed < self.enemy.warship.max_speed):
                midgame_utils.accelerate(self.enemy)
                decided = True
            elif (decision == "repair") and (self.enemy.warship.current_integrity < self.enemy.warship.max_integrity):
                midgame_utils.repair(self.enemy, self.enemy_sprite_list)
                decided = True
            else:
                decision = random.choice(decision_pool)

    def goto_game_over(self, player_wins: bool):
        self.clear()
        self.uimanager.clear()
        from scenes.pos_game.GameOverView import GameOverView
        game_over_view = GameOverView(player_wins, self.player, self.enemy, self.background)
        game_over_view.setup()
        self.window.show_view(game_over_view)
