import tkinter as tk

# Create the root window
root = tk.Tk()

# Create a text label
label = tk.Label(root, text="This text is bold and underlined in red!", 
                 font=("Helvetica", 10, "bold underline"), 
                 fg="red")

# Display the label in the window
label.pack()

# Start the program
root.mainloop()
