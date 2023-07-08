import tkinter as tk
from tkinter import ttk


def submit():
    ratings = [step_bar.get() for step_bar in step_bars]
    print("Ratings:", ratings)


# Create the main window
root = tk.Tk()
root.title("Preference System")

# Create a list to store the step bars
step_bars = []

# Create four step bars
for i in range(4):
    frame = ttk.Frame(root, padding="10")
    frame.pack()

    label = ttk.Label(frame, text=f"Item {i+1}")
    label.pack(side="left")

    step_bar = ttk.Scale(frame, from_=0, to=10,
                         orient="horizontal", length=200)
    step_bar.pack(side="left")

    step_bars.append(step_bar)

# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the GUI
root.mainloop()
