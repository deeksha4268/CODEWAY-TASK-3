import tkinter as tk
import random
from tkinter import messagebox

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        
        self.length_label = tk.Label(root, text="Enter password length (10 digits):")
        self.length_label.pack(pady=(10, 5))
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)
        
        self.complexity_label = tk.Label(root, text="Select complexity level:")
        self.complexity_label.pack(pady=(10, 5))
        
        self.complexity_var = tk.StringVar(root)
        self.complexity_var.set("Medium")
        
        self.complexity_options = ["Low", "Medium", "High"]
        self.complexity_dropdown = tk.OptionMenu(root, self.complexity_var, *self.complexity_options)
        self.complexity_dropdown.pack(pady=5)
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack(pady=(10, 5))
        
        self.password_display = tk.Text(root, height=1, width=30)
        self.password_display.pack(pady=5)
        
        self.copy_button = tk.Button(root, text="Copy Password", command=self.copy_password)
        self.copy_button.pack(pady=10)
        
    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()
        
        if length != 10:
            messagebox.showerror("Error", "Password length must be 10 digits.")
            return
        
        password = ""
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        
        if complexity == "Low":
            for _ in range(length):
                password += random.choice(digits)
        elif complexity == "Medium":
            for i in range(length):
                if i % 2 == 0:
                    password += random.choice(alphabets)
                else:
                    password += random.choice(digits)
        elif complexity == "High":
            special_chars = '!@#$%^&*()_+{}[];:,.<>?'
            for i in range(length):
                if i % 2 == 0:
                    password += random.choice(alphabets)
                else:
                    password += random.choice(special_chars)
        
        self.password_display.delete(1.0, tk.END)
        self.password_display.insert(tk.END, password)
        
    def copy_password(self):
        password = self.password_display.get(1.0, tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        messagebox.showinfo("Password Copied", "Password has been copied to clipboard.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()

