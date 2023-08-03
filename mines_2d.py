def count_adjacent_mines(grid):
    rows = len(grid)
    cols = len(grid[0])

    def is_valid_cell(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def count_mines_around(x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if is_valid_cell(nx, ny) and grid[nx][ny] == '#':
                    count += 1
        return count

    new_grid = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            if grid[i][j] == '-':
                mines_count = count_mines_around(i, j)
                new_row.append(str(mines_count))
            else:
                new_row.append(grid[i][j])
        new_grid.append(new_row)

    return new_grid


# Example usage:
grid = [["-", "-", "-", "#", "#"],["-", "#", "-", "-", "-"],["-", "-", "#", "-", "-"],["-", "#", "#", "-", "-"], ["-", "-", "-", "-", "-"] ]

result_grid = count_adjacent_mines(grid)

for row in result_grid:
    print(' '.join(row))
