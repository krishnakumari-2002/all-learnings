
# import tkinter as tk
# from tkinter import messagebox

# # Create the main window
# root = tk.Tk()
# root.title("Message App")
# root.geometry("350x200")

# # Ask the user to enter a message
# label = tk.Label(root, text="Enter your message:")
# label.pack(pady=10)

# # Input field
# entry = tk.Entry(root, width=35)
# entry.pack(pady=5)

# # Function to display the entered message
# def show_message():
#     user_input = entry.get()

#     messagebox.showinfo("Your Message", user_input)

# # Submit button
# submit_button = tk.Button(
#     root,
#     text="Submit",
#     command=show_message
# )
# submit_button.pack(pady=15)

# # Run the application
# root.mainloop()




import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("message box")
root.geometry("350x200")
label=tk.Label(root,text="Enter the message")
label.pack(pady=10)

entry=tk.Entry(root,width=35)
entry.pack(pady=5)

def show_message():
  user_input=entry.get()
  messagebox.showinfo("your message",user_input)


submit_button=tk.Button(
  root,
  text="Submit",
  command=show_message
)
submit_button.pack(pady=15)
root.mainloop()
