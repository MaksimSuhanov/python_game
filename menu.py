import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.25
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Работа с окнами'

class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show_view(self):
        arcade.set_background_color(arcade.color.ORANGE)



    def on_draw(self):
        self.clear()
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()
        arcade.draw_text('Пауза', SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x='center')
        arcade.draw_text('Press ESC to continue', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=20, anchor_x='center')
        arcade.draw_text('Press ENTER to restart', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30,
                         arcade.color.BLACK, font_size=20, anchor_x='center')
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top = player_sprite.top,
                                          bottom = player_sprite.bottom,
                                          color = arcade.color.ORANGE + (200,)
                                          )



    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
        elif key == arcade.key.ENTER:
            game = GameView()
            self.window.show_view(game)

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture('game_over.jpg')
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)

class InstructionView(arcade.View):
    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Экран инструкций", self.window.width / 2, self.window.height / 2, arcade.color.WHITE,
                         font_size=50, anchor_x='center')
        arcade.draw_text("Щелкните для продолжения", self.window.width / 2, self.window.height / 2 - 75, arcade.color.WHITE,
                         font_size=20, anchor_x='center')
        arcade.draw_text("START GAME", self.window.width / 2, self.window.height / 2 - 145,
                         arcade.color.WHITE,
                         font_size=20, anchor_x='center')

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 310 < x < 490 and 158 < y < 175:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.AMAZON)
        self.player_list = None
        self.player_sprite = None
        self.coin_list = None
        self.window.set_mouse_visible(False)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite(
            ":resources:images/space_shooter/playerShip1_green.png",
            SPRITE_SCALING_PLAYER
        )
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.coin_list = arcade.SpriteList()
        for i in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/keyBlue.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.coin_list.draw()




    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        print(f'{x=}')
        print(f'{y=}')


    def on_update(self, delta_time: float):
        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()

        if len(self.coin_list) == 0:
            view = GameOverView()
            self.window.show_view(view)

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.ESCAPE:
            pause = PauseView(self)
            self.window.show_view(pause)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)



if __name__ == '__main__':
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    star_view = InstructionView()
    window.show_view(star_view)
    arcade.run()