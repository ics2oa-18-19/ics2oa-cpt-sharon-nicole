import arcade


WIDTH = 640
HEIGHT = 480

player_health = 99
player_max_health = 100


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    max_bar_width = 200
    bar_height = 50
    arcade.draw_xywh_rectangle_filled(WIDTH/2 - max_bar_width/2,
                                      HEIGHT/2 - bar_height/2,
                                      max_bar_width,
                                      bar_height,
                                      arcade.color.BLUE)

    health_width = player_health / player_max_health * max_bar_width
    arcade.draw_xywh_rectangle_filled(WIDTH / 2 - max_bar_width / 2,
                                      HEIGHT / 2 - bar_height / 2,
                                      health_width,
                                      bar_height,
                                      arcade.color.RED)

    arcade.draw_text(f"{player_health}/{player_max_health}",
                     WIDTH/2 - max_bar_width/2,
                     HEIGHT / 2 - bar_height / 2,
                     arcade.color.BLACK,
                     font_size=30)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
