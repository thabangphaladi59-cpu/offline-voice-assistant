# Offline Voice Assistant - Dell D630
100% offline voice assistant that works with no internet, built on low-spec hardware.

## Why this project?
I built this on a Dell Latitude D630 with no WiFi hotspot to prove you can build AI tools offline with limited resources.

## Features
- 🎙️ Listens to voice commands offline (Vosk)
- 🗣️ Speaks back (pyttsx3)
- ⏰ Tells time, date
- 📁 Opens folders/files
- 🔌 100% offline - no API keys needed

## Tech Stack
Python, pyttsx3, SpeechRecognition, Vosk

## How to run
```bash
pip install pyttsx3 SpeechRecognition vosk pyaudio
python assistant.py
