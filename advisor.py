import requests
import tkinter as tk
from tkinter import messagebox

def get_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        response.raise_for_status()
        data = response.json()
        advice = data["slip"]["advice"]
        advice_message.set(advice)  # Put advice in the label, not popup
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch advice: {e}")

app = tk.Tk()
app.title("Advice App")

advice_message = tk.StringVar()
message_label = tk.Label(app, textvariable=advice_message, wraplength=400, font=("Arial", 12))

fetch_button = tk.Button(app, text="Get Advice", command=get_advice)
message_label.pack(pady=20)
fetch_button.pack(pady=10)

get_advice()
app.mainloop()
