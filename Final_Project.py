import tkinter as tk
from tkinter import filedialog, scrolledtext
from pdf2image import convert_from_path
import pytesseract
from openai import OpenAI
import os

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

selected_file = None
summary_text = ""


def get_poppler_path():
    return None


def extract_text_from_pdf(pdf_path):
    poppler_path = get_poppler_path()

    try:
        if poppler_path:
            pages = convert_from_path(pdf_path, poppler_path=poppler_path)
        else:
            pages = convert_from_path(pdf_path)

        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page) + "\n"

        return text

    except Exception as e:
        return f"ERROR: {str(e)}"


def summarize(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a study assistant."},
            {
                "role": "user",
                "content": f"""
Turn these notes into a clean bullet-point study guide.

RULES:
- Bullet points only
- Group ideas clearly
- Remove repetition

NOTES:
{text}
"""
            }
        ]
    )

    return response.choices[0].message.content


def process_file():
    global summary_text

    if not selected_file:
        output_box.insert(tk.END, "⚠ Please select a file first.\n")
        return

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, "Processing PDF... please wait.\n")

    raw_text = extract_text_from_pdf(selected_file)

    if raw_text.startswith("ERROR"):
        output_box.insert(tk.END, f"\n❌ {raw_text}\n")
        return

    if not raw_text.strip():
        output_box.insert(tk.END, "❌ No readable text found.\n")
        return

    summary_text = summarize(raw_text)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, summary_text)

    preview_box.delete("1.0", tk.END)
    preview_box.insert(tk.END, create_preview(summary_text))


def create_preview(text):
    return f"""
STUDY GUIDE PREVIEW

{text[:800]}...

✓ Cleaned notes generated
✓ Organized bullet points
✓ Study-ready format
"""


def select_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    output_box.insert(tk.END, f"Selected: {selected_file}\n")


def save_file():
    if not summary_text:
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(summary_text)


# --- UI SETUP (SINGLE WINDOW ONLY) ---

app = tk.Tk()
app.title("AI PDF Notes Summarizer (Fixed)")
app.geometry("900x650")

title = tk.Label(app, text="AI PDF Notes Summarizer", font=("Arial", 18))
title.pack(pady=10)

# Drag box (click to select)
drag_frame = tk.Frame(app, bd=2, relief="groove", width=400, height=120)
drag_frame.pack(pady=10)

drag_label = tk.Label(
    drag_frame,
    text="Drag PDF Here\n(or click to select)",
    font=("Arial", 12)
)
drag_label.pack(pady=20)

drag_frame.bind("<Button-1>", lambda e: select_file())
drag_label.bind("<Button-1>", lambda e: select_file())

# Buttons
btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Submit File", command=process_file).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Save New File", command=save_file).grid(row=0, column=1, padx=10)

# Output box
output_box = scrolledtext.ScrolledText(app, width=100, height=15)
output_box.pack(pady=10)

# Preview box
tk.Label(app, text="Preview", font=("Arial", 14)).pack()

preview_box = scrolledtext.ScrolledText(app, width=100, height=10)
preview_box.pack(pady=10)

app.mainloop()

