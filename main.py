import random
import arcade

SPRITE_SCALING_PLAYER = 0,5
SPRITE_SCALING_COIN = 0,25
COIN_COUNT = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Работа с окнами'
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AQUAMARINE)
        self.player_list = None
        self.player_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        self.clear()
        self.player_list.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass
    def on_update(self, delta_time: float):
        pass

if __name__ == '__main__':
    window = MyGame()
    window.setup()
    arcade.run()
