import pgzrun
import random

WIDTH = 800
HEIGHT = 600
center_x = WIDTH//2
center_y = HEIGHT//2
center = (center_x, center_y)
final_level = 5
start_speed = 10
ITEMS = ["bag", "battery", "bottle", "chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global game_over, game_complete, current_level, items

    screen.clear()
    screen.blit("bground", (0,0))
    if game_over:
        display_message("Game Over!!!!!", "that sucks to be you.")
    elif game_complete:
        display_message("Game Won!!!!!", "dang. heres a cookie 🍪🍪🍪🍪🍪🍪🍪")

    else:
        for item in items:
            item.draw()


def display_message(heading, subheading):
    screen.draw.text(heading, (center_x, (center_y-15)), font = ("Georgia", 50, "bold"), color = ("white"))
    screen.draw.text(subheading, (center_x, (center_y +15)), font = ("Georgia", 30), color = ("white"))


def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(num_extra_items):
    items_to_create = get_option_to_create(num_extra_items)

    new_items = create_items(items_to_create)
    layout_items(new_items)


    return new_items


def get_option_to_create(num_extra_items):

    items_to_create = ["paper"]
    for i in range (num_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items = []

    for i in items_to_create:
        item = Actor(i + "img")
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout)+1
    gap_size = WIDTH/number_of_gaps
    





pgzrun.go()


