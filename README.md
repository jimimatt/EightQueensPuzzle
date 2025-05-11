# Eight Queens Puzzle

Place 8 Queens on a 8x8 board that no two queens threaten each other.

## Solving idea

- build chessboard iterative row by row
- one queen per row
- check columns of queens in already existing rows
- tracking already occupied diagonal lines
- backtrack when no valid position is found
- use generators for position (back) tracking
- work inplace to avoid copying the board

Generator & working inplace to aim for a minimal memory footprint.

## Profiling

### trace

[trace](https://docs.python.org/3/library/trace.html) program execution

```
uv run python -m trace --count -C ./trace_inspection eight_queens_puzzle.py
```

### memray

[memray](https://github.com/bloomberg/memray) works only with Linux & MacOS. Here it's not part of the project, use from global installation:

```
python -m memray run eight_queens_puzzle.py
```

generate flamegraph from the generated *.bin file

```
python -m memray flamegraph eight_queens_puzzle.py*.bin
```
