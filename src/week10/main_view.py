import tkinter as tk
from frame_view import LoginFrame
from model import Database

root = tk.Tk()
root.geometry("450x250")
root.title("Bank GUI Login Module")
root.configure(bg='#607b8d')
root.resizable(False, False)

# Connect the main view to database
db = Database()

# load the login frame on the main window
login_frame = LoginFrame(root, db)

root.mainloop()