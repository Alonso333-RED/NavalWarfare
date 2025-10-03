import arcade
import arcade.gui
import config
from Battleship import Battleship
import scenes

def main():
    window = arcade.Window(config.WINDOW_WIDTH, config.WINDOW_HEIGHT, config.WINDOW_TITLE)
    menu_view = scenes.CoverView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()