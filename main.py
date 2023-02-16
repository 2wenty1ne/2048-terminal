import ast

# Spielfeld 4x4

GAME_SIZE = 4

def create_field(size):
    return [[0 for y in range(size)] for y in range(size)]


playing_field = create_field(GAME_SIZE)


def draw_playing_field(playing_field):
    row = ""
    column = ""
    for x_index, x_value in enumerate(playing_field):
        for y_index, y_value in enumerate(x_value):
            row_string = f" {y_value}"
            if not y_index == len(playing_field) - 1:
                row_string = row_string + " |"
            row = row + row_string
        print(row)
        row = ""
        if not x_index == len(playing_field) - 1:
            column_string = "---"
            for tile in range(len(playing_field) - 1):
                column_string = column_string + "----"
            column = column + column_string
        print(column)
        column = ""
    print()


#? Compressing
def compress_playfield(playing_field, compress_direction):

    print("Befor:")
    draw_playing_field(playing_field)

    while True:
        move_made_bool = False
        for index_y, row in enumerate(playing_field):
            for index_x, tile in enumerate(row):
                if playing_field[index_y][index_x]:
                    move_made_bool = one_move(playing_field, compress_direction, index_x, index_y)
                if move_made_bool:
                    break
            if move_made_bool:
                break

        if not move_made_bool:
            break

    print('After:')
    draw_playing_field(playing_field)


def one_move(playing_field, compress_direction, move_tile_x, move_tile_y):

    #print(f"X: {move_tile_x}, Y: {move_tile_y}\n")

    if compress_direction == "right":
        if move_tile_x + 1 > GAME_SIZE - 1:
            #print(f"out of bounds x right\nX: {move_tile_x}, Y: {move_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[move_tile_y][move_tile_x + 1]
        if dir_neighbour == 0:
            moved_value = playing_field[move_tile_y][move_tile_x]
            playing_field[move_tile_y][move_tile_x] = 0
            playing_field[move_tile_y][move_tile_x + 1] = moved_value
            return True
        
        else:
            return False


    if compress_direction == "left":
        if move_tile_x - 1 < 0 :
            #print(f"out of bounds x left\nX: {move_tile_x}, Y: {move_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[move_tile_y][move_tile_x - 1]
        if dir_neighbour == 0:
            moved_value = playing_field[move_tile_y][move_tile_x]
            playing_field[move_tile_y][move_tile_x] = 0
            playing_field[move_tile_y][move_tile_x - 1] = moved_value
            return True
        
        else:
            return False


    if compress_direction == "down":
        if move_tile_y + 1 > GAME_SIZE - 1:
            #print(f"out of bounds y down\nX: {move_tile_x}, Y: {move_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[move_tile_y + 1][move_tile_x]
        if dir_neighbour == 0:
            moved_value = playing_field[move_tile_y][move_tile_x]
            playing_field[move_tile_y][move_tile_x] = 0
            playing_field[move_tile_y + 1][move_tile_x] = moved_value
            return True
        
        else:
            return False


    if compress_direction == "up":
        if move_tile_y - 1 < 0 :
            #print(f"out of bounds y up\nX: {move_tile_x}, Y: {move_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[move_tile_y - 1][move_tile_x]
        if dir_neighbour == 0:
            moved_value = playing_field[move_tile_y][move_tile_x]
            playing_field[move_tile_y][move_tile_x] = 0
            playing_field[move_tile_y - 1][move_tile_x] = moved_value
            return True
        
        else:
            return False


#? Merging
def merge_playfield(playing_field, merge_direction):

    changed_playing_field = create_field(GAME_SIZE)

    print("Befor:")
    draw_playing_field(playing_field)

    #while True:
    merge_made_bool = False
    for index_y, row in enumerate(playing_field):
        for index_x, tile in enumerate(row):
            if playing_field[index_y][index_x]:
                merge_made_bool = one_merge(playing_field, merge_direction, index_x, index_y)
        #     if merge_made_bool:
        #         break
        # if merge_made_bool:
        #     break

        # if not merge_made_bool:
        #     break

    if merge_direction == "t":
        direction = input("Direction: ")
        merge_tile_x = int(input("X: "))
        merge_tile_y = int(input("Y: "))
        one_merge(playing_field, direction, merge_tile_x, merge_tile_y)

    print("After:")
    draw_playing_field(playing_field)


