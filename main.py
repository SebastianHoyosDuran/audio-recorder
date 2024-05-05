from audio_recorder import AudioRecorder

def main():
    sample_rate = 44100
    duration = int(input("Enter the time duration in seconds: "))
    recorder = AudioRecorder(sample_rate)
    recorder.record_audio(duration)

if __name__ == "__main__":
    main()
