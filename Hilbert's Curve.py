import turtle

DISTANCE = 64
TOP_ORDER = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
BOT_ORDER = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
NORTH = [0, 1, 2, 3]
EAST = [1, 2, 3, 0]
SOUTH = [2, 3, 0, 1]
WEST = [3, 0, 1, 2]


def hilbert_order(n, dis, direction, coor_list, a_turtle):
    if n == 1:
        for i in range(4):
            a_turtle.goto(coor_list[i])
    else:
        half_dis = dis / 2
        if direction == NORTH:
            dir_pair = [EAST, WEST]
        elif direction == SOUTH:
            dir_pair = [WEST, EAST]
        elif direction == WEST:
            dir_pair = [NORTH, SOUTH]
        else:
            dir_pair = [SOUTH, NORTH]

        hilbert_order(n - 1, half_dis, dir_pair[0], list_order(coor_list[0], BOT_ORDER, dir_pair[0], half_dis),
                      a_turtle)
        hilbert_order(n - 1, half_dis, direction, list_order(coor_list[1], TOP_ORDER, direction, half_dis),
                      a_turtle)
        hilbert_order(n - 1, half_dis, direction, list_order(coor_list[2], TOP_ORDER, direction, half_dis),
                      a_turtle)
        hilbert_order(n - 1, half_dis, dir_pair[1], list_order(coor_list[3], BOT_ORDER, dir_pair[1], half_dis),
                      a_turtle)


def list_order(coor, order, direction, distance):
    tmp_list = []
    order_dir = direction
    if order == BOT_ORDER:
        if direction == EAST:
            order_dir = WEST
        elif direction == WEST:
            order_dir = EAST
    for i in order_dir:
        tmp_list.append([coor[0] + (distance * order[i][0]), coor[1] + (distance * order[i][1])])

    print(tmp_list)
    return tmp_list


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.speed(1)
    tmp_dir = NORTH
    hilbert_order(2, DISTANCE, tmp_dir, list_order([0, 0], BOT_ORDER, tmp_dir, DISTANCE), my_turtle)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