def one_merge(playing_field, merge_direction, merge_tile_x, merge_tile_y):

    merge_value = playing_field[merge_tile_y][merge_tile_x]
    #print(f"X: {merge_tile_x}, Y: {merge_tile_y}\nValue: {merge_value}\n")

    if merge_direction == "right":
        if merge_tile_x + 1 > GAME_SIZE - 1:
            #print(f"out of bounds x right\nX: {merge_tile_x}, Y: {merge_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[merge_tile_y][merge_tile_x + 1]
    
        if dir_neighbour == merge_value:
            playing_field[merge_tile_y][merge_tile_x] = 0
            playing_field[merge_tile_y][merge_tile_x + 1] = merge_value + 1
            return True
        
        else:
            return False


    if merge_direction == "left":
        #print(f'Direction: {merge_direction}')
        if merge_tile_x - 1 < 0 :
            #print(f"out of bounds x left\nX: {merge_tile_x}, Y: {merge_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[merge_tile_y][merge_tile_x - 1]

        if dir_neighbour == merge_value:
            playing_field[merge_tile_y][merge_tile_x] = 0
            playing_field[merge_tile_y][merge_tile_x - 1] = merge_value + 1
            return True
        
        else:
            return False


    if merge_direction == "down":
        #print(f'Direction: {merge_direction}')
        if merge_tile_y + 1 > GAME_SIZE - 1:
            #print(f"out of bounds y down\nX: {merge_tile_x}, Y: {merge_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[merge_tile_y + 1][merge_tile_x]

        if dir_neighbour == merge_value:
            playing_field[merge_tile_y][merge_tile_x] = 0
            playing_field[merge_tile_y + 1][merge_tile_x] = merge_value + 1
            return True
        
        else:
            return False


    if merge_direction == "up":
        #print(f'Direction: {merge_direction}')
        if merge_tile_y - 1 < 0 :
            #print(f"out of bounds y up\nX: {merge_tile_x}, Y: {merge_tile_y}\n")
            return False
        
        dir_neighbour = playing_field[merge_tile_y - 1][merge_tile_x]

        if dir_neighbour == merge_value:
            playing_field[merge_tile_y][merge_tile_x] = 0
            playing_field[merge_tile_y - 1][merge_tile_x] = merge_value + 1
            return True
        
        else:
            return False


#? Gameloop
while True:
    command = input("Input a command: ")
    print()
    if command == "place" or command == "p":
        draw_playing_field(playing_field)
        x_change = int(input("Input a x to change: "))
        y_change = int(input("Input a y to change: "))
        new_value = int(input("New cell value: "))
        print()
        print(f'X: {x_change}, Y: {y_change}\nValue on field befor change: {playing_field[y_change][x_change]}')
        playing_field[y_change][x_change] = new_value
        draw_playing_field(playing_field)


    elif command == "compress" or command == "c":
        compress_direction = input("Input a direction: ")

        if compress_direction not in ["left", "right", "up", "down", "t"]:
            print("Unknown direction! :(\n")
            continue

        compress_playfield(playing_field, compress_direction)


    elif command == "merge" or command == "m":
        merge_direction = input("Input a direction: ")

        if merge_direction not in ["left", "right", "up", "down", "t"]:
            print("Unknown direction! :(\n")
            continue

        merge_playfield(playing_field, merge_direction)


    elif command == "draw" or command == "d":
        draw_playing_field(playing_field)


    elif command == "save" or command == "s":
        print(playing_field)
        with open("gamestate.txt", "w") as disk:
            disk.write(str(playing_field))
        print("-Saved successfully!-\n")


    elif command == "load" or command == "l":
        with open("gamestate.txt", "r") as disk:
            gamestate = disk.readline()

        gamestate = ast.literal_eval(gamestate)
        playing_field = gamestate
        print("-Loaded successfully!-\n")


    else:
        print("Unknown command :(\n")

