import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Initialize the task counter
task_counter = 1

def add_to_list():
    global task_counter
    # Retrieve text from entry widget
    new_item = entry.get()
    # Check if entry is empty
    if new_item == "":
        messagebox.showwarning("Input Error", "Please add an item")
    else:
        # Add new item to the listbox with task number
        listbox.insert(tk.END, f"{task_counter}. {new_item}")
        # Clear the entry widget
        entry.delete(0, tk.END)
        # Increment the task counter
        task_counter += 1

def remove_from_list():
    # Get the selected item index
    selected_item_index = listbox.curselection()
    # Check if an item is selected
    if not selected_item_index:
        messagebox.showwarning("Selection Error", "Please Select item to remove")
    else:
        # Remove the selected item from listbox
        listbox.delete(selected_item_index)
        #renumber the tasks
        renumber_tasks()

def renumber_tasks():
    # Get all tasks
    tasks = listbox.get(0, tk.END)
    # Clear the listbox
    listbox.delete(0, tk.END)
    # goes through the remaining tasks to replace number
    for index, task in enumerate(tasks):
        # Extract the task text (without the number)
        task_text = task.split(". ", 1)[1]
        # Insert the task with the new number
        listbox.insert(tk.END, f"{index + 1}. {task_text}")


# Create the main window
window = ctk.CTk()
window.title("To-do List")
ctk.set_appearance_mode("dark")  # Set dark mode appearance

# entry widget
entry = ctk.CTkEntry(window, width=200)
entry.pack(pady=15)
entry.focus()  # Focus on entry widget

# add button
add_button = ctk.CTkButton(window, text="Add", command=add_to_list, width=10)
add_button.pack(pady=7)

# CTkFrame with rounded corners
listbox_frame = ctk.CTkFrame(window, corner_radius=15)
listbox_frame.pack(pady=15)

# listbox widget
listbox = tk.Listbox(listbox_frame, width=50, height=15, bg="grey", bd=0, highlightthickness=0, relief='flat', font=("Helvetica", 16))
listbox.pack(padx=10, pady=10)

# remove button
remove_button = ctk.CTkButton(window, text="Remove", command=remove_from_list, width=10)
remove_button.pack(pady=7)

# Start the main event loop
window.mainloop()
