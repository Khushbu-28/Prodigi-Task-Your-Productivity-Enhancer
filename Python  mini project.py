import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from datetime import datetime, timedelta
from tkinter import scrolledtext, filedialog
# Global variables 
thought_label = None
entry = None
listbox = None
journal_entry = None
end_time = None  # Declare end_time as global
start_focus_timer_func=None
winner=None
# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "cummins" and password == "miniproject":
        messagebox.showinfo("Success", "Login Successful")
        open_welcome_page()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Function to open the welcome page
def open_welcome_page():
    root.withdraw()  # Hide the login window
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome to Prodigi")
    welcome_window.geometry("1000x100")
    welcome_window.configure(bg="sky blue")

    # Create a label to display a good thought
    global thought_label  # Declare as global
    thought_label = tk.Label(welcome_window, text="Coding is today's language of creativity", font=("Times", "24", "bold italic"), bg="sky blue", fg="black")
    thought_label.pack()
    display_thought()

    # Create a dictionary of menu options
    menu_options = {
        "To-Do List": "📋",
        "Focus Mode Timer": "⏲️",
        "Notes Making": "📝",
        "Journaling": "📔",
        "Brain Games": "🧠",
    }

    # Create and display menu buttons with text-based icons
    menu_frame = tk.Frame(welcome_window,bg="peachpuff2")
    menu_frame.pack(pady=25)
    for option, icon in menu_options.items():
        button = tk.Button(menu_frame, text=f"{icon}\n{option}", font=("Segoe Script",25),bg="LemonChiffon2",
                           command=lambda opt=option: on_select(opt))
        button.pack(side=tk.TOP, padx=25, pady=10)

# Function to display a good thought
def display_thought():
    thought = "Coding is today's language of creativity."
    thought_label.config(text=thought)

# Function to handle menu option selection
def on_select(selected_option):
    if selected_option == "To-Do List":
        open_todo_list()
    elif selected_option == "Focus Mode Timer":
        open_focus_timer()
    elif selected_option == "Notes Making":
        open_notes_making()
    elif selected_option == "Journaling":
        open_journaling()
    elif selected_option == "Brain Games":
        open_brain_games()
    else:
        messagebox.showerror("Error", "Please select an option.")

# Function to open the To-Do List page
def open_todo_list():
    root.withdraw()  # Hide the welcome window
    todo_list_window = tk.Toplevel()
    todo_list_window.title("To-Do List")
    todo_list_window.geometry("700x600")
    todo_list_window.configure(bg="sky blue")
    
    
    # Create an entry field for adding tasks
    global entry  # Declare as global
    entry = tk.Entry(todo_list_window, width=40, font=("BOLD", 45),bg="burlywood1")
    entry.pack()

    # Create a button to add tasks
    add_button = tk.Button(todo_list_window, text="Add Task",width=20,height=1, command=add_task,font=("BOLD",25), bg="Pink", fg="black")
    add_button.pack()

    # Create a listbox to display tasks
    global listbox  # Declare as global
    listbox = tk.Listbox(todo_list_window,width=35, selectmode=tk.SINGLE,font=("Times",30),bg="burlywood1")
    listbox.pack()

    # Create a button to delete selected tasks
    delete_button = tk.Button(todo_list_window, text="Delete Task", width=20,height=1,command=delete_task,font=("BOLD",25), bg="light green", fg="black")
    delete_button.pack()

