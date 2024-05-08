# Python Audio Recorder

This project provides a simple and user-friendly Python class `AudioRecorder` for capturing audio input from your default recording device and saving it as a WAV file.

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. You can verify this by running `python3 --version` or `python --version` in your terminal. If you don't have Python, download and install it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Installing

1. **Clone the Repository:**

   ```bash
   git clone https://your_github_repository_url.git
   ```

2. **Install Dependencies:**

Navigate to the project directory:

```bash
  cd python-audio-recorder
```

Then, install the required libraries using pip:

```bash
   pip install -r requirements.txt
```

## Usage

Once the dependencies are installed, you can start using the AudioRecorder class:

1. **Run the Script:**

```bash
    python main.py
```

This will execute the main.py script, which prompts you for the desired recording duration and handles the recording process.

2. **Record Audio:**
   The script will ask you to enter the recording time in seconds. Type in the desired duration and press Enter.
   The script will then initiate the recording process, displaying a message indicating that recording is in progress.

3. **Save Recording:**
   After the specified duration, the recording will stop, and a message will be displayed confirming the recording completion and indicating the location of the saved WAV file (defaulting to "out.wav").

### Features

Captures audio input from the default recording device.
Saves recordings as WAV files.
Provides a user-friendly interface for specifying recording duration.
Utilizes the sounddevice library for efficient audio recording.
Employs the scipy.io.wavfile library for seamless WAV file creation.

## Authors

Contributors names and contact info

Sebastian Hoyos
[@SebastianHoyosDuran](https://co.linkedin.com/in/sebastianhoyosduran)
