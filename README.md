# Music Player with SoundCloud Streaming

This is a Python-based music player application built using **Tkinter** for the GUI and **Pygame** for audio playback. The app allows you to play local MP3 files, control playback (play, pause, stop, resume), adjust volume, and stream music from **SoundCloud** using **pywebview**.

## Features

- **Play Local Music:** Load and play MP3 files from your system.
- **Default Music Playback:** Plays a default `twinkle.mp3` file if no other file is selected.
- **Playback Controls:** Play, Pause, Stop, and Resume music easily with buttons.
- **Volume Control:** Adjust the volume using a horizontal slider.
- **SoundCloud Streaming:** Stream tracks directly from SoundCloud via an embedded browser window.

## Demo

![App Screenshot](screenshot.png)  <!-- Add a screenshot of your app if available -->

## Requirements

Make sure you have Python installed (>= 3.6 recommended).

### Install Dependencies

Use the following command to install the required libraries:

```bash
pip install pygame pywebview
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Run the application:

```bash
python music_player.py
```

3. **Optional:** Place a `twinkle.mp3` file in the same directory if you want to use the default playback feature.

## How to Use

1. **Load Local Music:** Click the "Load Music" button to choose an MP3 file from your computer.
2. **Play Default Music:** Click "Play Default" to play `twinkle.mp3`.
3. **Control Playback:** Use the Play, Pause, Stop, and Resume buttons.
4. **Adjust Volume:** Slide the volume control to adjust the volume.
5. **Stream from SoundCloud:** Click "Play SoundCloud Track" to open an embedded SoundCloud player and stream music directly.

## Customization

- **Change the SoundCloud Track:**
  - Replace the SoundCloud URL in the `play_soundcloud` function:
  
  ```python
  url = "https://soundcloud.com/forss/flickermood"  # Replace with your desired track URL
  ```

- **Modify UI:**
  - You can tweak the layout and appearance of the buttons and labels by modifying the Tkinter widgets in the code.

## Contributing

Feel free to fork this repository, submit pull requests, or open issues if you'd like to contribute!

---

**Enjoy your music! 🎵🎶**

