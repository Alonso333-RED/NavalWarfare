import arcade
import config
from Warship import Warship
from scenes.pre_game.CoverView import CoverView

def main():

    window = arcade.Window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, config.WINDOW_TITLE)
    cover_view = CoverView()
    window.show_view(cover_view)
    arcade.run()

if __name__ == "__main__":
    main()