
# WAV Gen (PyQt6 GUI)

<p align="center">
  <img alt="type" src="https://img.shields.io/badge/type-PyQt6%20GUI-blue">
  <img alt="audio" src="https://img.shields.io/badge/audio-WAV%20tone%20generator-blueviolet">
  <img alt="python" src="https://img.shields.io/badge/python-3.10%2B-orange">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-green">
</p>

A small **PyQt6 desktop app** that generates a **mono sine-wave WAV** file.  
Set sample rate, duration, frequency, volume, choose an output folder, and export a `.wav`.


## What’s inside
- `wav_gen.py` — main application (loads the UI, handles events, generates the WAV output)
- `interface_gen.py` — PyQt6 UI layout (generated UI class used by `wav_gen.py`)

## Features
- Folder picker for output directory
- Generates **mono** WAV (16-bit PCM)
- Adjustable parameters:
  - Sample rate (e.g., 44100)
  - Duration (seconds)
  - Frequency (Hz)
  - Volume (float)
  - Output filename

## Requirements
- Python 3.x
- PyQt6

Install:
```bash
pip install PyQt6
```

## Run
```bash
python wav_gen.py
```

## Usage
1. Run the app.
2. Click **Select Folder** and choose where to save the file.
3. Enter:
   - sample rate
   - duration (seconds)
   - frequency (Hz)
   - volume
   - output filename
4. Click **Generate** to create the `.wav`.

## Output
The app saves the generated file to:
`<selected_folder>/<filename>.wav`

## Third‑party reference (MIT)
The WAV generation logic in this project is **adapted** from the MIT-licensed script:

- **Alessandro Cudazzo** — “Generate a sine wave and save it in a wav file” (`sine_wave.py`)  
  https://gist.github.com/alessandrocuda/9df6043b79e68e3ddc1c262eddcfa015

If you further modify the WAV generation code, keep the attribution in the source file(s) that include adapted portions.

## Notes
- Output is **mono** only (this GUI version focuses on mono export).
- `interface_gen.py` is generated UI code; typically you only edit logic in `wav_gen.py`.
