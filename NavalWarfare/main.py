import arcade
import config
from utils import general_utils
from Warship import Warship
from scenes.pre_game.CoverView import CoverView

def main():

    ijnYamato = Warship(
        "Yamato", 9500, 2500, 0.25,
        37, 51, 6, 1, 12, 6, 3, 1, 1150,
        "NavalWarfare/images/ships_sprites/IJNyamato_default.png",
        "NavalWarfare/images/ships_sprites/IJNyamato_damaged.png",
        "NavalWarfare/images/ships_sprites/IJNyamato_repaired.png"
    )

    general_utils.store_warship(ijnYamato)
    hmsSovereign = general_utils.load_warship("yamato")
    print(hmsSovereign.get_base_stats())
    hmsSovereign.name = "Sovereign"
    general_utils.store_warship(hmsSovereign)

    window = arcade.Window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, config.WINDOW_TITLE)
    cover_view = CoverView()
    window.show_view(cover_view)
    arcade.run()

if __name__ == "__main__":
    main()