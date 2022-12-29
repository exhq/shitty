import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import subprocess
# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
email = tk.StringVar()
password = tk.StringVar()


def login_clicked():
    """ callback when the login button clicked
    """
    ssubprocess = subprocess.Popen(
        email.get() , shell=True, stdout=subprocess.PIPE)
    subprocess_return = ssubprocess.stdout.read()
    msg = subprocess_return
    showinfo(
        title='Information',
        message=msg
    )


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# email
email_label = ttk.Label(signin, text="command:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# login button
login_button = ttk.Button(signin, text="enter", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)


root.mainloop()