import tkinter as tk
import re

def check_password():
    password = entry.get()
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letter")

    if re.search("[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letter")

    if re.search("[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add number")

    if re.search("[@#$%^&*!]", password):
        strength += 1
    else:
        suggestions.append("Add special character")

    # Strength result + color    
    if strength <= 2:
        result = "Weak 😡"
        color = "red"
    elif strength <= 4:
        result = "Medium 😐"
        color = "orange"
    else:
        result = "Strong 💪"
        color = "green"
    
    output_label.config(text="Strength: " + result, fg=color)

    suggestion_text = "\n".join(suggestions)
    suggestion_label.config(text=suggestion_text)

    # Progress bar
    progress.set((strength/5)*100)

def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
    else:
        entry.config(show='*')    

# Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")

# Label
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

# Input
entry = tk.Entry(root, show="*", width=30)
entry.pack()

# Show/Hide button
tk.Button(root, text="Show/Hide", command=toggle_password).pack(pady=5)

# Check Button
tk.Button(root, text="Check Strength", command=check_password).pack(pady=10)

# Output
output_label = tk.Label(root, text="", font=("Arial", 12))
output_label.pack()

suggestion_label = tk.Label(root, text="", font=("Arial", 10))
suggestion_label.pack()

# Progress bar
progress = tk.DoubleVar()
tk.Scale(root, variable=progress, from_=0, to=100, orient='horizontal', length=250, label="Strength Meter").pack(pady=10)

# Run window
root.mainloop()