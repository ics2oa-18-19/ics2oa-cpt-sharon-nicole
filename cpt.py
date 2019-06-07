
import arcade


WIDTH = 1360
HEIGHT = 710
current_screen = "play"
fish_x = WIDTH/4
fish_y = HEIGHT/4
up = False
down = False

def update(delta_time):
    pass

def on_draw():
    arcade.start_render()
    # Draw in here...\
    if current_screen == "menu":
        arcade.draw_text(
                         "Welcome to Fishy Goes Home", WIDTH/2, HEIGHT/2, arcade.color.BLUE)
        arcade.draw_text("press I for instructions ", WIDTH/2, HEIGHT/2-30, arcade.color.RED)
        arcade.draw_text("press P for play screen", WIDTH / 2, HEIGHT / 2 - 60, arcade.color.RED)
    elif current_screen == "instruction":
        arcade.draw_text("instructions: W: up, S: down, collect bubbles and move away from other objects", WIDTH/16, HEIGHT/2, arcade.color.RED)
        arcade.draw_text("press esc to go back to main menu", WIDTH/16, HEIGHT/2-30, arcade.color.RED)
    elif current_screen == "play":
        arcade.draw_circle_filled(fish_x, fish_y, 25, arcade.color.ORANGE)

def on_key_press(key, modifiers):
    global current_screen, fish_x, fish_y
    print (key)
    if key == arcade.key.I:
        current_screen = "instruction"
    elif key == arcade.key.ESCAPE:
        current_screen = "menu"
    elif key == arcade.key.P:
        current_screen = "play screen"
    if key == arcade.key.W:
        fish_y += 10
    elif key == arcade.key.S:
        fish_y -= 10
    elif key == arcade.key.A:
        fish_x -=10
    elif key == arcade.key.D:
        fish_x += 10
def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
