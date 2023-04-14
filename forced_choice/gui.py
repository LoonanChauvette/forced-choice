import tkinter as tk
import time
import threading
import random
import numpy as np
from player import Player

class SoundPlayerApp:
    def __init__(self, num_alternatives=2):
        self.num_alternatives = num_alternatives
        self.alternatives = np.arange(self.num_alternatives)
        self.step_size = 2
        self.correct = 0
        self.correct_in_a_row = 0

        self.player = Player()
        self.player.set_system_volume(50)
        self.player.set_vlc_volume(25)
        self.player.load_file("C:/Users/loona/OneDrive/Desktop/250hz_05vol_2sec.wav")
        
        self.root = tk.Tk()
        self.root.geometry("300x400")
        self.root.title("Sound Player")

        # Create the play button
        self.play_button = tk.Button(self.root, text="Play Sound")
        self.play_button.config(command=self.activate)
        self.play_button.pack(pady=10)

        self.color_buttons = []
        for alt in self.alternatives:
            color_button = tk.Button(self.root, text=f"{alt}", bg="white", width=10)
            color_button.config(command=lambda alt=alt: self.check_answer(alt))
            color_button.pack(pady=10)
            self.color_buttons.append(color_button)
        self.disable_buttons()


    def activate(self):
        self.correct = random.choice(self.alternatives)
        print(f"correct = {self.correct}")
        sound_thread = threading.Thread(target=self.play_sound)
        sound_thread.start()
        color_thread = threading.Thread(target=self.color)
        color_thread.start()
        
    def play_sound(self):
        time.sleep(0.5)
        for a in self.alternatives:
            if a == self.correct:
                self.player.play()
            else:
                time.sleep(self.player.duration / 1000)
            time.sleep(0.5)

    def color(self):
        time.sleep(0.5)
        for button in self.color_buttons:
            button.config(bg="green")
            time.sleep(self.player.duration / 1000)
            time.sleep(0.5)
            button.config(bg="white")
        self.enable_buttons()

    def check_answer(self, pressed_button):
        print(f"Pressed : {pressed_button}, correct : {self.correct}")
        correct = pressed_button == self.correct
        self.correct_answer() if correct else self.incorrect_answer()
        self.disable_buttons()

    def correct_answer(self):
        print("Correct!")
        new_volume = self.player.get_system_volume() - self.step_size
        self.player.set_system_volume(new_volume)

    def incorrect_answer(self):
        print("Incorrect!")
        new_volume = self.player.get_system_volume() + self.step_size
        self.player.set_system_volume(new_volume)

    def enable_buttons(self):
        for button in self.color_buttons:
            button.config(state=tk.NORMAL)
    
    def disable_buttons(self):
        for button in self.color_buttons:
            button.config(state=tk.DISABLED)
   
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    sound_player_app = SoundPlayerApp(num_alternatives=3)
    sound_player_app.run()

