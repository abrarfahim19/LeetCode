import collections

board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]

row = collections.defaultdict(set)
col = collections.defaultdict(set)
sqr = collections.defaultdict(set)


for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == ".":
            continue
        elif (
            (board[r][c] in row[r])
            or (board[r][c] in col[c])
            or (board[r][c] in sqr[(r // 3, c // 3)])
        ):
            print("Position", r, c, "Value", board[r][c], "- False")
        row[r].add(board[r][c])
        col[c].add(board[r][c])
        sqr[(r // 3, c // 3)].add(board[r][c])
print("True")
