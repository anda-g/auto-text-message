import customtkinter as kit
from tkinter import messagebox
import pyautogui

textArray = []
is_start = False
i = 0

app = kit.CTk()
app.title("Auto Loung Songsa -by vannda ya boii")
app.geometry("420x500")
app.resizable(False, False)

app.configure(padx=20, pady=10)

input_frame = kit.CTkFrame(app, fg_color="transparent")
input_frame.pack(pady=(20, 10), fill="x")

textAreaInput = kit.CTkTextbox(input_frame, width=300, height=30, corner_radius=8)
textAreaInput.pack(side="left", expand=True, fill="x", padx=(0, 10))


def add_text():
    new_text = textAreaInput.get("1.0", "end-1c").strip()
    if new_text:
        textArray.append(new_text)
        textArea.configure(state="normal")
        textArea.delete("1.0", "end")
        textArea.insert("1.0", "\n".join(textArray))
        textArea.configure(state="disabled")
        textAreaInput.delete("1.0", "end")


addText = kit.CTkButton(input_frame, text="Add", width=80, command=add_text)
addText.pack(side="left")

textArea = kit.CTkTextbox(app, width=300, height=300, corner_radius=8)
textArea.insert("1.0", "\n".join(textArray))
textArea.configure(state="disabled")
textArea.pack(pady=10, fill="both", expand=True)


def type_text():
    global is_start
    global i

    if is_start and textArray:
        pyautogui.write(textArray[i])
        pyautogui.press('enter')
        if i == len(textArray) - 1:
            i = 0
        else:
            i = i + 1
        app.after(1000, type_text)


def start():
    global is_start
    if not textArray:
        messagebox.showwarning("Warning", "Please add some text before starting.")
        return

    is_start = not is_start

    if is_start:
        textAreaInput.configure(state="disabled")
        button.configure(text="Stop", fg_color="#c0392b", hover_color="#a93226")
        type_text()
    else:
        textAreaInput.configure(state="normal")
        button.configure(text="Start", fg_color="#16a085", hover_color="#138d75")


button = kit.CTkButton(
    app,
    text="Start",
    fg_color="#16a085",
    hover_color="#138d75",
    height=40,
    corner_radius=8,
    command=start
)
button.pack(pady=20, fill="x")

app.mainloop()