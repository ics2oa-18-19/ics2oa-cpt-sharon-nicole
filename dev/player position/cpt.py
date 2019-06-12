import arcade
import random

WIDTH = 1360
HEIGHT = 710
current_screen = "menu"
#          x         y
fish = [WIDTH/4, HEIGHT/4 ]
seaweed_x = [WIDTH, WIDTH, WIDTH, WIDTH]
seaweed_y = [WIDTH, WIDTH, WIDTH, WIDTH]
bubble_x = [WIDTH, WIDTH, WIDTH, WIDTH]
bubble_y = [WIDTH, WIDTH, WIDTH, WIDTH]
up = False
down = False
left = False
right = False
player_health = 100
player_max_health = 100


def update(delta_time):
    global health_width, seaweed_x, seaweed_y
    for index in range(len(seaweed_x)):
        seaweed_x[index] -= 6

        if seaweed_x[index] < 0:
            seaweed_x[index] -= 1360
            seaweed_x[index] = random.randrange(WIDTH, WIDTH + 50)
            seaweed_y[index] = random.randrange(0, HEIGHT)
    # bubble
    for index in range(len(bubble_x)):
        bubble_x[index] -= 6

        if bubble_x[index] < 0:
            bubble_x[index] -= 1360
            bubble_x[index] = random.randrange(WIDTH, WIDTH + 50)
            bubble_y[index] = random.randrange(0, HEIGHT)
# movement
    if fish [1] <= HEIGHT:
        if up == True:
            fish [1] +=10
    if fish[1] >= 1:
        if down == True:
            fish[1] -= 10
    if fish [0] >= 1:
        if left == True:
            fish[0] -= 10
    if fish[0] <= WIDTH:
        if right == True:
            fish[0] += 10

# health bar

def on_draw():
    arcade.start_render()
    # screens and fish
    if current_screen == "menu":
        arcade.draw_text(
            "Fishy", WIDTH /4 , HEIGHT/2, arcade.color.WHITE, font_size= 100)
        arcade.draw_text("press I for instructions ", WIDTH / 2, HEIGHT / 2 - 30, arcade.color.RED)
        arcade.draw_text("press P for play screen", WIDTH / 2, HEIGHT / 2 - 60, arcade.color.RED)
        arcade.draw_circle_filled(fish[0], fish[1], 100, arcade.color.ORANGE)
        arcade.draw_circle_filled(fish[0] + 40, fish[1], 15, arcade.color.BLACK)
        arcade.draw_triangle_filled(fish[0], fish[1], fish[0] - 50, fish[1] + 10, fish[0] - 50, fish[1] - 50,
                                    arcade.color.ORANGE)
    elif current_screen == "instruction":
        arcade.draw_text(
            "instructions: W= up S= down A= left D = right - collect bubbles and move away from other objects",
            WIDTH / 16, HEIGHT / 2, arcade.color.RED)
        arcade.draw_text("press esc to go back to main menu", WIDTH / 16, HEIGHT / 2 - 30, arcade.color.RED)
    elif current_screen == "over":
        arcade.draw_text("GAME OVER", WIDTH / 16, HEIGHT / 2, arcade.color.RED, font_size=100)
    # seaweed drawing
    if current_screen == "play":
        for x, y in zip(seaweed_x, seaweed_y):
            arcade.draw_rectangle_filled(x, y, 10, 80, arcade.color.SPRING_GREEN)

    # bubble drawing
    if current_screen == "play":
        for x, y in zip(bubble_x, bubble_y):
            arcade.draw_circle_filled(x, y, 5, arcade.color.LIGHT_BLUE)
    # fish
    if current_screen == "play":
        arcade.draw_circle_filled(fish[0], fish[1], 25, arcade.color.ORANGE)
        arcade.draw_circle_filled(fish[0] + 10, fish[1], 2, arcade.color.BLACK)
    # health bar drawing
    if current_screen == "play":
        max_bar_width = 200
        bar_height = 50
        arcade.draw_xywh_rectangle_filled(WIDTH / 2 - max_bar_width / 2,
                                          HEIGHT - bar_height,
                                          max_bar_width,
                                          bar_height,
                                          arcade.color.BLUE)

        health_width = player_health / player_max_health * max_bar_width
        arcade.draw_xywh_rectangle_filled(WIDTH / 2 - max_bar_width / 2,
                                          HEIGHT - bar_height,
                                          health_width,
                                          bar_height,
                                          arcade.color.GREEN)



def on_key_press(key, modifiers):
    global current_screen, fish, up, down, left, right
    print(key)
    if key == arcade.key.I:
        current_screen = "instruction"
    elif key == arcade.key.ESCAPE:
        current_screen = "menu"

    elif key == arcade.key.P:
        current_screen = "play"
    if key == arcade.key.W:
       up = True
    if key == arcade.key.S:
        down =True
    if key == arcade.key.A:
        left = True
    if key == arcade.key.D:
        right = True

    if key == arcade.key.B:
        current_screen = "over"


def on_key_release(key, modifiers):
    global current_screen, fish, up, down, left,right
    if current_screen == "play":
        if key == arcade.key.W:
            up = False
        if key == arcade.key.S:
            down = False
        if key == arcade.key.A:
            left = False
        if key == arcade.key.D:
            right = False

def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
