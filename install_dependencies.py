import os
import subprocess

# List of required dependencies
dependencies = [
    "eel", "pyaudio", "pyautogui", "pvporcupine", "hugchat", "playsound"
]

# Install dependencies
for package in dependencies:
    try:
        subprocess.run(["pip", "install", package], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}. Try manually installing it.")

print("All dependencies installed successfully!")
