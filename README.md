

# Voice Assistant

This project is a simple voice assistant written in Python. It uses the `speech_recognition` library for voice input, `pyttsx3` for text-to-speech, and `webbrowser` for opening websites. The assistant can recognize voice commands to open various websites and device applications, tell the current time, and perform Google searches.

## Requirements

- Python 3.x
- `speech_recognition` library
- `pyttsx3` library
- Internet connection for accessing websites

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:
    ```bash
    pip install speechrecognition pyttsx3
    ```

## Usage

1. Run the script:
    ```bash
    python script_name.py
    ```
2. The assistant will greet you and start listening for commands.

## Available Commands

### Websites
You can open the following websites by saying "open [website name]":
- YouTube
- Google
- Mail
- BBC News
- CNN
- The New York Times
- ESPN
- BBC Sport
- Coursera
- Khan Academy
- Wikipedia
- Jio Cinema
- Reddit
- Facebook
- Twitter
- Instagram
- LinkedIn
- Amazon
- eBay
- Netflix
- Spotify

### Device Applications
You can open the following device applications by saying "open [application name]":
- settings
- calculator
- notepad
- command prompt
- task manager
- control panel
- file explorer
- powershell
- snipping tool
- system information
- disk management
- device manager
- event viewer
- services
- registry editor
- performance monitor

### Other Commands
- "What is the time?" - The assistant will tell you the current time.
- If no specific command is recognized, the assistant will perform a Google search for the given query.

## Stopping the Assistant
To stop the assistant, say "stop".

## Notes
- Make sure your microphone is working properly.
- The voice recognition might not be perfect and can sometimes result in errors.

## License
This project is licensed under the MIT License.

---

Feel free to modify the README file as needed.
