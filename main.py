import customtkinter as kit
from tkinter import messagebox
import pyautogui
from openai import OpenAI

textArray = []
is_start = False
i = 0

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

app = kit.CTk()
app.title("Auto Loung Songsa -by vannda ya boii")
app.geometry("420x500")
app.resizable(False, False)

app.configure(padx=20, pady=10)

input_frame = kit.CTkFrame(app, fg_color="transparent")
input_frame.pack(pady=(20, 10), fill="x")

textAreaInput = kit.CTkTextbox(input_frame, width=300, height=30, corner_radius=8)
textAreaInput.pack(side="left", expand=True, fill="x", padx=(0, 10))
textAreaInput.insert("1.0", "Describe your mistake here...")
textAreaInput.bind("<FocusIn>", lambda e: textAreaInput.delete("1.0", "end") if textAreaInput.get("1.0", "end-1c") == "Describe your mistake here..." else None)



def add_text():
    global textArray  # Declare as global to modify it
    mistake = textAreaInput.get("1.0", "end-1c")

    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            model="qwen/qwen3-4b:free",
            messages=[
                {
                    "role": "user",
                    "content": "Generate exactly 30 short, heartfelt apology sentences I can say to my girlfriend after a mistake. Which my mistake is "+ mistake+ " Each sentence must be under 20 words, emotionally supportive, caring, and enclosed in single quotes. Return as plain text: 'sentence 1', 'sentence 2', ..., 'sentence 30'. No newlines, no numbers, no brackets, no explanation—just one line of text."
                }
            ]
        )

        response_text = completion.choices[0].message.content

        textArray = [
            line.strip().strip("'")
            for line in response_text.split('\n')
            if line.strip()  # Skip empty lines
        ]

        textArea.configure(state="normal")
        textArea.delete("1.0", "end")
        textArea.insert("end", "\n".join(textArray))
        textArea.configure(state="disabled")

        print("Successfully added to textArray:", textArray)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate text: {str(e)}")
    finally:
        addText.configure(text="Generate")




addText = kit.CTkButton(input_frame, text="Generate", width=80, command=add_text)
addText.pack(side="left")

textArea = kit.CTkTextbox(app, width=300, height=300, corner_radius=8)
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
        app.after(2000, type_text)


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