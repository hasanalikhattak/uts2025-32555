import tkinter as tk
from tkinter import Toplevel

# --- Functions ---

def submit_action():
    """
    Creates a new window to show a "working" message.
    """
    # Create a new top-level window
    working_window = Toplevel(root)
    working_window.title("Status")
    working_window.geometry("200x100")
    
    # Add a label to the new window
    working_label = tk.Label(working_window, text="working", font=("Helvetica", 16))
    working_label.pack(pady=30) # pack is used to place the widget

def cancel_action():
    """
    Clears the username and password entry fields.
    """
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    # Set focus back to the username field
    username_entry.focus_set()

# --- GUI Setup ---

# Create the main window
root = tk.Tk()
root.title("Login Portal")
root.geometry("300x150") # Set the size of the window

# Create a frame to hold the widgets for better organization
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack(expand=True)

# Username Label and Entry
username_label = tk.Label(main_frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w", pady=5) # sticky="w" aligns to the west (left)

username_entry = tk.Entry(main_frame)
username_entry.grid(row=0, column=1, pady=5)

# Password Label and Entry
password_label = tk.Label(main_frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w", pady=5)

password_entry = tk.Entry(main_frame, show="*") # 'show="*" masks the password
password_entry.grid(row=1, column=1, pady=5)

# Buttons Frame
buttons_frame = tk.Frame(main_frame)
buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

# Submit Button
submit_button = tk.Button(buttons_frame, text="Submit", command=submit_action)
submit_button.pack(side="left", padx=5)

# Cancel Button
cancel_button = tk.Button(buttons_frame, text="Cancel", command=cancel_action)
cancel_button.pack(side="left", padx=5)

# Start the main event loop
root.mainloop()