# Function to open the Focus Mode Timer page
def open_focus_timer():
    root.withdraw()  # Hide the welcome window
    focus_timer_window = tk.Toplevel()
    focus_timer_window.title("Focus Mode Timer")
    focus_timer_window.geometry("400x200")
    focus_timer_window.configure(bg="pale turquoise")

    # Create a label and entry for setting the focus time
    focus_label = tk.Label(focus_timer_window, text="Enter focus time (minutes):", font=("BOLD", 16), bg="pale turquoise")
    focus_label.pack()
    global entry  # Declare as global
    entry = tk.Entry(focus_timer_window, font=("Helvetica", ))
    entry.pack()

    # Create a label for displaying the timer
    timer_label = tk.Label(focus_timer_window, text="", font=("Helvetica", 24), bg="pale turquoise")
    timer_label.pack()

    def start_focus_timer():
        global end_time
        minutes = int(entry.get())
        end_time = datetime.now() + timedelta(minutes=minutes)
        update_timer()

    # Create a button to start the timer
    start_button = tk.Button(focus_timer_window, text="Start Focus Timer", command=start_focus_timer, font=("Helvetica", 16), bg="light blue", fg="white")
    start_button.pack()

    def update_timer():
        current_time = datetime.now()
        remaining_time = end_time - current_time
    
        if remaining_time.total_seconds() > 0:
            minutes, seconds = divmod(int(remaining_time.total_seconds()), 60)
            timer_label.config(text=f"{minutes:02}:{seconds:02}", font=("Helvetica", 24), fg="green")
            timer_label.after(1000, update_timer)
        else:
            timer_label.config(text="Focus time is up!", font=("Helvetica", 20), fg="red")

# Function to add a task to the to-do list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

# Function to delete a selected task from the to-do list
def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

def save_note():
    note_content = text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(note_content)

def clear_note():
    text.delete("1.0", tk.END)
    
    
def open_notes_making():
    root.withdraw()  # Hide the welcome window
    notes_making_window = tk.Toplevel()
    notes_making_window.title("Notes Making")
    notes_making_window.geometry("500x400")
    notes_making_window.configure(bg="sky blue")
    # Create a text area for making notes
    global text  # Declare as global
    text = scrolledtext.ScrolledText(notes_making_window, width=100, height=30, font=("Helvetica", 15), bg="Light yellow", fg="black")
    text.pack()

    # Create buttons to save and clear notes
    save_button = tk.Button(notes_making_window, text="Save Note",width=23,height=3, font=("courior new",15,"bold"), command=save_note, bg="light green", fg="black")
    clear_button = tk.Button(notes_making_window, text="Clear Note", width=23,height=3, font=("courior new",15,"bold"),command=clear_note, bg="Pink", fg="black")

    save_button.pack()
    clear_button.pack()

# Function to save a journal entry
def save_entry():
    entry_text = journal_entry.get("1.0", "end-1c")
    if not entry_text.strip():
        messagebox.showwarning("Empty Entry", "Please write something before saving.")
        return

    with open("journal.txt", "a") as file:
        file.write(entry_text + "\n")
    messagebox.showinfo("Saved", "Your journal entry has been saved.")

# Function to clear the journal entry text area
def clear_entry():
    journal_entry.delete("1.0", "end")

# Function to load journal entries
def load_entries():
    try:
        with open("journal.txt", "r") as file:
            entries = file.readlines()
        journal_entry.delete("1.0", "end")
        for entry in entries:
            journal_entry.insert("end", entry)
    except FileNotFoundError:
        messagebox.showinfo("No Entries", "No journal entries found.")

def open_journaling():
    root.withdraw()  # Hide the welcome window
    journaling_window = tk.Toplevel()
    journaling_window.title("Journaling Application")
    journaling_window.geometry("600x400")
    journaling_window.configure(bg="cadet blue")

    # Create a text area for journal entries
    global journal_entry  # Declare as global
    journal_entry = ScrolledText(journaling_window, width=123, height=36, font=("Helvetica", 12,"bold"), bg="Light yellow", fg="black")
    journal_entry.pack()

    # Create buttons to save, clear, and load entries
    save_button = tk.Button(journaling_window, text="Save Entry", width=15,height=2,font=("Helvetica", 12,"bold"),command=save_entry, bg="Light blue", fg="black")
    clear_button = tk.Button(journaling_window, text="Clear Entry", width=15,height=2,font=("Helvetica", 12,"bold"),command=clear_entry, bg="Pink", fg="black")
    load_button = tk.Button(journaling_window, text="Load Entries", width=15,height=2,font=("Helvetica", 12,"bold"),command=load_entries, bg="Light coral", fg="white")

    save_button.pack()
    clear_button.pack()
    load_button.pack()
    
    
