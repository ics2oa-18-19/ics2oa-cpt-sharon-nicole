import arcade


WIDTH = 640
HEIGHT = 480

up = False
down = False
fish_x = HEIGHT/2
fish_y = WIDTH/ 2
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
    global up, down, fish_x
    if up == True:
        fish_x += 10
    if down == True:
        fish_x -= 10



def on_draw():
    arcade.start_render()
    if fish_x == HEIGHT/2:
        arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)


def on_key_press(key, modifiers):
    global fish_x
    print (key)
    if key == arcade.key. W:
        fish_x += 10
    elif key == arcade.key.S:
        fish_x -= 10



def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
