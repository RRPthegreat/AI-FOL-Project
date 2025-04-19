import tkinter as tk
from tkinter import ttk, messagebox

class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FOL Smart Home Assistant")
        self.root.geometry("500x430")
        self.root.configure(bg="#f0f0f0")

        # Title Label
        ttk.Label(self.root, text="Smart Home Assistant", font=("Helvetica", 16)).pack(pady=10)

        # Checkboxes
        self.night_var = tk.BooleanVar()
        self.home_var = tk.BooleanVar()
        self.window_var = tk.BooleanVar()
        self.temp_var = tk.BooleanVar()

        ttk.Checkbutton(root, text="Is it Night Time?", variable=self.night_var).pack(anchor='w', padx=20)
        ttk.Checkbutton(root, text="Is Someone Home?", variable=self.home_var).pack(anchor='w', padx=20)
        ttk.Checkbutton(root, text="Is Window Open?", variable=self.window_var).pack(anchor='w', padx=20)
        ttk.Checkbutton(root, text="Is Temperature Low?", variable=self.temp_var).pack(anchor='w', padx=20)

        # Button Frame
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=15)

        # Buttons
        ttk.Button(button_frame, text="Run Assistant", command=self.run_rules).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Refresh Page", command=self.refresh).grid(row=0, column=1, padx=10)

        # Output Box
        self.output_box = tk.Text(root, height=10, width=60, wrap=tk.WORD)
        self.output_box.pack(pady=10)

    def run_rules(self):
        self.output_box.delete(1.0, tk.END)

        isNightTime = self.night_var.get()
        isSomeoneHome = self.home_var.get()
        windowOpen = self.window_var.get()
        temperatureLow = self.temp_var.get()

        output = "--- Smart Home Decision System ---\n"

        if isNightTime and isSomeoneHome:
            output += "Rule: Night time & someone is home → Lights ON\n"
            output += "Action: Lights turned ON.\n"

        if not isSomeoneHome:
            output += "Rule: No one is home → Lock Doors\n"
            output += "Action: Doors are LOCKED.\n"

        if windowOpen and not isSomeoneHome:
            output += "Rule: Windows open & no one is home → Close Windows\n"
            output += "Action: Windows are CLOSED.\n"

        if temperatureLow:
            output += "Rule: Temperature is low → Turn on Heater\n"
            output += "Action: Heater is ON.\n"

        if output.strip() == "--- Smart Home Decision System ---":
            output += "No actions triggered based on current input."

        self.output_box.insert(tk.END, output)

    def refresh(self):
        # Clear checkboxes
        self.night_var.set(False)
        self.home_var.set(False)
        self.window_var.set(False)
        self.temp_var.set(False)
        # Clear output box
        self.output_box.delete(1.0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()
