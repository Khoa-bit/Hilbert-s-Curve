import turtle

DISTANCE = 64
CW = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
CCW = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
NORTH = [0, 1, 2, 3]
EAST = [1, 2, 3, 0]
SOUTH = [2, 3, 0, 1]
WEST = [3, 0, 1, 2]


def hilbert_order(n, dis, direction, order, coor_list, a_turtle):
    if n == 1:
        for i in range(4):
            a_turtle.goto(coor_list[i])
            a_turtle.down()
    else:
        half_dis = dis / 2
        if direction == NORTH:
            dir_pair = [WEST, EAST]
        elif direction == SOUTH:
            dir_pair = [EAST, WEST]
        elif direction == WEST:
            dir_pair = [SOUTH, NORTH]
        else:
            dir_pair = [NORTH, SOUTH]

        if order == CCW:
            order_top = CW
            order_bot = CCW
            dir_pair.reverse()
        else:
            order_top = CCW
            order_bot = CW

        hilbert_order(n - 1, half_dis, dir_pair[0], order_top, list_order(coor_list[0], order_bot, dir_pair[0], half_dis),
                      a_turtle)
        hilbert_order(n - 1, half_dis, direction, order_bot, list_order(coor_list[1], order_top, direction, half_dis),
                      a_turtle)
        hilbert_order(n - 1, half_dis, direction, order_bot, list_order(coor_list[2], order_top, direction, half_dis),
                      a_turtle)
        hilbert_order(n - 1, half_dis, dir_pair[1], order_top, list_order(coor_list[3], order_bot, dir_pair[1], half_dis),
                      a_turtle)


def list_order(coor, order, direction, distance):
    tmp_list = []
    order_dir = direction
    if order == CCW:
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
    my_turtle.speed(0)
    tmp_dir = NORTH

    my_turtle.up()
    hilbert_order(6, DISTANCE, tmp_dir, CCW, list_order([0, 0], CW, tmp_dir, DISTANCE), my_turtle)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
