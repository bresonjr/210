import socket
import tkinter as tk
import os
import pygame.mixer

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 1234
IP_ADDRESS = (SERVER, PORT)
song_counter = 0

def setup():
    global SERVER, PORT, IP_ADDRESS
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(IP_ADDRESS)
    print("Connected to {}:{}".format(SERVER, PORT))
    musicWindow()

def getMusicFiles():
    global song_counter
    music_files = []
    for root, dirs, files in os.walk("/path/to/music/directory"):
        for file in files:
            if file.endswith(".mp3"):
                music_files.append(file)
                song_counter += 1
    return music_files

def play():
    global song_selected
    song_selected = listbox.curselection()[0]
    pygame.mixer.music.load(music_files[song_selected])
    pygame.mixer.music.play()
    if pygame.mixer.music.get_busy():
        infor_label["text"] = "Playing: " + music_files[song_selected]
    else:
        infor_label["text"] = ""

def stop():
    global song_selected
    song_selected = listbox.curselection()[0]
    pygame.mixer.music.stop()
    infor_label["text"] = ""

def resume():
    global song_selected
    song_selected = listbox.curselection()[0]
    pygame.mixer.music.unpause()
    infor_label["text"] = "Resumed: " + music_files[song_selected]

def pause():
    global song_selected
    song_selected = listbox.curselection()[0]
    pygame.mixer.music.pause()
    infor_label["text"] = "Paused: " + music_files[song_selected]

def musicWindow():
    global music_files, listbox, infor_label
    music_files = getMusicFiles()
    root = tk.Tk()

    # Create the GUI elements
    selectsong_label = tk.Label(root, text="Select Song:")
    selectsong_label.pack()

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
    for i, song in enumerate(music_files):
        listbox.insert(tk.END, song)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar.config(command=listbox.yview)

    play_button = tk.Button(root, text="Play", command=play)
    play_button.pack()

    stop_button = tk.Button(root, text="Stop", command=stop)
    stop_button.pack()

    resume_button = tk.Button(root, text="Resume", command=resume)
    resume_button.pack()

    pause_button = tk.Button(root, text="Pause", command=pause)
    pause_button.pack()

    infor_label = tk.Label(root, text="")
    infor_label.pack()

    root.mainloop()

if __name__ == "__main__":
    pygame.mixer.init()
    setup()
