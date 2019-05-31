
import arcade


WIDTH = 1000
HEIGHT = 1000
current_screen = "menu"

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
    elif  current_screen == "instruction":
        arcade.draw_text("instructions: Click button to control fish. Steer away from nets, hooks, and collect bubbles for extra health", WIDTH/2, HEIGHT/2, arcade.color.RED)
        arcade.draw_text("press esc to go back to main menu", WIDTH- 10, HEIGHT/2-30, arcade.color.RED)
    if current_screen == "play":
        arcade.draw_text ("play screen", WIDTH/2, HEIGHT/2, arcade.color.RED)


def on_key_press(key, modifiers): 
    pass
    global current_screen
    print (key)
    if key == arcade.key.I:
        current_screen = "instruction"
    elif key == arcade.key.ESCAPE:
        current_screen = "menu"
    elif key == arcade.key.P:
        current_screen = "play screen"

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
