import turtle

# Settings
DISTANCE = 140
N = 5
DRAW_SPEED = 0  # 0 is the fastest speed

# Constants
CW = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
CCW = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
NORTH = [0, 1, 2, 3]
EAST = [1, 2, 3, 0]
SOUTH = [2, 3, 0, 1]
WEST = [3, 0, 1, 2]


def CLI_UI():
    global N, DRAW_SPEED
    N = int(input("Enter the order of Hilbert's Curve: "))
    DRAW_SPEED = int(input("Enter drawing speed (0 is the fastest): "))


def hilbert_order(n, dis, direction, order, coor_list, a_turtle):
    """
    Recursively draw the smaller order of Hilbert's curve.
    :param n: The order of Hilbert's curve
    :type n: int
    :param dis: The distance to the 4 corner of a square (radius)
    :type dis: float
    :param direction: The facing direction (E, W, N or S) that is save for the next iteration
    :type direction: a list
    :param order: can be clockwise or counter-clockwise that is save for the next iteration
    :type order: 2D list
    :param coor_list: a list of coordinates for drawing or for recursion
    :type coor_list: 2D list
    :param a_turtle: a turtle
    :type a_turtle: turtle.Turtle()
    :return:
    :rtype:
    """
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

        hilbert_order(n - 1, half_dis, dir_pair[0], order_top,
                      list_order(coor_list[0], order_bot, dir_pair[0], half_dis), a_turtle)
        hilbert_order(n - 1, half_dis, direction, order_bot,
                      list_order(coor_list[1], order_top, direction, half_dis), a_turtle)
        hilbert_order(n - 1, half_dis, direction, order_bot,
                      list_order(coor_list[2], order_top, direction, half_dis), a_turtle)
        hilbert_order(n - 1, half_dis, dir_pair[1], order_top,
                      list_order(coor_list[3], order_bot, dir_pair[1], half_dis), a_turtle)


def list_order(coor, order, direction, distance):
    """
    Splitting 1 coordinates into 4 corner coordinates
    :param coor: The coordinate that is divided into 4 corners coordinates
    :type coor: a coordinate list [x, y]
    :param order: can be clockwise or counter-clockwise that splits the input coordinate
    :type order: 2D list
    :param direction: The facing direction (E, W, N or S)
    :type direction: a list
    :param distance: how far to split according to the input coordinate
    :type distance: float
    :return: 4 corners coordinates
    :rtype: 2D list
    """
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
    CLI_UI()
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.speed(DRAW_SPEED)

    my_turtle.up()
    hilbert_order(N, DISTANCE, NORTH, CCW, list_order([0, 0], CW, NORTH, DISTANCE), my_turtle)

    my_win.exitonclick()


if __name__ == '__main__':
    main()
