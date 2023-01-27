import ast

# Spielfeld 4x4

GAME_SIZE = 4

playing_field = [[0 for y in range(GAME_SIZE)] for y in range(GAME_SIZE)]



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

    x_test = move_tile_x
    y_test = move_tile_y
    #print(f"X: {x_test}, Y: {y_test}\n")

    if compress_direction == "right":
        if x_test + 1 > GAME_SIZE - 1:
            #print(f"out of bounds x right\nX: {x_test}, Y: {y_test}\n")
            return False
        
        x_neighbour = playing_field[y_test][x_test + 1]
        if x_neighbour == 0:
            moved_value = playing_field[y_test][x_test]
            playing_field[y_test][x_test] = 0
            playing_field[y_test][x_test + 1] = moved_value
            return True
        
        else:
            return False


    if compress_direction == "left":
        if x_test - 1 < 0 :
            #print(f"out of bounds x left\nX: {x_test}, Y: {y_test}\n")
            return False
        
        x_neighbour = playing_field[y_test][x_test - 1]
        if x_neighbour == 0:
            moved_value = playing_field[y_test][x_test]
            playing_field[y_test][x_test] = 0
            playing_field[y_test][x_test - 1] = moved_value
            return True
        
        else:
            return False


    if compress_direction == "down":
        if y_test + 1 > GAME_SIZE - 1:
            #print(f"out of bounds y down\nX: {x_test}, Y: {y_test}\n")
            return False
        
        x_neighbour = playing_field[y_test + 1][x_test]
        if x_neighbour == 0:
            moved_value = playing_field[y_test][x_test]
            playing_field[y_test][x_test] = 0
            playing_field[y_test + 1][x_test] = moved_value
            return True
        
        else:
            return False


    if compress_direction == "up":
        if y_test - 1 < 0 :
            #print(f"out of bounds y up\nX: {x_test}, Y: {y_test}\n")
            return False
        
        x_neighbour = playing_field[y_test - 1][x_test]
        if x_neighbour == 0:
            moved_value = playing_field[y_test][x_test]
            playing_field[y_test][x_test] = 0
            playing_field[y_test - 1][x_test] = moved_value
            return True
        
        else:
            return False



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
        pass 


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

