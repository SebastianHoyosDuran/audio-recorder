import sounddevice
from scipy.io.wavfile import write

class AudioRecorder:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
class AudioRecorder:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def record_audio(self, duration, output_file="out.wav", channels=1):
        """
        Records audio for a specified duration and saves it to a WAV file.

        Args:
            duration (int): The duration of the recording in seconds.
            output_file (str, optional): The name of the output WAV file. Defaults to "out.wav".
            channels (int, optional): The number of audio channels. Defaults to 1 (mono).

        Returns:
            None

        Raises:
            None

        Note:
            This method uses the `sounddevice` library to record audio from the default input device.
            It then saves the recorded audio to a WAV file using the `scipy.io.wavfile.write` function.
            The `sample_rate` attribute of the `AudioRecorder` instance determines the sampling rate of the audio.

        Example:
            # Record audio for 5 seconds and save it to "my_recording.wav"
            recorder.record_audio(5, output_file="my_recording.wav")
        """
        print("Recording....")
        record_voice = sounddevice.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=channels)
        sounddevice.wait()
        write(output_file, self.sample_rate, record_voice)
        print("Finished recording. Please check the file:", output_file)
