import arcade
import arcade.gui
import config

WINDOW_WIDTH = config.WINDOW_WIDTH
WINDOW_HEIGHT = config.WINDOW_HEIGHT
WINDOW_TITLE = config.WINDOW_TITLE
VERSION = config.VERSION

class MenuView(arcade.View):
    def __init__(self, bg_color: tuple = (26, 26, 26)):
        super().__init__()
        self.background_color = bg_color

        self.label0 = arcade.Text(
            "Menu Principal",
            WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 1.25),
            color=arcade.color.WHITE,
            font_size=100,
            anchor_x="center",
            anchor_y="center"
        )

        self.label1 = arcade.Text(
            f"Naval Warfare, ({VERSION}) por Alonso",
            (WINDOW_WIDTH / 2) - 225, (WINDOW_HEIGHT / 2) - 350,
            color=arcade.color.WHITE,
            font_size=25,
            anchor_x="center",
            anchor_y="center"
        )

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.label0.draw()
        self.label1.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.BACKSPACE:
            from scenes.CoverView import CoverView
            cover_view = CoverView()
            cover_view.setup()
            self.window.show_view(cover_view)

    '''
    def on_key_release(self, key, modifiers):
        if key == arcade.key.A:
            cover_view = CoverView()
            cover_view.setup()
            self.window.show_view(cover_view)
            '''