def open_brain_games():
    root = tk.Tk()  # Create the main window
    root.withdraw()  # Hide the welcome window
    brain_games_window = tk.Toplevel()
    brain_games_window.title("Brain Games")
    brain_games_window.geometry("800x600")
    brain_games_window.configure(bg="sky blue")
    global winner  # Declare 'winner' as global

    def open_tic_tac_toe():
        def check_winner(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):
                    return True
                if all(board[j][i] == player for j in range(3)):
                    return True
            if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
                return True

        def draw_board():
            for i in range(3):
                for j in range(3):
                    cell = tk.Button(tic_tac_toe_window, text=board[i][j], width=20, height=6, font=("Helvetica", 20, "bold"), bg="DarkSlateGray1", command=lambda row=i, col=j: make_move(row, col))
                    cell.grid(row=i, column=j)

        def make_move(row, col):
            global winner  # Declare 'winner' as global
            if board[row][col] == " " and not winner:
                board[row][col] = current_player
                draw_board()
                if check_winner(board, current_player):
                    messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
                    winner = True
                elif all(cell != " " for row in board for cell in row):
                    messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                else:
                    switch_player()

        def switch_player():
            nonlocal current_player
            current_player = "X" if current_player == "O" else "O"

        tic_tac_toe_window = tk.Toplevel(brain_games_window)
        tic_tac_toe_window.title("Tic-Tac-Toe")
        tic_tac_toe_window.geometry("600x600")

        # Center the Tic-Tac-Toe window
        window_width = tic_tac_toe_window.winfo_reqwidth()
        window_height = tic_tac_toe_window.winfo_reqheight()
        screen_width = tic_tac_toe_window.winfo_screenwidth()
        screen_height = tic_tac_toe_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        tic_tac_toe_window.geometry(f"+{x}+{y}")

        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        global winner  # Declare 'winner' as global
        winner = False

        draw_board()

    def show_game_buttons():
        tic_tac_toe_button.pack()

    # Create a notebook for Brain Games
    brain_games_tabs = ttk.Notebook(brain_games_window)

    tic_tac_toe_button = tk.Button(brain_games_window, text="Tic-Tac-Toe", command=open_tic_tac_toe, bg="Pink", fg="black", width=15, height=10, font=("Helvetica", 30))

    show_game_buttons()

    # Display the main window
    brain_games_window.mainloop()


# Create the main window
root = tk.Tk()
root.title("Prodigi - Productivity Enhancer")
root.geometry("400x300")

# Define a soft matte blue background color
background_color = "thistle"

# Create a background canvas
canvas = tk.Canvas(root, bg=background_color)
canvas.pack(fill="both", expand=True)

# Create a login frame
login_frame = tk.Frame(canvas, bg="pale turquoise", bd=10)
login_frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)

# Create a label for the title
title_label = tk.Label(login_frame, text="Welcome to Prodigi Task", font=("Segoe Script", 50), bg="thistle")
title_label.pack(pady=20)

# Create labels and entry widgets for username and password
username_label = tk.Label(login_frame, text="Username:", bg="thistle", font=("Segoe Script", 19))
username_label.pack()
username_entry = tk.Entry(login_frame, bg="light gray", relief="ridge", borderwidth=5, font=("Segoe Script", 19), width=20)
username_entry.pack(pady=10)

password_label = tk.Label(login_frame, text="Password:", bg="thistle", font=("Segoe Script", 19))
password_label.pack()
password_entry = tk.Entry(login_frame, show="*", bg="light gray", relief="ridge", borderwidth=5, font=("Segoe Script", 19), width=20)
password_entry.pack(pady=10)

# Create a login button with matte blue color
login_button = tk.Button(login_frame, text="Login", bg=background_color, fg="black", command=login, font=("Segoe Script", 19))
login_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()



