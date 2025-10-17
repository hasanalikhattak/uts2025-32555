from controller import Controller
import tkinter as tk
import tkinter.messagebox as mb

class ConfirmationView(tk.Toplevel):
    def __init__(self, master, msg):
        super().__init__(master=master)
        self.title("Welcome")
        self.geometry("250x120")
        # Place to the right of the main window
        x = master.winfo_x() + master.winfo_width() + 10
        y = master.winfo_y()
        self.geometry(f"250x120+{x}+{y}")
        self.configure(bg='#b2c7d9')
        self.resizable(False, False)
        label = tk.Label(self, text=msg, font=("Arial", 12), bg='#b2c7d9')
        label.pack(pady=20)
        close_btn = tk.Button(self, text="Close", command=self.destroy, width=10)
        close_btn.pack(pady=5)

class FrameOnly(tk.LabelFrame):
    def __init__(self, master) -> None:
        super().__init__(master, text="Frame Only", bg='#b2c7d9', font=("Arial", 12, "bold"))
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        label = tk.Label(self, text="This is a frame only.", bg='#b2c7d9', font=("Arial", 10))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

class LoginFrame(tk.LabelFrame):
    
    # Complete the function clear to clear fields content
    def clear(self):
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        
    # Complete the login function to match input fields data with model data
    # - If the customer exist, open a new confirmation window the the welcome message
    # - If the credentials are incorrect open a pop-up error notification
    def login(self, master, model):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        user = model.match(email, password)
        if user:
            from controller import Controller
            Controller.save(user)
            msg = f"Welcome, {user.name}!"
            ConfirmationView(master, msg)
        else:
            # Standalone modal error pop-up
            error_win = tk.Toplevel(self)
            error_win.title("Login Failed")
            error_win.geometry("280x100")
            error_win.resizable(False, False)
            error_win.grab_set()  # Modal
            error_win.configure(bg='#f8d7da')
            label = tk.Label(error_win, text="Incorrect email or password.", fg="#721c24", bg="#f8d7da", font=("Arial", 11))
            label.pack(pady=15)
            btn = tk.Button(error_win, text="OK", width=10, command=error_win.destroy)
            btn.pack(pady=5)
            error_win.transient(self)
            error_win.focus_force()
   
    # Complete the constructor function 
    def __init__(self, master, model) -> None:
        super().__init__(master, text="Sign In", bg='#b2c7d9', font=("Arial", 12, "bold"))
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        # Email label and entry
        email_label = tk.Label(self, text="Email", bg='#b2c7d9', font=("Arial", 10))
        email_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.email_entry = tk.Entry(self, width=25)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Password label and entry
        password_label = tk.Label(self, text="Password", bg='#b2c7d9', font=("Arial", 10))
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_entry = tk.Entry(self, show="*", width=25)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Buttons
        login_btn = tk.Button(self, text="Login", width=10, command=lambda: self.login(master, model))
        login_btn.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        cancel_btn = tk.Button(self, text="Cancel", width=10, command=master.quit)
        cancel_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")