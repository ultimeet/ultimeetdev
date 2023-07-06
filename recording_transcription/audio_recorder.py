import datetime
import wave
import pyaudio
import os

class AudioRecorder:
    def __init__(self):
        self.sample_rate = 22050
        self.duration = 1 * 60 * 60  # Duration of 3 hours (in seconds)
        self.frames = []
        self.recording = False
        self.meeting_id = ''

    def record_audio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=self.sample_rate,
                            input=True,
                            frames_per_buffer=1024)

        print("Recording started...")

        while self.recording:
            data = stream.read(1024)
            self.frames.append(data)

        print("Recording stopped.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        self.save_recording()

    def save_recording(self):
        #timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        meeting_id_rec = self.meeting_id
        print('meeting_id:',self.meeting_id)
        #filename = f"{self.meeting_id.wav}"

        filename = "{}.wav".format(self.meeting_id)

        # Change 'media' to the appropriate directory in your Django project
        file_path = os.path.join('/Users/sudarshanchavan/Desktop/my_code/', filename)

        wf = wave.open(file_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        print(f"Recording saved as '{filename}'")

