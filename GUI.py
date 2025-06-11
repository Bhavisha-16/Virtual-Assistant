from tkinter import *
from PIL import Image, ImageTk
import Action
import Speech_to_Text

root = Tk()
root.title("AI Assistant")
root.geometry("550x670")
root.resizable(False, False)
root.config(bg="#FFD343")

# ask function
def ask():
    user_val = Speech_to_Text.Speech_to_Text()
    bot_val = Action.process(user_val)
    text.insert(END, 'User---> ' + user_val + "\n")
    if bot_val:
        text.insert(END, "BOT <--- " + str(bot_val) + "\n")
    if bot_val == "Ok Bhavisha":
        root.destroy()

# send function
def send():
    send = entry.get()
    bot = Action.process(send)
    text.insert(END, 'User---> ' + send + "\n")
    if bot:
        text.insert(END, "BOT <--- " + str(bot) + "\n")
    if bot == "Ok Bhavisha":
        root.destroy()

# delete function
def delete():
    text.delete('1.0', END)

# frame
frame = LabelFrame(root, padx=20, pady=7, borderwidth=3, relief="raised", bg="#FFD343")
frame.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
frame.grid_columnconfigure(0, weight=1)
# text label
text_label = Label(frame, text="AI Assistant", font=("comic sans ms", 16, "bold"), bg="#436fff")
text_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

# image
image = ImageTk.PhotoImage(Image.open("C:/Users/Admin/Downloads/assitant.png"))
image_label = Label(frame, image=image, bg="#FFD343")
image_label.grid(row=1, column=0, pady=20, sticky="ew")

# text widget
text = Text(root, font=('courier', 10, 'bold'), bg="#436fff")
text.grid(row=1, column=0, padx=50, pady=10, sticky="nsew")

# entry widget
entry = Entry(root, justify=CENTER)
entry.grid(row=2, column=0, padx=100, pady=10, sticky="ew")

# buttons frame
buttons_frame = Frame(root, bg="#FFD343")
buttons_frame.grid(row=3, column=0, pady=10, sticky="ew")
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)
buttons_frame.grid_columnconfigure(2, weight=1)

# ask button
Button(buttons_frame, text="Ask", bg="#436fff", pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask).grid(row=0, column=0, padx=10)

# send button
Button(buttons_frame, text="Send", bg="#436fff", pady=16, padx=40, borderwidth=3, relief=SOLID, command=send).grid(row=0, column=1, padx=10)

# delete button
Button(buttons_frame, text="Delete", bg="#436fff", pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete).grid(row=0, column=2, padx=10)

# Make the GUI responsive
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
