import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#calculates the cordinates of the cell
def precompute_coords(max_cell_num):
    coords = {}
    dirs = [(1, -1, 0), (0, -1, 1), (-1, 0, 1),
            (-1, 1, 0), (0, 1, -1), (1, 0, -1)]

    x = y = z = 0
    coords[1] = (x, y, z)
    cid = 1
    ring = 0

    while cid < max_cell_num:
        ring += 1
        dx, dy, dz = dirs[0]
        x += dx
        y += dy
        z += dz
        cid += 1
        coords[cid] = (x, y, z)

        for side in range(6):
            dir = dirs[(side + 1) % 6]
            steps = ring if side > 0 else ring - 1
            for _ in range(steps):
                if cid >= max_cell_num:
                    return coords
                x += dir[0]
                y += dir[1]
                z += dir[2]
                cid += 1
                coords[cid] = (x, y, z)
    return coords

#calculates the distance between the cells
def get_distance(a, b, coords):
    if a not in coords or b not in coords:
        raise ValueError(f"Cells {a} or {b} are not precomputed.")
    x1, y1, z1 = coords[a]
    x2, y2, z2 = coords[b]
    return (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) // 2



def compute_and_display():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        if not (1 <= a <= MAX_CELL and 1 <= b <= MAX_CELL):
            messagebox.showerror("Input Error", f"Values must be between 1 and {MAX_CELL}")
            return

        dist = get_distance(a, b, coords)
        result_label.config(text=f"Distance between cells {a} and {b} is {dist}.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integers for cell numbers.")


MAX_CELL = 10000
coords = precompute_coords(MAX_CELL)

#creating the dashboard
root = tk.Tk()
root.title("Hex Grid Distance Calculator")
image_path = r"C:\Users\Bhavana\OneDrive\Pictures\Screenshots\Screenshot 2025-06-11 105927.png"
image = Image.open(image_path)


photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.grid(row=0, column=0, columnspan=2,pady=10)

tk.Label(root, text="Enter Cell A:").grid(row=1, column=0, padx=50, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1)

tk.Label(root, text="Enter Cell B:").grid(row=1, column=3, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=4)

compute_btn = tk.Button(root, text="Compute Distance", command=compute_and_display)
compute_btn.grid(row=0, column=4, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result will appear here.")
result_label.grid(row=0, column=6, columnspan=2, pady=10)

root.mainloop()
