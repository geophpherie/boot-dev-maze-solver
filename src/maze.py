from tkinter import Tk, Canvas
import time


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack()


class Window:
    def __init__(self, width: int, height: int):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()

    def close(self):
        self._running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self._canvas, fill_color)


class Cell:
    def __init__(
        self,
        window: Window = None,
        has_left_wall: bool = True,
        has_right_wall: bool = True,
        has_top_wall: bool = True,
        has_bottom_wall: bool = True,
    ):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        self._win = window

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_top_wall = has_top_wall

    def draw(self, top_left: Point, bot_right: Point):
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bot_right.x
        self._y2 = bot_right.y

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            if self._win:
                self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            if self._win:
                self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            if self._win:
                self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self._win:
                self._win.draw_line(line, "black")

    def draw_move(self, to_cell: "Cell", undo: bool = False):
        if undo:
            color = "red"
        else:
            color = "grey"

        c1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        c2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)

        line = Line(c1, c2)

        self._win.draw_line(line, color)


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window = None
    ):
        self.x1 = x1
        self.y1 = y1

        self._num_rows = num_rows
        self._num_cols = num_cols

        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y

        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells: list[list[Cell]] = []

        for i in range(self._num_cols):
            col: list[Cell] = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        cell = self._cells[i][j]
        top_left = Point(
            self.x1 + (self._cell_size_x * i), self.y1 + (self._cell_size_y * j)
        )
        bottom_right = Point(
            self.x1 + (self._cell_size_x * (i + 1)),
            self.y1 + (self._cell_size_y * (j + 1)),
        )
        cell.draw(top_left, bottom_right)
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.005)
