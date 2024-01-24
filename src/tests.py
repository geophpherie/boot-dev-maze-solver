import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)

    def test_maze_has_start(self):
        num_cols = 20
        num_rows = 1
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertFalse(m._cells[0][0].has_top_wall)

    def test_maze_has_end(self):
        num_cols = 20
        num_rows = 1
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m._cells[-1][-1].has_bottom_wall)

    def test_no_cell_visited(self):
        num_cols = 20
        num_rows = 1
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        for i in range(m._num_cols):
            for j in range(m._num_rows):
                self.assertFalse(m._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
