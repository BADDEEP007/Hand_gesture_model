import tkinter as tk

class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gesture Controlled Smart Home")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # Devices and initial states
        self.devices = {
            'Bulb': False,
            'Fan': False,
            'Music': False
        }

        # Create canvas for visual representation
        self.canvas = tk.Canvas(root, width=500, height=300, bg="#ffffff")
        self.canvas.pack(pady=10)

        # Draw devices (placeholders)
        self.draw_devices()

        # Status label
        self.status_label = tk.Label(root, text="Waiting for gesture...", bg="#f0f0f0", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def draw_devices(self):
        self.canvas.delete("all")

        # Bulb
        self.canvas.create_oval(50, 50, 100, 100, fill="yellow" if self.devices['Bulb'] else "gray", tags="bulb")
        self.canvas.create_text(75, 110, text="Bulb", font=("Arial", 10))

        # Fan
        self.canvas.create_oval(200, 50, 250, 100, fill="skyblue" if self.devices['Fan'] else "gray", tags="fan")
        self.canvas.create_text(225, 110, text="Fan", font=("Arial", 10))

        # Music
        self.canvas.create_rectangle(350, 50, 400, 100, fill="green" if self.devices['Music'] else "gray", tags="music")
        self.canvas.create_text(375, 110, text="Music", font=("Arial", 10))

    def turn_on_device(self, device):
        self.devices[device] = True
        self.status_label.config(text=f"{device} turned ON")
        self.draw_devices()

    def turn_off_device(self, device):
        self.devices[device] = False
        self.status_label.config(text=f"{device} turned OFF")
        self.draw_devices()

    # Gesture handlers
    def gesture_thumb_up(self):
        self.turn_on_device('Bulb')

    def gesture_thumb_down(self):
        self.turn_off_device('Bulb')

    def gesture_closed_fist(self):
        self.turn_on_device('Fan')

    def gesture_open_palm(self):
        self.turn_off_device('Fan')

    def gesture_victory(self):
        self.turn_on_device('Music')

    def gesture_iloveyou(self):
        self.turn_off_device('Music')

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()
