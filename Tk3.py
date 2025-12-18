import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

def show_text():
    text = entry.get()
    output_label.config(text="You entered: " + text)

window = tk.Tk()
window.title("Combined Tkinter App")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=10)

button = tk.Button(window, text="Click Me", command=button_click)
button.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

show_button = tk.Button(window, text="Show Text", command=show_text)
show_button.pack(pady=10)

output_label = tk.Label(window, text="")
output_label.pack(pady=10)
window.mainloop()
