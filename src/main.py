from maze import Window, Maze, Line, Point, Cell


def main():
    win = Window(800, 600)
    # win.draw_line(Line(Point(1, 1), Point(2, 2)), "red")
    # win.draw_line(Line(Point(8, 200), Point(300, 700)), "black")

    # cell = Cell(win, has_top_wall=False, has_left_wall=False)
    # cell.draw(
    #     Point(5, 5),
    #     Point(100, 100),
    # )

    # cell_1 = Cell(win, has_bottom_wall=False)
    # cell_1.draw(Point(105, 105), Point(200, 250))

    # cell_2 = Cell(win, has_right_wall=False)
    # cell_2.draw(Point(200, 200), Point(350, 350))

    # cell_1.draw_move(cell_2)

    maze = Maze(
        x1=5, y1=5, num_rows=20, num_cols=20, cell_size_x=20, cell_size_y=20, win=win
    )
    win.wait_for_close()


if __name__ == "__main__":
    main()
