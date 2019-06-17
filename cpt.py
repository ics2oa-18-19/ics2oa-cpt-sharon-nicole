import arcade
import random
import math

WIDTH = 1360
HEIGHT = 710
current_screen = "menu"
#          x         y
fish = [WIDTH/4, HEIGHT/4 , 2 ]
seaweed_x = [24,50,78]
seaweed_y = [100,500,60]
rock_x = []
rock_y = []
other_fish_x =[45, 60, 73]
other_fish_y = [84, 83, 96]
up = False
down = False
left = False
right = False
player_health = 100
player_max_health = 100

for _ in range(5):
    x = random.randrange (0, WIDTH)
    y = random.randrange (HEIGHT, HEIGHT *2)

    rock_x.append(x)
    rock_y.append(y)

def update(delta_time):
    global seaweed_x, seaweed_y, current_screen
    for index in range(len(seaweed_x)):
        seaweed_x[index] -= 20

        if seaweed_x[index] < 0:
            seaweed_x[index] -= 1360
            seaweed_x[index] = random.randrange(WIDTH, WIDTH + 50)
            seaweed_y[index] = random.randrange(0, HEIGHT)
    # bubble
    for index in range(len(rock_x)):
        rock_x[index] -= 10

        if rock_x[index] < 0:
            rock_x[index] -= 1360
            rock_x[index] = random.randrange(WIDTH, WIDTH + 50)
            rock_y[index] = random.randrange(0, HEIGHT)

    for index in range (len(other_fish_x)):
        other_fish_x [index] -= 50

        if other_fish_x[index] < 0:
            other_fish_x[index] -=1360
            other_fish_x [index] = random.randrange(WIDTH,WIDTH +70)
            other_fish_y [index] = random. randrange (0, HEIGHT)
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

# player dies

    for i, (x,y) in enumerate (zip(rock_x, rock_y)):
        a = x - (fish[0]+10)
        b = y - (fish[1]+10)
        dist = math.sqrt(a**2 + b**2)

    if dist - 10 - 40 <= 0:
        current_screen = "over"

def on_draw():
    arcade.start_render()
    # screens and fish
    if current_screen == "menu":
        arcade.draw_text(
            "Fishy", WIDTH /4 , HEIGHT/2, arcade.color.WHITE, font_size= 100)
        arcade.draw_text("press I for instructions ", WIDTH / 2, HEIGHT / 2 - 30, arcade.color.WHITE, font_size= 20)
        arcade.draw_text("press P for play screen", WIDTH / 2, HEIGHT / 2 - 60, arcade.color.WHITE, font_size= 20)
        arcade.draw_circle_filled(fish[0], fish[1], 100, arcade.color.ORANGE)
        arcade.draw_circle_filled(fish[0] + 40, fish[1], 15, arcade.color.BLACK)
        arcade.draw_triangle_filled(fish[0], fish[1], fish[0] - 50, fish[1] + 10, fish[0] - 50, fish[1] - 50,
                                    arcade.color.ORANGE)
    elif current_screen == "instruction":
        arcade.draw_text(
            "Instructions: W= up S= down A= left D = right",
            WIDTH / 16, HEIGHT / 2, arcade.color.WHITE, font_size= 30)
        arcade.draw_text ("Help fishy avoid rocks and bring him home", WIDTH/16, HEIGHT/2 -30, arcade.color.WHITE, font_size= 27)
        arcade.draw_text("Press esc to go back to main menu", WIDTH / 16, HEIGHT / 2 - 60, arcade.color.WHITE, font_size= 27)
    elif current_screen == "over":
        arcade.draw_text("GAME OVER", WIDTH / 16, HEIGHT / 2, arcade.color.RED, font_size=100)
    # seaweed drawing
    if current_screen == "play":
        for x, y in zip(seaweed_x, seaweed_y):
            arcade.draw_rectangle_filled(x, y, 10, 80, arcade.color.SPRING_GREEN)

#rock
    if current_screen == "play":
        for x, y in zip (rock_x, rock_y):
            arcade.draw_circle_filled(x, y, 5, arcade.color.LIGHT_BLUE)
    # fish
    if current_screen == "play":
        arcade.draw_circle_filled(fish[0], fish[1], 25, arcade.color.ORANGE)
        arcade.draw_circle_filled(fish[0] + 10, fish[1], fish [2], arcade.color.BLACK)
#other fish
    if current_screen == "play":
        for x, y in zip (other_fish_x, other_fish_y):
            arcade.draw_circle_filled(x,y,25, arcade.color.PURPLE)
            arcade.draw_circle_filled(x - 10, y, 5, arcade.color.BLACK)

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

    def draw_bubble(x, y):
        arcade.draw_circle_filled(x, y, 5, arcade.color.LIGHT_BLUE)

if __name__ == '__main__':
    setup()
