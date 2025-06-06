def cell_to_cube(n):

    if n == 1:
        return (0, 0, 0)
    # Find which ring the cell is in
    ring = 1
    cells = 1
    while cells + 6 * ring <= n:
        cells += 6 * ring
        ring += 1
    # Position within the ring
    pos = n - cells
    directions = [
        (0, 1, -1),   # down-right
        (-1, 1, 0),   # down
        (-1, 0, 1),   # down-left
        (0, -1, 1),   # up-left
        (1, -1, 0),   # up
        (1, 0, -1),   # up-right
    ]
    x, y, z = ring, 0, -ring
    for side in range(6):
        step = min(ring, pos)
        dx, dy, dz = directions[side]
        x += dx * step
        y += dy * step
        z += dz * step
        pos -= step
        if pos == 0:
            break
    return (x, y, z)

def hex_distance(a, b):
    ax, ay, az = cell_to_cube(a)
    bx, by, bz = cell_to_cube(b)
    return max(abs(ax - bx), abs(ay - by), abs(az - bz))

def main():
    while True:
        line = input().strip()
        if line == "00" or line == "0 0":
            break
        if ' ' in line:
            a, b = map(int, line.split())
        else:
            a, b = int(line[:len(line)//2]), int(line[len(line)//2:])
        dist = hex_distance(a, b)
        print(f"The distance between cells {a} and {b} is {dist} .")


if __name__ == "__main__":
    import sys
    from io import StringIO
    sys.stdin = StringIO("19 30\n00\n")
    main()