import tkinter as tk
from tkinter import filedialog, messagebox
import pygame
import webview  # For embedding SoundCloud in a separate window
import os

# Initialize pygame mixer
pygame.mixer.init()

# Function to load and play local music
def load_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        song_label.config(text=f"Playing: {os.path.basename(file_path)}")

# Function to play the default twinkle.mp3
def play_music():
    if not pygame.mixer.music.get_busy():
        if os.path.exists("twinkle.mp3"):
            pygame.mixer.music.load("twinkle.mp3")
            pygame.mixer.music.play()
            song_label.config(text="Playing: twinkle.mp3")
        else:
            messagebox.showerror("Error", "twinkle.mp3 not found!")

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    song_label.config(text="Music Stopped")

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()
    song_label.config(text="Music Paused")

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()
    song_label.config(text="Music Resumed")

# Function to set the volume
def set_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# Function to embed and play SoundCloud music in a separate window
def play_soundcloud():
    url = "https://soundcloud.com/forss/flickermood"  # Replace with any SoundCloud track URL
    webview.create_window('SoundCloud Player', url, width=600, height=400)
    webview.start()
    song_label.config(text="Streaming from SoundCloud")

# Create the main window
root = tk.Tk()
root.title("Enhanced Music Player with SoundCloud")
root.geometry("400x400")

# Song/Status label
song_label = tk.Label(root, text="No Song Playing", font=("Helvetica", 12))
song_label.pack(pady=10)

# Buttons for local music
load_button = tk.Button(root, text="Load Music", command=load_music)
load_button.pack(pady=5)

play_button = tk.Button(root, text="Play Default", command=play_music)
play_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=5)

resume_button = tk.Button(root, text="Resume", command=resume_music)
resume_button.pack(pady=5)

# Volume control
volume_label = tk.Label(root, text="Volume")
volume_label.pack(pady=5)
volume_scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=set_volume)
volume_scale.set(50)  # Default volume at 50%
volume_scale.pack(pady=5)

# Divider
divider = tk.Label(root, text="------------------------------")
divider.pack(pady=10)

# Button for SoundCloud streaming
soundcloud_button = tk.Button(root, text="Play SoundCloud Track", command=play_soundcloud)
soundcloud_button.pack(pady=5)

root.mainloop()